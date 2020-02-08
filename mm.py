import requests, re
from bs4 import BeautifulSoup as bs  # 用css选择器

print('大胸妹, 小翘臀, 黑丝袜, 美腿控, 有颜值, 大杂烩')
a = ['大胸妹', '小翘臀', '黑丝袜', '美腿控', '有颜值', '大杂烩']
case = str(input('请输入你要爬取的类型:'))
if case not in a:
    print('您输入的不对!!!重新输入!!!')
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

url = 'https://www.buxiuse.com/?cid={}'.format(get_cid())
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
}
response = requests.get(url = url, headers=headers)
html = response.text
soup = bs(html, 'lxml') # 使用bs4中的css选择器
lis = soup.select('ul.thumbnails li')
for i in lis:
    img = i.select('div.thumbnail div.img_single a img')[0].attrs['src']
    name = i.select('div.thumbnail div.img_single a img')[0].attrs['title']
    response = requests.get(img).content
    with open('G:\\新建文件夹\\{}.jpg'.format(name), 'wb') as f:
        f.write(response)
    print('下载图片 ')
