# BanBrick
BanBrick 是一个超小的监控系统，可以部署在树莓派上。采用部署 Agent 主动上报的方式来工作，服务端对监控的项集中分析和告警。

## 基本概念

1. 监控项：代表逻辑上用户关心的项，存储 Agent 最新上报的数据。
2. 触发器：对监控项设置的一些条件，当监控项的变化导致了触发器条件结果产生变化时，能够发送邮件通知指定的用户。
3. 项目：项目管理着一些逻辑相关的监控项。
4. 组：组分隔了项目，限制了用户对不同项目的可见性。
5. 用户：用户分为超级管理员、管理员和普通用户，超级管理员有全局项目可见性，管理员能够登录面板管理所属组的项目，普通用户只能上报数据而不能登录面板。

## 快速开始
执行以下命令即可快速启动一个 demo 服务，请根据提示创建一个超级管理员用于登录：
```shell
$ sudo make demo-run
```

使用浏览器访问 [http://127.0.0.1:9274](http://127.0.0.1:9274) 即可登录控制面板。
注意，该命令仅为创建演示，每次执行会重新初始化数据。
如果要在树莓派中作为简单的服务启动，可以执行以下命令：
```shell
$ sudo make init
$ sudo make server-run
```

有些系统因没有安装 gettext 工具以致初始化的时候编译本地化语言文件失败，可以用以下命令安装：
```shell
$ sudo apt-get install gettext
```

安装完毕后重新初始化即可。