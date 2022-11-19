"""
author:steam-404 for GitHub
由于我的网站每天都有新内容,所以写了个自动脚本。
这是一个用于自动拉取GitHub仓库并自动部署的脚本

拉取github代码,强制拉取并覆盖本地文件
仓库地址: https://github.com/steam-404/411message6.0-for-production-environment.git
"""
from datetime import datetime

import winsound
# 蜂鸣器模块
import logging
# 日志模块
import time
# 时间模块
import os
# os处理模块
import sys
# 终端处理模块
import pyttsx3
# 语言模块
import time
import datetime

# 时间模块

logging = str(logging)

loggingMessage = logging


# 日志信息

# 蜂鸣器提示音    持续一秒
def message1sound():
    winsound.Beep(2000, 1000)


# 蜂鸣器警告音    持续三秒,重复三次
def message2sound():
    for i in range(3):
        winsound.Beep(1000, 1000)


# 获取当前事件用于日志记录
def times():
    result = ''
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day

    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    return "{}年{}月{}日{}时{}分{}秒".format(year, month, day, hour, minute, second)


# 日志写入
def loggingWrite(message):
    file = open("logging.txt", "a")
    file.write("日志开始记录:\t{}\n{}\n\n".format(times(),loggingMessage))
    file.close()


# message = pyttsx3.init()
# msg = "当前仓库url:github.com steam-404 411message6.0 for production environment.git"
# msg += "当前映射域名:4 1 1 点 f r e e.s v i p s s 点 t o p"
# message.say(msg)
# message.runAndWait()

# nowTime = pyttsx3.init()
# 语音初始化
# nowTime.say(times())
# 内容播放
# nowTime.runAndWait()
# 等待播放内容
# print(times())

loggingWrite(loggingMessage)
# 写入日志信息
