# 2019 淘宝双十一合伙人猫铺

## 使用说明

> 由于本人常用iphone手机，只有一台备用安卓，故我适配的屏幕是1080p。
> 脚本比较简单，可以看着代码修改坐标。
> 因为懒得重新登录，我在安卓手机登录的是天猫，故适配了天猫农场（淘宝没有，直接注释掉就可以了）。

请先在电脑安装python3，并配置好adb

请打开淘宝，进入领猫币中心。

<img src="./img/WechatIMG6.jpeg" width="375"/>

将手机连接电脑，打开开发者模式，并允许usb调试。


### 本项目采用 pipenv 管理 第三方库

没有装过 pipenv，请在项目根目录执行

```
➜ pip install pipenv
➜ pipenv install
```

开始运行程序

```
➜ cd nfu 
➜ pipenv run python main.py
```