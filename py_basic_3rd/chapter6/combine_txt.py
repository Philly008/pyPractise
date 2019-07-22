# -*- coding: utf-8 -*-
# @Time       : 2019/1/5 15:42
# @Author     : Philly
# @File       : combine_txt.py
# @Description: 扫描目录下的文件并拼接在一起
import os, shutil


if __name__ == '__main__':
    work_dir = r'C:\Users\hasee\Desktop\resources\shell_cookbook'
    file = open('linux_shell.sh', 'w')
    for parent, dirnames, filenames in os.walk(work_dir, followlinks=True):
        for filename in filenames:
            file_path = os.path.join(parent, filename)
            print('文件名：%s' % filename)
            print('文件完整路径：%s\n' % file_path)
            ch_file = file_path.split('\\')
            ch_file_last = ch_file[-1]
            ch_file_name = ch_file_last.split('\.')[-1]

            ch_file_names = str(ch_file[-2]) + '_' + str(ch_file_name)
            print(ch_file_names)
            file.write(ch_file_names + '\n')
            for line in open(file_path, 'r', encoding='utf-8'):
                file.writelines(line)
            file.write('\n')
    file.close()
























