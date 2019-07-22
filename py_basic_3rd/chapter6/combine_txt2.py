# -*- coding: utf-8 -*-
# @Time       : 2019/1/5 15:42
# @Author     : Philly
# @File       : combine_txt.py
# @Description: 扫描目录下的文件并拼接在一起
import os
import re


if __name__ == '__main__':
    work_dir = r'C:\Users\hasee\Desktop\resources\shell_cookbook'
    file = open('linux_shell.sh', 'w')


    for parent, dirnames, filenames in os.walk(work_dir, followlinks=True):
        for filename in filenames:
            # r = '^[0-9]*'
            # res = re.search(r, filename)
            # if res:
            file_path = os.path.join(parent, filename)
            ch_file = file_path.split('\\')  # 以反斜杠分隔
            ch_file_name = ch_file[-1].split('.')[-2]   # 取出文件名称，不包括 .sql
            ch_file_names = str(ch_file[-2]) + '_' + str(ch_file_name)  # 合并章节和文件名称
            print(ch_file_names)
            print('文件名：%s' % filename)
            print('文件完整路径：%s\n' % file_path)
            file.write(ch_file_names + '\n****start****\n')
            for line in open(file_path, 'r', encoding='utf-8'):
                file.writelines(line)
            file.write('\n****end****\n\n')
    file.close()
























