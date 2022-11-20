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
    file.write("日志开始记录:\t{}\n{}\n\n".format(times(), loggingMessage))
    file.close()


# 克隆指定文件
def clone():
    os.system("git clone https://github.com/steam-404/411message6.0-for-production-environment")
    return "克隆文件"


# 递归删除文件及其子文件
def delete_file(message):
    pass


def say(sayMessage):
    pyttsx3.speak(sayMessage)
    # sayMessage = pyttsx3.init()
    # sayMessage.say("{}".format(message))
    # message.runAndWait()


say("当前仓库url:github.com steam-404 411message6.0 for production environment.git 当前映射域名:4 1 1 点 f r e e.s v i p s s 点top")

nowTime = pyttsx3.init()
# 语音初始化
nowTime.say(times())
# 内容播放
nowTime.runAndWait()
# 等待播放内容
print(times())

say("线程已开启")
say("正在检查旧仓库是否存在")
# 判断文件是否存在
fileMessage = os.path.exists("411message6.0-for-production-environment")

say("旧文件仓库,已存在")
# 如果文件夹存在则删除，在克隆
if fileMessage:
    # 语音播报
    say("{}\t正在删除".format(time))
    message2sound()
    delete_file("temporaryFile/411message6.0-for-production-environment")
    say("{}\t旧文件删除成功".format(times()))
    message1sound()
# 如果文件不存在则直接克隆
elif not fileMessage:
    say("正在克隆新仓库")
    # 判断是否克隆成功,继续克隆直到成功
    cloneMessage = True
    say("新仓库克隆成功")
    say("线程已关闭")
    while cloneMessage:
        clone()
        fileMessage = os.path.exists("411message6.0-for-production-environment")
        if fileMessage:
            loggingMessage += "{}\t克隆失败正在重新克隆".format(times())
            cloneMessage = False
        else:
            pass

else:
    loggingMessage += logging

# loggingWrite(loggingMessage)
# 写入日志信息
