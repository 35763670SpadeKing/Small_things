#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：jones
import SendQQ
import time
import pyautogui
from PIL import Image, ImageGrab
from io import BytesIO
import win32clipboard
pyautogui.PAUSE = 1

def send_msg_to_clip(type_data, msg):
    """
    操作剪贴板分四步：
    1. 打开剪贴板：OpenClipboard()
    2. 清空剪贴板，新的数据才好写进去：EmptyClipboard()
    3. 往剪贴板写入数据：SetClipboardData()
    4. 关闭剪贴板：CloseClipboard()

    :param type_data: 数据的格式，
    unicode字符通常是传 win32con.CF_UNICODETEXT
    :param msg: 要写入剪贴板的数据
    """
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(type_data, msg)
    win32clipboard.CloseClipboard()
def screenshot():
    #选定区域截图
    img_name = 'H:\剑灵/test.png'
    img = ImageGrab.grab((400, 110, 1200, 300))
    img.save(img_name) #截图保存位置，覆盖保存
    #img.show() #截图后显示截图
    """
    图片转换成二进制字符串，然后以位图的格式写入剪贴板
    主要思路是用Image模块打开图片，
    用BytesIO存储图片转换之后的二进制字符串

    :param file_img: 图片的路径
    """
    # 把图片写入image变量中
    # 用open函数处理后，图像对象的模式都是 RGB
    image = Image.open(img_name)

    # 声明output字节对象
    output = BytesIO()

    # 用BMP (Bitmap) 格式存储
    # 这里是位图，然后用output字节对象来存储
    image.save(output, 'BMP')

    # BMP图片有14字节的header，需要额外去除
    data = output.getvalue()[14:]
    # 关闭
    output.close()
    # DIB: 设备无关位图(device-independent bitmap)，名如其意
    # BMP的图片有时也会以.DIB和.RLE作扩展名
    # 设置好剪贴板的数据格式，再传入对应格式的数据，才能正确向剪贴板写入数据
    send_msg_to_clip(win32clipboard.CF_DIB, data)

if __name__ == "__main__":
    screenshot()
