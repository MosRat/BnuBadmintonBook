import asyncio
import json
import time

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from requests_html import HTMLSession, AsyncHTMLSession

s = HTMLSession()
sa = AsyncHTMLSession()


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

with open('1.json','r' ,encoding='utf8') as f:
    dt = json.load(f)



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
    cook = input("请输入cookie：")
    if cook:
        cookies = cook
    hd = deal_arg(f'''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cache-Control: max-age=0
Connection: keep-alive
Cookie: JSESSIONID={cookies}
Host: cgyd.prsc.bnu.edu.cn
sec-ch-ua: "Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47''')

    data = f'''bookData.totalCost: 
bookData.book_person_zjh: 
bookData.book_person_name: 
bookData.book_person_phone: 17879539869
gymnasium_idForCache: 2
item_idForCache: 5326
time_dateForCache: 2022-10-21
userTypeNumForCache: 1
putongRes: putongRes
selectedPayWay: 1
allFieldTime: 5477#2022-10-21
companion_1: 
companion_2: 
companion_3: 
companion_4: 
companion_5: 
companion_6: 
companion_7: 
companion_8: 
companion_9: 
checkcodeuser: 55
selectPayWay: 1'''
    head = deal_arg(f'''Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Connection: keep-alive
Content-Length: 423
Content-Type: application/x-www-form-urlencoded
Cookie: JSESSIONID={cookies}
Host: cgyd.prsc.bnu.edu.cn
Origin: https://cgyd.prsc.bnu.edu.cn
Referer: https://cgyd.prsc.bnu.edu.cn/gymbook/gymBookAction.do?ms=viewGymBook&gymnasium_id=2&item_id=&time_date=&userType=
sec-ch-ua: "Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47
X-Requested-With: XMLHttpRequest''')
    datas = deal_arg(data)
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
