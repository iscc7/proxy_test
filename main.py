from ip_text import ip_test
from new_tex import get_ip, get_text

test_URL = 'http://www.baidu.com'

with open('./ip.txt', 'w') as ip_file:
    for i in range(2):
        URL = 'http://www.kuaidaili.com/free/inha/'+str(i)
        html = get_text(url=URL)
        ip_list = get_ip(html)
        IP = ip_test(test_url=URL, ip_list=ip_list, timeout=0.1)
        for sub_ip in IP:
            ip_file.write(sub_ip+'\n')
