import os
import time
from pynput import mouse
from pynput import keyboard
import logging
import datetime
import calendar


os.system("color a\n"
          "生命周期开始")
# 时间判断模块
year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().isoweekday()
date=datetime.datetime.now().day
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute
second = datetime.datetime.now().second


# 获取当前时间用于记录
times="{}年" \
      "{}月" \
      "{}日" \
      "星期{}" \
      "{}时" \
      "{}秒".format(year,month,day,date,hour,minute,second) \

print(logging)
print("author:steam-404 for GitHub\n此软件完全免费,只更新于GitHub")
print("使用前请先添加环境变量\n目前仅适应win10/win11 64位系统")
os.system("wemeetapp.exe")
print("正在创建日志")
loggingMessage=open('logging.txt','a',encoding="utf-8")
loggingMessage.write("日志开始记录:{}".format(times))
print("日志创建完成")
print("正在启动腾讯会议...ing")





for i in range(5, 0):
    time.sleep(1)

print("脚本执行中,不要乱点。也不要关dos窗口")

message_mouse = mouse.Controller()
# 816,327  加入会议的坐标
message_mouse.position = (816, 327)
print("等待程序启动中")
time.sleep(5)

print("进入会议")
message_mouse.press(mouse.Button.left)
time.sleep(5)
message_mouse.release(mouse.Button.left)

# (841, 337)  会议号坐标
# message_mouse.press(mouse.Button.left)
# time.sleep(5)

# (890,860)   切换会议坐标
# message_mouse.position = (890, 853)
# message_mouse.press(mouse.Button.left,1)
# message_mouse.release(mouse.Button.left)

# 测试会议测试号腾讯会议：433-934-8941
# 解码后: 100,99,99,104,99,100,104,105,100,97

# 课表
# 软件测试 464 238 7924

# 键盘实例化
board = keyboard.Controller()

print("正在写入会议号")
while True:
    if day == 5:
        if hour == 14:
            if minute == 20:
                board.type('4642387924')

                message_mouse.position = (956, 840)
                time.sleep(3)
                message_mouse.press(mouse.Button.left)
                message_mouse.release(mouse.Button.left)
            else:
                pass
        else:
            pass
    else:
        time.sleep(30)
        print("重新进入时间判断")
        pass
print("会议号写入完成")



print("生命周期结束")
