# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 13:56:06 2020

@author: Vidya

"""

from collections import Counter


def is_anagram(word1, word2):
    c1 = Counter(word1)
    c2 = Counter(word2)

    if not (c1 - c2):
        return True
    else:
        return False


if __name__ == '__main__':

    print(is_anagram('test1', 'test2') == False)

    print(is_anagram('test1', '1test') == True)

    w1 = 'tuvwxyzabcdefghmnopqrsjkli'
    w2 = 'abcdefghijklmnopqrstuvwxyz'

    print(is_anagram(w1, w2) == True)
