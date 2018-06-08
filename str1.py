# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 09:30:20 2017

@author: Administrator
"""

from random import Random
def random_str(randomlength=10000):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str
print (random_str())
