# -*- coding: utf-8 -*-
# @Time       : 2019/7/24 15:36
# @Author     : Philly
# @File       : 15.py
# @Description: 15 lines: itertools
from itertools import groupby

lines = '''
This is the 
first paragraph.

This is the second.
'''.splitlines()
# Use itertools.groupby and bool to return groups of consecutive lines that
# either have content or don't.
for has_chars, frags in groupby(lines, bool):
    if has_chars:
        print(' '.join(frags))
# PRINTS:
# This is the first paragraph.
# This is the second.


