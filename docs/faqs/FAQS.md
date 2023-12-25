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
