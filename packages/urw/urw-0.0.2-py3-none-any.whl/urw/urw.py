#!/usr/bin/python

import os
import sys
import getopt
import requests as r
import random


def show_random_words(number_of_words):
    exe_path = os.path.dirname(__file__)
    f = open('{}/wordlist.txt'.format(exe_path), 'r', encoding='utf-16')
    lines = f.readlines()

    random_res = ''
    while number_of_words > 0:
        random_res += random.choice(lines).strip() + ' '
        number_of_words = number_of_words - 1
        
    return random_res.strip()

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], 'n:h',['number_of_words', 'help'])
    for o, a in opts:
        if o in ['-h', '--help']:
            show_help()
            sys.exit(0)
        elif o in ['-n', '--number_of_words']:
            ans = show_random_words(int(a))


    print('\033[1mRESULT\033[0m {}'.format(ans))
