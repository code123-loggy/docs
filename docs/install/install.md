# 安装

<img src="../pexels-scott-webb-1544943.jpg" style="height:190px;width:100%; object-fit: cover;"/>

## 准备
* 硬件环境   
 4核16G 200G SSD磁盘


* 操作系统    
linux debian 11或者相关发行版（推荐）
Windows server 2022
其它基于Linux发行版

* 运行环境    
jdk 11

* 数据库    
Mysql Server 5.7    
questdb 7.2.1 下载

* 日志收集    
filebeat-oss-8.7.0 下载

## 下载
从[这里](/downloads/)下载需要的组件。

* loggy-scep 实时日志处理模块
* loggy-console 用户界面模块

## 安装
* scep安装    
解压至`/opt/loggy/scep`    
`bash /opt/loggy/scep/bin/scep.sh start`

* console安装    
解压至`/opt/loggy/console`    
`bash /opt/loggy/console/bin/console.sh start`

## 访问
打开 [http://localhost:1234](http://localhost:1234)