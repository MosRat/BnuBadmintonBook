import asyncio
import json
import time

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from requests_html import HTMLSession, AsyncHTMLSession

s = HTMLSession()
sa = AsyncHTMLSession()
ids={
  "5877": [
    "18:00-19:00',",
    "羽1"
  ],
  "5927": [
    "18:00-19:00',",
    "羽2"
  ],
  "5977": [
    "18:00-19:00',",
    "羽3"
  ],
  "6027": [
    "18:00-19:00',",
    "羽4"
  ],
  "35406": [
    "18:00-19:00',",
    "羽5"
  ],
  "35456": [
    "18:00-19:00',",
    "羽6"
  ],
  "35506": [
    "18:00-19:00',",
    "羽7"
  ],
  "35556": [
    "18:00-19:00',",
    "羽8"
  ],
  "50399": [
    "18:00-19:00',",
    "小综合1"
  ],
  "50449": [
    "18:00-19:00',",
    "小综合2"
  ],
  "50499": [
    "18:00-19:00',",
    "小综合3"
  ],
  "50549": [
    "18:00-19:00',",
    "小综合4"
  ],
  "737974": [
    "18:00-19:00',",
    "二层东"
  ],
  "738025": [
    "18:00-19:00',",
    "二层西"
  ],
  "5875": [
    "19:00-20:00',",
    "羽1"
  ],
  "5925": [
    "19:00-20:00',",
    "羽2"
  ],
  "5975": [
    "19:00-20:00',",
    "羽3"
  ],
  "6025": [
    "19:00-20:00',",
    "羽4"
  ],
  "35404": [
    "19:00-20:00',",
    "羽5"
  ],
  "35454": [
    "19:00-20:00',",
    "羽6"
  ],
  "35504": [
    "19:00-20:00',",
    "羽7"
  ],
  "35554": [
    "19:00-20:00',",
    "羽8"
  ],
  "50397": [
    "19:00-20:00',",
    "小综合1"
  ],
  "50447": [
    "19:00-20:00',",
    "小综合2"
  ],
  "50497": [
    "19:00-20:00',",
    "小综合3"
  ],
  "50547": [
    "19:00-20:00',",
    "小综合4"
  ],
  "737972": [
    "19:00-20:00',",
    "二层东"
  ],
  "738023": [
    "19:00-20:00',",
    "二层西"
  ],
  "5873": [
    "20:00-21:00',",
    "羽1"
  ],
  "5923": [
    "20:00-21:00',",
    "羽2"
  ],
  "5973": [
    "20:00-21:00',",
    "羽3"
  ],
  "6023": [
    "20:00-21:00',",
    "羽4"
  ],
  "35402": [
    "20:00-21:00',",
    "羽5"
  ],
  "35452": [
    "20:00-21:00',",
    "羽6"
  ],
  "35502": [
    "20:00-21:00',",
    "羽7"
  ],
  "35552": [
    "20:00-21:00',",
    "羽8"
  ],
  "50395": [
    "20:00-21:00',",
    "小综合1"
  ],
  "50445": [
    "20:00-21:00',",
    "小综合2"
  ],
  "50495": [
    "20:00-21:00',",
    "小综合3"
  ],
  "50545": [
    "20:00-21:00',",
    "小综合4"
  ],
  "737970": [
    "20:00-21:00',",
    "二层东"
  ],
  "738021": [
    "20:00-21:00',",
    "二层西"
  ],
  "5871": [
    "21:00-22:00',",
    "羽1"
  ],
  "5921": [
    "21:00-22:00',",
    "羽2"
  ],
  "5971": [
    "21:00-22:00',",
    "羽3"
  ],
  "6021": [
    "21:00-22:00',",
    "羽4"
  ],
  "35400": [
    "21:00-22:00',",
    "羽5"
  ],
  "35450": [
    "21:00-22:00',",
    "羽6"
  ],
  "35500": [
    "21:00-22:00',",
    "羽7"
  ],
  "35550": [
    "21:00-22:00',",
    "羽8"
  ],
  "50393": [
    "21:00-22:00',",
    "小综合1"
  ],
  "50443": [
    "21:00-22:00',",
    "小综合2"
  ],
  "50493": [
    "21:00-22:00',",
    "小综合3"
  ],
  "50543": [
    "21:00-22:00',",
    "小综合4"
  ],
  "737968": [
    "21:00-22:00',",
    "二层东"
  ],
  "738019": [
    "21:00-22:00',",
    "二层西"
  ]
}









def last_task(func, loop_list, add_args=True, unpack_args='', **kwargs):
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    if add_args:
        if unpack_args == 'list' or any([isinstance(loop_list[0], i) for i in (tuple, list, set)]):
            tasks = [func(*i, **kwargs) for i in loop_list]
        elif unpack_args == 'dict' or isinstance(loop_list[0], dict):
            tasks = [func(**i, **kwargs) for i in loop_list]
        else:
            tasks = [func(i, **kwargs) for i in loop_list]
    else:
        tasks = [func() for _ in loop_list]
    done, _ = loop.run_until_complete(asyncio.wait(tasks))
    return [t.result() for t in done]




def deal_arg(content: str):
    """

    :param content: 处理内容
    :return: 字典格式参数
    """
    ls = content.strip().split('\n')
    for i in ls:
        if i.endswith(':'):
            i += "''"
    ls = [i.split(':', 1) for i in ls]
    for i in ls:
        i[1] = i[1][1:]
    d = dict(ls)
    return d

try:
    with open('1.json','r' ,encoding='utf8') as f:
        dt = json.load(f)
except:
    dt=ids



item = dict(pp='5462', bd='5326')
code_url = "https://cgyd.prsc.bnu.edu.cn/Kaptcha.jpg"
urls = "https://cgyd.prsc.bnu.edu.cn/gymbook/gymbook/gymBookAction.do?ms=saveGymBook"
gound_id = [5877, 5927, 6027, 35456, 35506, 35556, 5875, 5925, 5975, 6025, 35404, 35454, 35504, 5873, 5923, 5973, 6023,
            35402, 35502, 35552]
gound_id=dt.keys()
cookies = 'a5T463QpoqkeupgOwq'

def prevent_io(sematime=3):
    """
    装饰器，装饰可以接await关键字的协程函数，控制其协程最大数
    :param sematime: 最大协程量
    :return: 修饰后协程函数
    """

    sema = asyncio.Semaphore(sematime)

    def wrapper(func):
        if __name__ == '__main__':
            print(f'已为函数{func.__name__}设置了最大协程数{sematime}')

        async def x_get_source(*args, **kwargs):
            async with sema:
                res = await func(*args, **kwargs)
                return res

        return x_get_source

    return wrapper







def get_code():
    r = s.get(code_url, headers=hd)
    image_path = time.time()
    with open(f'{image_path}.jpg', 'wb') as f:
        f.write(r.content)
        f.close()
    img = Image.open(str(image_path) + '.jpg')
    plt.imshow(img)
    plt.show()


@prevent_io(4)
async def go(i, times):
    datas['time_dateForCache'] = f'2022-{times}'
    datas['allFieldTime'] = f'{i}#2022-{times}'
    re = await sa.post(url=urls, data=datas, headers=head)
    print('结果：', dt[str(i)], re.text)


def main():

















    # mode = input("输入模式，pp乓乓球，bd羽毛球：")
    times = input("时间：%M-%d：")
    # datas['item_idForCache'] = item[mode]
    get_code()
    datas['checkcodeuser'] = input('输入验证码：')
    while 1:
        loop_list = [(i, times) for i in gound_id]
        last_task(go, loop_list)
        time.sleep(1.5)


if __name__ == '__main__':
    cook=input("请输入cookie：")
    if cook :
        cookies=cook
    main()

# ls=deal_arg('''bookData.totalCost:
# bookData.book_person_zjh:
# bookData.book_person_name:
# bookData.book_person_phone: 17879539869
# gymnasium_idForCache: 2
# item_idForCache: 5326
# time_dateForCache: 2022-10-21
# userTypeNumForCache: 1
# putongRes: putongRes
# selectedPayWay: 1
# allFieldTime: 5477#2022-10-21
# companion_1:
# companion_2:
# companion_3:
# companion_4:
# companion_5:
# companion_6:
# companion_7:
# companion_8:
# companion_9:
# checkcodeuser: 84
# selectPayWay: 1''')
# for i in datas:
#     if datas[i]!=ls[i]:
#         print(datas[i],ls[i])
