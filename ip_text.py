from requests import get
from new_tex import get_ip, get_text


def ip_test(test_url, ip_list, timeout):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
    }
    great_ip = []
    for item in ip_list:
        ip_proxies = {"http": item}
        try:
            get(url=test_url, headers=header, proxies=ip_proxies, timeout=timeout)
            great_ip.append(item)
        except:
            pass
    return great_ip


if __name__ == '__main__':
    URL = 'http://www.kuaidaili.com/free/inha/1/'
    text_URL = 'http://www.baidu.com'
    html = get_text(url=URL)
    ip_List = get_ip(html)
    IP = ip_test(test_url=text_URL, ip_list=ip_List, timeout=0.1)
    print IP, '\nip length:', len(IP)
    with open('./ip.txt', 'w') as text_file:
        for i in IP:
            text_file.write(i+'\n')
