#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from argparse import ArgumentParser
import subprocess
import requests
from bs4 import BeautifulSoup

def get_option():
    argparser = ArgumentParser()
    argparser.add_argument('-u', '--url', type=str, default='none',
                            help='ダウンロードするコンテストのURLを指定します')
    return argparser.parse_args()

def main():
    args = get_option()
    url = args.url
    if (url == 'none'):
        url = 'https://atcoder.jp/contests/' + os.getcwd().split('/')[-1].lower() + '/tasks'

    r = requests.get(url)
     
    soup = BeautifulSoup(r.content, "html.parser")
    link_list = []
    for td in soup.find_all('td'):
        soup = BeautifulSoup(str(td), "html.parser")
        for td_a in soup.find_all('a'):
            link = td_a.get('href')
            link_list.append('https://atcoder.jp' + link)
    links = sorted(set(link_list), key=link_list.index)

    for i in range(len(links)):
        directory = './'+chr(ord('A')+i)
        res = subprocess.run(['oj', 'download', links[i]], cwd=directory)

if  __name__ == '__main__':
    main()
