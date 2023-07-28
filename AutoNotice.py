#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：jones
import SendQQ
import time
import pyautogui

pyautogui.PAUSE = 1


def notice():
    # 发送消息通知
    people = 'Life'  # 好友全称
    note = '冰雪村，速来！！ '  # 发送的消息
    ntime = (time.strftime('%H:%M:%S', time.localtime(time.time())))
    message = "%s%s" % (note, ntime)
    SendQQ.send_msg(people, message)
    print(message)
    print('发送成功！')
    time.sleep(120)


while True:
    try:
        # pyautogui.locateOnScreen("img/ai.png", region=(x, y, width, height)),可以添加region限定匹配区域
        cp1 = pyautogui.locateOnScreen('G:\Python\Projects\Auto_notice\moudle//cc.png', confidence=0.95)  # 血条
        cp3 = pyautogui.locateOnScreen('G:\Python\Projects\Auto_notice\moudle//head.jpg', confidence=0.8)  # 血条
        cp2 = pyautogui.locateOnScreen('G:\Python\Projects\Auto_notice\moudle//lingqi.png', confidence=0.9,
                                       region=(400, 110, 1200, 300))  # 灵气
        # 对比指定位置像素值，模糊比对
        # cp4 = pyautogui.pixelMatchesColor(100, 200, (255, 255, 245), tolerance=10) #tolerance参数可以指定红、绿、蓝3种颜色误差范围
        if cp1 or cp3:
            try:
                print(cp1, cp3)
                notice()  # 调用通知函数
            except Exception as e:
                # 访问异常的错误编号和详细信息
                print(e.args)
                print(str(e))
                print(repr(e))
        elif cp2:
            try:
                print('cp2')
                notice()  # 调用通知函数
            except Exception as e:
                # 访问异常的错误编号和详细信息
                print(e.args)
                print(str(e))
                print(repr(e))
        else:
            time.sleep(2)
            print('没有找到目标，继续等待中---')

    except KeyboardInterrupt:  # 处理 Ctrl-C 按键
        print('\nDone.')
    # pyautogui.scroll(-500)    # 本业没有匹配，滚动鼠标；
