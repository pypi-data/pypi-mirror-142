#!/usr/bin/python

import os
import sys
from argparse import ArgumentParser
import requests as r
import random
from rwp import languages


def show_supported_languages(exe_path):
    langs = languages.get_supported_languages(exe_path)

    print()
    print('\033[4mSUPPORTED LANGUAGES\033[0m')
    for lang in langs:
        print(lang)
    print()

def random_words(exe_path, language, number_of_words):
    f = languages.get_language_pool(language, exe_path)
    lines = f.readlines()

    random_res = ''
    while number_of_words > 0:
        random_res += random.choice(lines).strip() + ' '
        number_of_words = number_of_words - 1
        
    return random_res.strip()

if __name__ == '__main__':
    exe_path = os.path.dirname(__file__)

    cmd_line = ArgumentParser(description='Random Pakistani words and phrases generator.')
    cmd_line.add_argument('-s', '--supported_languages', action='store_true', help='Show supported languages.')
    cmd_line.add_argument('-l', '--language', metavar='L', type=str, help='Pakistani language to use for the random words.')
    cmd_line.add_argument('-n', '--number_of_words', metavar='N', type=int, help='Number of words to generate for the complete output.')
    args = cmd_line.parse_args()

    ans = ''
    if args.supported_languages:
        show_supported_languages(exe_path)
        exit
    else:
        if args.number_of_words:
            if not args.language:
                raise('Please specify one of the supported languages.')

            ans = random_words(exe_path, args.language, args.number_of_words)


    print('\033[1mRESULT\033[0m {}'.format(ans))
