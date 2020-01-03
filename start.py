#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import shutil
from colorama import Fore, Back, Style

def main():
    argvs = sys.argv
    argc = len(argvs)

    check = '[' +   Fore.MAGENTA  + 'x' + Fore.RESET + ']'
    plus =  '[' + Fore.LIGHTGREEN_EX + '+' + Fore.RESET + ']'

    if argc < 1:
        print('Usege\nstart-atcoder.py contest-name')
        exit(0)
    contest_name = argvs[1]
    if os.path.exists(contest_name):
        print(check, contest_name, 'is exists')
        exit(0)
    else:
        os.mkdir(contest_name)
        print(check, contest_name, 'is created\n')

    src = '/home/akri/atelier/atcoder/download-testcase-tool/download.py'
    shutil.copyfile(src, contest_name + '/download.py')
    print(plus, 'download.py created\n')

    contest_class = contest_name[:3]
    contest_number = int(contest_name[3:])
    if contest_class == 'ABC' and contest_number >= 126:
        problem_number = 6
    elif contest_class == 'AGC':
        problem_number = 6
    else:
        problem_number = 4 

    for i in range(problem_number):
        path = contest_name+'/'+chr(ord('A')+i) # +'/main.cpp'
        if os.path.isfile(path):
            print(check, chr(ord('A')+i), 'is exists')
        else:
            os.mkdir(path)
            src = '/home/akri/.config/nvim/template/cpp/base-yatcoder.cpp'
            shutil.copyfile(src, path + '/main.cpp')
            print(plus, chr(ord('A')+i), 'created')

if __name__ == '__main__':
    main()

