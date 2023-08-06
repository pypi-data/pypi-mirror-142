#!/usr/bin/python

import os


_DATA='languages'

def get_language_pool(language, exe_path):
    if language == 'urdu': encoding = 'utf-16'
    elif language == 'sindhi': encoding = 'utf-8'

    file_path = '{}/{}/{}.txt'.format(exe_path, _DATA, language)

    if not os.path.exists(file_path):
        raise('Please make sure that the language file exists.')

    f = open(file_path, 'r', encoding=encoding)
    return f

def get_supported_languages(exe_path):
    ls = os.listdir('{}/{}'.format(exe_path, _DATA))

    languages = []
    for l in ls:
        languages.append(l.split('_')[0].capitalize())

    return languages
