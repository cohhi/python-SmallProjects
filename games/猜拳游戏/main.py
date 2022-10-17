import random

win = 0  # 获胜次数
count = 0  # 游玩次数

while True:
    print("============================================================================")
    print("获胜次数:{}\t局数{}\t平局不计算次数".format(win,count))
    if count == 3:
        print("游戏结束")
        print("局数用完")
        if win >= 2:
            print("你赢了")
        break
    elif count == 3 and win == 2:
        print("游戏结束你赢了")
        break
    count += 1
    ranNum = random.randint(1, 3)
    userChoose = int(input("请猜拳\t1.石头\t2.剪刀\t3.布\n"))
    print("电脑出了{}".format(ranNum))
    if userChoose == 1:
        if ranNum == 1:
            print("平局")
            count -= 1
        elif ranNum == 2:
            print("你赢了")
            win += 1
        elif ranNum == 3:
            print("你输了")
    elif userChoose == 2:
        if ranNum == 1:
            print("你输了")
        elif ranNum == 2:  # 如果平局就给循环体变量-1
            print("平局")
            count -= 1
        elif ranNum == 3:
            win += 1
            print("你赢了")
    elif userChoose == 3:
        if ranNum == 1:
            win += 1
            print("你赢了")
        elif ranNum == 2:
            print("你输了")
        elif ranNum == 3:  # 如果平局就给循环体变量-1
            print("平局")
            count -= 1
