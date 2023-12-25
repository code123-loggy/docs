# FAQS

<img src="./pexels-daniyal-ghanavati-110812.jpg" class="cover"/>

## 启动如何指定 JAVA_HOME

```
JAVA_HOME=/usr/lib/jvm/openjdk-11-jdk /opt/loggy/scep/bin/scep.sh start
```

## Questdb 的数据目录在哪里

Linux 下，Questdb 默认数据目录`$HOME/.questdb`， windows 下`C:\Windows\System32\qdbroot`，通过`quest.sh -d path_to_data` `-d`参数执行数据目录

## Questdb 的监听端口怎么修改

```
## $DAT_DIR/conf/server.conf
http.bind.to=0.0.0.0:9000
```

更多[参考](https://questdb.io/docs/configuration/)

## Questdb 的端口

| 端口 | 配置                 | 说明              | 示例                                |
| ---- | -------------------- | ----------------- | ----------------------------------- |
| 9009 | line.tcp.net.bind.to | line 协议数据     | `line.tcp.net.bind.to=0.0.0.0:9009` |
| 9000 | http.bind.to         | Web 和 Rest 接口  | `http.bind.to=0.0.0.0:9000`         |
| 8812 | pg.net.bind.to       | postgres 协议端口 | `pg.net.bind.to=8812`               |


## Console配置文件

```
server.port=9080
## default数据库配置，用于保存配置
db.default.url=jdbc:mysql://localhost:3306/scep?useUnicode=true&characterEncoding=UTF-8&useSSL=false&connectTimeout=20000
db.default.driver=com.mysql.jdbc.Driver
db.default.user=scep
db.default.pass=123456
## tsdb 指向Questdb，假如Questdb端口有修改，请相应修改
db.tsdb.url=jdbc:postgresql://localhost:8812/qdb
db.tsdb.driver=org.postgresql.Driver
db.tsdb.user=admin
db.tsdb.pass=quest
```


## Secp配置文件
```
## 端口，用户接收filebeat的数据，对应filebeat.yml output模块的配置路径`filebeat/es/`
server.bind.ip=0.0.0.0
server.port=1234
## tsdb 对应Questdb的配置
db.tsdb.url=jdbc:postgresql://localhost:8812/qdb
db.tsdb.driver=org.postgresql.Driver
db.tsdb.user=admin
db.tsdb.pass=quest
## biz.rule.url，这两个地址指向Console服务的地址，假如Console中有修改，请做对应修改
biz.rule.url=http://localhost:9080/api/v1/jsonapi/BizRuleConfig/list
alert.rule.url=http://localhost:9080/api/v1/jsonapi/AlertRuleConfig/list
## 对应Questdb得`line.tcp.net.bind.to`
qdb.lp=localhost:9009
## 数据默认时区，不建议修改
evt.tz=+0
```