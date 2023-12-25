
# FAQS

<img src="./pexels-daniyal-ghanavati-110812.jpg" class="cover"/>


## 启动如何指定JAVA_HOME

```
JAVA_HOME=/usr/lib/jvm/openjdk-11-jdk /opt/loggy/scep/bin/scep.sh start
```

## Questdb的数据目录在哪里
Linux下，Questdb默认数据目录`$HOME/.questdb`， windows下`C:\Windows\System32\qdbroot`，通过`quest.sh -d path_to_data` `-d`参数执行数据目录

## Questdb的监听端口怎么修改

```
## $DAT_DIR/conf/server.conf
http.bind.to=0.0.0.0:9000
```