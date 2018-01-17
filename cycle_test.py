from ip_text import ip_test


with open('./ip.txt', 'r+') as ip_text:
    ip_set = ip_text.readlines()
    test_URL = 'http://www.baidu.com'
    ip = ip_test(test_URL, ip_set)
    print ip

