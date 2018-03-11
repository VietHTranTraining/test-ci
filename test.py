#!/usr/bin/env python
"""
docstring
"""

import string

SHIFT = 3
CHOICE = raw_input("would you like to encode or decode?")
WORD = (raw_input("Please enter text"))

def do_sth():
    """
    docstring
    """
    letters = string.ascii_letters + string.punctuation + string.digits
    encoded = ''
    if CHOICE == "encode":
        for letter in WORD:
            if letter == ' ':
                encoded = encoded + ' '
            else:
                index = letters.index(letter) + SHIFT
                encoded = encoded + letters[index]
    if CHOICE == "decode":
        for letter in WORD:
            if letter == ' ':
                encoded = encoded + ' '
            else:
                index = letters.index(letter) - SHIFT
                encoded = encoded + letters[index]
    print encoded
