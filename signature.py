from tkinter import *
import requests
import tkinter.messagebox  # 对话框模块，弹出对话框框
from PIL import ImageTk  # 下载包 或pycharm中安装pillow
from bs4 import BeautifulSoup as bs  # 用css选择器

root = Tk()  # 创建窗口
root.wm_title('签名设计')  # 主标题
# 窗口大小为600x300,中间为小写x，
# 两组加号分别为窗口左上角的横纵坐标（打开窗口时窗口出现的位置
root.geometry('600x300')  # 生成的窗口大小


# 可以获取屏幕分辨率按比例显示窗口位置
# wid = root.winfo_screenwidth()
# hei = root.winfo_screenheight()
# print(wid, hei)
# root.geometry('600x300+{}+{}'.format(wid//3, hei//3))

def download():
    '''
    这里要用一点爬虫的知识,用css选择器获取签名后的图片
    可以了解一下
    :return:
    '''
    name = entry.get()  # 获取输入的名字
    name = name.strip()  # 去掉名字前后的空格
    if name == '':
        tkinter.messagebox.showinfo('请输入名字')  # messagebox.showinfo()弹出提示框
    else:
        data = {
            'word': name,
            'sizes': 60,
            'fonts': 'jfcs.ttf',
            # 'fontcolor': '#000000',
        }
        url = 'http://www.uustv.com/'
        try:
            # 获取html
            result = requests.post(url=url, data=data)
            result.encoding = 'utf8' # 吧源码的格式转为utf8
            html = result.text
            soup = bs(html, 'lxml') # 使用bs4中的css选择器
            image = soup.select('div.tu img')[0].attrs['src'] # 获取签名图片
            imgurl = url + image # 然后把图片链接补全
            response = requests.get(imgurl).content
            with open('{}.gif'.format(name), 'wb') as f: # 下载图片
                f.write(response)
            print('下载图片成功!!!')
            # 显示图片
            bm = ImageTk.PhotoImage(file='{}.gif'.format(name))
            label2 = Label(root, image=bm)
            label2.bm = bm
            label2.grid(row=3, columnspan=2)
        except Exception as e:
            print('错误信息{}'.format(e))


label = Label(root, text='名字', font='华文行楷, 20', fg='blue')  # 设置标签
label.grid(row=0, column=0)  # 标签位置
# 输入姓名的输入框
entry = Entry(root, font='华文行楷, 20')  # 输入窗口
entry.grid(row=0, column=1)  # 窗口位置

button = Button(root, text='开始设计签名', font='华文行楷, 20', fg='red', command=download)  # 生成一个按钮
button.grid(row=1, column=0)  # 按钮位置

def on_closing():
    if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()  # 主循环
