Title:   Filebeat配置
Summary: 配置如何通过Filebeat收集日志
Date:    Nov 23, 2023

# filebeat配置

<img src="./bird-8253245_1280.jpg" class="cover"/>


filebeat是elastic开源的日志收集组件。loggy也可以直接使用它来做日志接入。
> 文中以filebeat-oss-8.7.0版本示范，其它版本可能略有区别。[下载](https://www.elastic.co/cn/downloads/past-releases/filebeat-oss-8-7-0)

## 收集日志文件
1. 首先在filebeat.yml文件中增加inputs，类型是filestream，日志路径可以使用通配符，解析部分使用了一个多行的解析，这里用日期开头来区分日志行。   

        # filebeat.yml
        filebeat.inputs:
        # 输入配置
        - type: filestream
          # Unique ID among all inputs, an ID is required.
          id: my-filestream-id
          # Change to true to enable this input configuration.
          enabled: true
          # 日志路径， linux 和 windows 参考下面例子，支持通配符
          paths:
            #- /var/log/*.log
            - D:\...\app-*.log
          parsers:
            - multiline:
                type: pattern
                pattern: '^20[0-9]{2}-[0-9]{2}-[0-9]{2}'
                negate: true
                match: after

2. 配置一个输出，loggy采用eslasticsearch格式来接收日志，所以需要选用output.elasticsearch

        # 输出配置
        output.elasticsearch:
          enabled: true
          # Array of hosts to connect to.
          hosts: ["localhost:1234/metrics-console/filebeat/es/"]
          allow_older_versions: true

3. 解析器是有点复杂，但不用担心，官方文档组织的很好。
下面就是一个从日志中提取时间的例子，这也是日常使用最多的情况之一。

        # =================================解析器配置=================================
        # 通过脚本来提取日志时间
        processors:
          - script:
              lang: javascript
              source: >
                function process(event) {
                    var str = event.Get("message");
                    var ts = str.split(" ").slice(0,2).join(" ");
                    event.Put("log_time", ts);
                }
          - timestamp:
              field: log_time
              layouts:
                - '2006-01-02 15:04:05.999'
              test:
                - '2019-11-18 04:59:51.123'
          - drop_fields:
              fields: [log_time]
        
从日志中提取时间，分三步   
第一，script来从日志中找到时间戳。例子中就是用 `javascript`，从`event`拿到`message`字段，然后用   空格来分割，取出前两段。然后通过 `Put` 来把这个日期临时保存到事件中，最后会把它删除。    
第二，用 `timestamp` 来设置日志的 `@timestamp` 字段， `layouts`表示输出格式， `test`表示输入的格式，这里的格式是 `golang` 日期格式（有点怪怪的）。   
第三，然后通过 `drop_fields` 把第一步中的临时字段删除。

## 收集syslog

1. 先在filebeat中配置一个inputs，这里配置了用udp协议监听7654端口的syslog输入。

        filebeat.inputs:
        - type: syslog
          format: rfc3164
          protocol.udp:
            host: "localhost:7654"

2. 由于loggy需要其他一些信息，我们再配置一个处理器，对数据格式稍作调整。调整后的`process`看起是这样的，`copy-fields` 和 `replace` 这两个指令是新加的。
  
        processors:
          - script:
              lang: javascript
              source: >
                function process(event) {
                    var str = event.Get("message");
                    var ts = str.split(" ").slice(0,2).join(" ");
                    event.Put("log_time", ts);
                }
          - timestamp:
              field: log_time
              layouts:
                - '2006-01-02 15:04:05.999'
              test:
                - '2019-11-18 04:59:51.123'
              fail_on_error: false
              ignore_missing: true
          - copy_fields:
              fields:
              - from: log.source.address
                to: source
              fail_on_error: false
              ignore_missing: true
          - replace:
              fields:
                - field: "source"
                  pattern: '(\d+\.\d+\.\d+\.\d+):\d+'
                  replacement: "$1"
              ignore_missing: true
              fail_on_error: false
          - drop_fields:
              fields: ["log_time","host"]

2. 配置 `/etc/rsyslog.conf`转发syslog到这个端口    
修改完成之后记得重启 rsyslog 服务

        ## 修改 /etc/rsyslog.conf，增加syslog转发到本机的9876端口，保存，重启
        *.* @localhost:9876



2. 启动filebeat后，用ss命令确认7654端口已经开启，在linux可以用logger来发送syslog来验证。
        
        logger Test Message
        

## 运行
配置文件配好之后就可以运行了。
```
filebeat -e -c filebeat.yml
```
> 其中 -e表示把日志输出到控制台，方便调试和查看。正式运行时候应该去掉这个这个参数。
