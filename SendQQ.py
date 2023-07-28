# -*- coding:utf-8 -*-
"""
Author：jones
Time: 2022/12/12
Software: PyCharm
"""
# 该例程仅供学习使用

# 使用psutil来判断QQ是否登录
from string import Template

import psutil,time,os
import pyperclip
import scshot
import pyautogui as gui
import time

gui.PAUSE = 1

people = 'Life'	# 好友全称
note = '冰雪村，速来！！ '	# 发送的消息
ntime = (time.strftime('%H:%M:%S',time.localtime(time.time())))
message = "%s%s"%(note,ntime)


QQ_dir = r'D:\QQ\Bin\QQ.exe'	# QQ路径

# 判断QQ是否登录
def proc_exist(process_name):
    pl = psutil.pids()
    for pid in pl:  # 通过PID判断
        if psutil.Process(pid).name() == process_name:
            return isinstance(pid,int)

# 发送消息
def send_msg(people, msg):
    if proc_exist('QQ.exe'):
        # 打开QQ主界面
        # 通过图片匹配qq图标
        time.sleep(1)    # 等待 1 秒
        left, top, width, height = gui.locateOnScreen('G:\Python\Projects\Auto_notice\moudle\qq.jpg')   # 寻找 模板图片；
        center = gui.center((left, top, width, height))    # 寻找 图片的中心
        gui.click(center)
        #gui.moveTo(1673, 1054, duration=0.2)
        #gui.moveTo(1673, 1054, duration=0.2)
        #gui.click()
        time.sleep(0.5)
    else:
        # 登录QQ
        QQ_login()

    # 搜索好友并打开聊天窗口
    gui.moveTo(1590, 195, duration=0.2)
    gui.click()
    time.sleep(0.5)
    #复制好友名称，发送
    pyperclip.copy(people)
    gui.hotkey('ctrl', 'v')
    time.sleep(1)
    gui.hotkey('Enter')
    time.sleep(1)

    # 输入需要发送的信息
    gui.moveTo(600, 850, duration=0.2)
    gui.click()
    pyperclip.copy(msg)
    gui.hotkey('ctrl', 'v')
    # 发送截图
    scshot.screenshot()
    gui.hotkey('ctrl', 'v')
    gui.hotkey('Enter')

    # 隐藏主界面并退出聊天界面
    #gui.moveTo(1850, 150, duration=0.5)
    #gui.click()
    gui.hotkey('Esc')
    time.sleep(1)
    gui.hotkey('alt', 'z')

# 登录QQ
def QQ_login():
    os.startfile(QQ_dir)
    print('正在打开QQ')
    time.sleep(3)
    gui.moveTo(960, 695, duration=0.5)
    gui.click()
    time.sleep(10)

if __name__ == "__main__":
    send_msg(people,message)

# 查看鼠标位置
# while True:
#     last_position=gui.position()
#     if last_position!=gui.position():
#         print(gui.position())
