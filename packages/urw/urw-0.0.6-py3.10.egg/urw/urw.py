#!/usr/bin/python

import os
import sys
from argparse import ArgumentParser
import requests as r
import random


def random_words(number_of_words):
    exe_path = os.path.dirname(__file__)
    f = open('{}/wordlist.txt'.format(exe_path), 'r', encoding='utf-16')
    lines = f.readlines()

    random_res = ''
    while number_of_words > 0:
        random_res += random.choice(lines).strip() + ' '
        number_of_words = number_of_words - 1
        
    return random_res.strip()

if __name__ == '__main__':
    cmd_line = ArgumentParser(description='Random Urdu words and phrases generator.')
    cmd_line.add_argument('-n', '--number_of_words', metavar='N', type=int, help='Number of words to generate for the complete output.')
    args = cmd_line.parse_args()

    ans = ''
    if args.number_of_words:
        ans = random_words(args.number_of_words)


    print('\033[1mRESULT\033[0m {}'.format(ans))
