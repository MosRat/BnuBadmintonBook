import json
import re

from requests_html import HTMLSession


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


s = HTMLSession()
cookies = 'ahhqv6VrCupgbgRvpq'
head = deal_arg(f'''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Cache-Control: max-age=0
Connection: keep-alive
Cookie: JSESSIONID=ahhqv6VrCupgbgRvpq
Host: cgyd.prsc.bnu.edu.cn
sec-ch-ua: "Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52''')
print('1')

res = s.get(
    'https://cgyd.prsc.bnu.edu.cn/gymsite/cacheAction.do?ms=viewBook&gymnasium_id=2&item_id=5326&time_date=2022-10-25&userType=1',
    headers=head)
print(res.status_code)
ls = re.findall(r"{id:'(\d+)',time_session:'(.*?)'*?field_name:'(.*?)'", res.text)
it = ((i, (j, k)) for i, j, k in ls)

with open('1.json', 'w', encoding='utf8') as f:
    json.dump(dict(it),f,ensure_ascii=False)
