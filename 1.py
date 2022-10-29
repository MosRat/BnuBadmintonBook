import time

import matplotlib.pyplot
import numpy
from requests_html import HTMLSession
s=HTMLSession()
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

code_url= "https://cgyd.prsc.bnu.edu.cn/Kaptcha.jpg"
urls="https://cgyd.prsc.bnu.edu.cn/gymbook/gymbook/gymBookAction.do?ms=saveGymBook"
hd=deal_arg('''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cache-Control: max-age=0
Connection: keep-alive
Cookie: JSESSIONID=a1Lp15b0jNG4T4nGPp
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
datas=deal_arg('''bookData.totalCost: 
bookData.book_person_zjh: 
bookData.book_person_name: 
bookData.book_person_phone: 17879539869
gymnasium_idForCache: 2
item_idForCache: 5462
time_dateForCache: 2022-10-18
userTypeNumForCache: 1
putongRes: putongRes
selectedPayWay: 1
allFieldTime: 5477%232022-10-18
companion_1: 
companion_2: 
companion_3: 
companion_4: 
companion_5: 
companion_6: 
companion_7: 
companion_8: 
companion_9: 
checkcodeuser: 15
selectPayWay: 1''')
head=deal_arg('''Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Connection: keep-alive
Content-Length: 423
Content-Type: application/x-www-form-urlencoded
Cookie: JSESSIONID=a1Lp15b0jNG4T4nGPp
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
r=s.get(code_url,headers=hd)
with open(f'{time.time()}.jpg','wb') as f:
    f.write(r.content)
    f.close()
# nr=numpy.array(r.content)
# matplotlib.pyplot.imshow(nr)
datas['checkcodeuser']=input('输入验证码：')
re=s.post(url=urls,data=datas,headers=head)
print(re.text)