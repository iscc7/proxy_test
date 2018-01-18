# -*- coding:utf-8 -*-
from requests import get
from re import compile


def get_text(url):
    header = {
        'Host': 'www.kuaidaili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
    }
    txt = get(url, headers=header)
    return txt.text


def get_ip(text):
    regular = compile('<td data-title="IP">([0-9]+?\.[0-9]+?\.[0-9]+?\.[0-9]+?)</td>')
    regular2 = compile('<td data-title="PORT">([0-9]+?)</td>')
    ip = regular.findall(text)
    port = regular2.findall(text)
    result = []
    for i in range(len(ip)):
        result.append(ip[i]+':'+port[i])
    return result


if __name__ == '__main__':
    URL = 'http://www.kuaidaili.com/free/inha/1/'
    html = get_text(url=URL)
    IP = get_ip(html)
    print IP, '\nip length:', len(IP)
