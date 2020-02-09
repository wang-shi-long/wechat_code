import requests
from requests.exceptions import RequestException
import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup as bs
import bs4
from tkinter import *
from tkinter.filedialog import askdirectory
import os
root = tk.Tk()
root.title('crawler pics')
class DB():
    def __init__(self):
        self.lab1 = tk.Label(root, text="目标路径:")
        self.lab2 = tk.Label(root, text="选择分类:")
        self.lab3 = tk.Label(root, text="爬取页数:")
        self.menu = ttk.Combobox(root, width=6, state='readonly')
        self.menu['value'] = ('大胸妹', '小翘臀', '黑丝袜', '美腿控', '有颜值', '大杂烩')
        self.menu.current(0)
        self.page = tk.Entry(root, width=5)
        self.path = StringVar()
        self.input = tk.Entry(root, textvariable=self.path, width=80)  # 创建一个输入框,显示图片存放路径
        self.info = tk.Text(root, height=20)  # 创建一个文本展示框，并设置尺寸
        # 添加一个按钮，用于选择图片保存路径
        self.t_button = tk.Button(root, text='选择路径', relief=tk.RAISED, width=8, height=1,
                                  command=self.select_Path)
        # 添加一个按钮，用于触发爬取功能
        self.t_button1 = tk.Button(root, text='爬取', relief=tk.RAISED, width=8, height=1, command=self.download)
        # 添加一个按钮，用于触发清空输出框功能
        self.c_button2 = tk.Button(root, text='清空输出', relief=tk.RAISED, width=8, height=1, command=self.cle)
    def gui_arrang(self):
        """完成页面元素布局，设置各部件的位置"""
        self.lab1.grid(row=0, column=0)
        self.lab2.grid(row=1, column=0)
        self.lab3.grid(row=2, column=0)
        self.menu.grid(row=1, column=1, sticky=W)
        self.page.grid(row=2, column=1, sticky=W)
        self.input.grid(row=0, column=1)
        self.info.grid(row=3, rowspan=5, column=0, columnspan=3, padx=15, pady=15)
        self.t_button.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
        self.t_button1.grid(row=1, column=2)
        self.c_button2.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)
    def download(self):
        # a = ['大胸妹', '小翘臀', '黑丝袜', '美腿控', '有颜值', '大杂烩']
        try:
            for i in range(1, int(self.page.get()) + 1):
                case = self.menu.get()
                print('下载第{}页'.format(i))
                print('================{}'.format(case))
                category = {
                    'DXM': 2,
                    'XQT': 6,
                    'HSW': 7,
                    'MTK': 3,
                    'YYZ': 4,
                    'DZH': 5
                }

                def get_cid():
                    cid = None
                    if case == '大胸妹':
                        cid = category['DXM']
                    elif case == '小翘臀':
                        cid = category['XQT']
                    elif case == '黑丝袜':
                        cid = category['HSW']
                    elif case == '美腿控':
                        cid = category['MTK']
                    elif case == '有颜值':
                        cid = category['YYZ']
                    elif case == '大杂烩':
                        cid = category['DZH']
                    return cid

                url = 'https://www.buxiuse.com/?cid={}&page={}'.format(get_cid(), i)
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
                }
                response = requests.get(url=url, headers=headers)
                html = response.text
                soup = bs(html, 'lxml')  # 使用bs4中的css选择器
                lis = soup.select('ul.thumbnails li')
                for i in lis:
                    img = i.select('div.thumbnail div.img_single a img')[0].attrs['src']
                    name = i.select('div.thumbnail div.img_single a img')[0].attrs['title']
                    response = requests.get(img).content
                    img_url = self.input.get()
                    self.info.insert('end', "正在下载:" + name + '\n')
                    # os.mkdir(img_url+'/'+case)
                    with open('{}//{}.jpg'.format(img_url, name), 'wb') as f:
                        f.write(response)
                    print('下载成功 ')
        except Exception as e:
            print(e)
    def select_Path(self):
        """选取本地路径"""
        path_ = askdirectory()
        self.path.set(path_)
    def cle(self):
        """定义一个函数，用于清空输出框的内容"""
        self.info.delete(1.0,"end")  # 从第一行清除到最后一行
if __name__ == '__main__':
    t = DB()
    t.gui_arrang()
    tk.mainloop()
