# SentryLog
基于 Python-Logging 日志拓展
- 封装了 Sentry日志输出
- 增加了 默认的日志出颜色

## 安装步骤
### pip install -r requirements.txt

### 环境要求
```
１.Win 系统: 请查看文档 https://www.python.org/ftp/python/ 

２.Linux　系统：

1)下载
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz

2)解压Python-3.7.0.tgz
tar -zxvf Python-3.7.0.tgz

3)建立一个空文件夹，用于存放python3程序　
mkdir /usr/local/python3 

4)执行配置文件，编译，编译安装　
cd Python-3.7.0
./configure --prefix=/usr/local/python3
make && make install

5)建立软连接
ln -s /usr/local/python3/bin/python3.7 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3.7 /usr/bin/pip3

6)测试一下python3是否可以用　
python3
```

### 案例
```
log_test : 存在小部分测试用例
```

### 配置说明
```
由于logging配置文件种类较多，以conf文件做一下说明
日志的大致流程:

输入--- 加载配置 ---- 加载处理器 ---- 加载格式 ---- 输出

通常来配置的有

1. 处理的配置
 -1- 输出的位置
 -2- 自定义输出
2. 格式的配置
 -1- 输出消息的格式
 -2- 自定义输出

需要注意：
由于logging 中源码中的Config对格式读取有一定的局限性，比如说自定义传参可能无法满足，如果需要请自行修改源码做适配
```

#### loggers
```
[loggers]
keys=x,y,z
x,y,z : 代表logging-name,也就是对应logging的名称，再配置文件中充当实例的身份上下文做分类,支持多个配置，根据不同的环境实例化供选择

比如说
logger_x : 属于x的配置

-------

[handlers]
keys=h1,h2,h3
h1,h2,h3 : 代表logging-handler, 用来处理日志输出的位置，同样支持多个配置，执行流程先进先出的流程，

比如说指定了h1,h2,h3 handlers同时都引用了，那么日志的输出顺序是 h1-->h2-->h3

-------


[logger_x]
handlers=h1,h2,h3
propagate # 传播，如果子handler中没有输出会默认找父类的输出
qualname # 身份辨识

作用就是引用handlers 


-------

[handler_x]
class # 指定 处理日志的处理器 ,支持自定义
level # 日志过滤级别
formatter # 指定 处理后日志输出的格式，这里是一个身份识别的上下文，
args # 处理器的所需要的参数，详情见官网

-------

[formatter_x]
class # 默认的话走原生的格式出书，支持自定义
format # 指定日志输出的格式

这里需要注意的： 如果自定义通过args传参的话，并非适配所有的参数，源码比较固定

```

