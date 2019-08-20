# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 12:07:40 2019

@author: Vidya

Problem

https://code.google.com/codejam/contest/11254486/dashboard

You just made a new friend at an international puzzle conference, 
and you asked for a way to keep in touch. 
You found the following note slipped under your hotel room door the next day:

"Salutations, new friend! I have replaced every digit of my phone number 
with its spelled-out uppercase English representation 
("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", 
"EIGHT", "NINE" for the digits 0 through 9, in that order), 
and then reordered all of those letters in some way to produce a string S. 
It's up to you to use S to figure out how many digits are in my phone number 
and what those digits are, but I will tell you that my phone number 
consists of those digits in nondecreasing order. Give me a call... if you can!"

You would to like to call your friend to tell him that this is an 
obnoxious way to give someone a phone number, but you need the phone number 
to do that! What is it?

Input

The first line of the input gives the number of test cases, T. 
T test cases follow. Each consists of one line with a string S of 
uppercase English letters.

Output

For each test case, output one line containing Case #x: y, 
where x is the test case number (starting from 1) and y is a string of digits: 
the phone number.

Limits

1 ≤ T ≤ 100.
A unique answer is guaranteed to exist.
Small dataset

3 ≤ length of S ≤ 20.
Large dataset

3 ≤ length of S ≤ 2000. 

"""

from collections import Counter

# The dictionary count of each char in a number string
all_numbers_chars = [Counter(c) for c in ['ZERO', 'ONE', 'TWO', 'THREE',
                                          'FOUR', 'FIVE', 'SIX', 'SEVEN',
                                          'EIGHT', 'NINE']]
# Order of search for the numbers
order_of_search = [0, 6, 2, 8, 4, 5, 7, 1, 3, 9]

# Choose one unique char for each number
unique_chars = ['Z', 'O', 'W', 'T', 'U', 'F', 'X', 'S', 'G', 'N']


def get_digits(number):

    num_extract = []

    # Dictionary Counter for the characters in the number string given
    num_chars = Counter(list(number))

    for i in order_of_search:

        # Search (in order of search) for the unique char of that number
        # in the number string
        # For e.g - num_chars[0] - will look for 'Z' and if it is found
        # will remove all chars of ZERO using the all_numbers_chars

        while num_chars[unique_chars[i]] > 0:
            num_chars -= all_numbers_chars[i]

            num_extract.append(i)

    num_extract.sort()
    return ''.join(map(str, num_extract))


def read_numbers(input_file):
    case = 1
    with open(input_file) as f:
        # Skipped the count of test cases
        next(f)
        for line in f:
            num = line.strip()
            extracted_num = get_digits(num)
            print('Case #{0}: {1}'.format(str(case), str(extracted_num)))
            case += 1


if __name__ == '__main__':

    input_file = 'input.txt'

    read_numbers(input_file)
