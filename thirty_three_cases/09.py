# -*- coding: utf-8 -*-
# @Time       : 2019/7/24 14:22
# @Author     : Philly
# @File       : 09.py
# @Description: 9 lines: Opening files
# indent your Python code to put into an email
import glob
# glob supports Unix style pathname extensions
python_files = glob.glob('*.py')
for file_name in sorted(python_files):
    print('    --------' + file_name)
    with open(file_name, encoding='utf-8') as f:
        for line in f:
            print('     ' + line.rstrip())
    print()

