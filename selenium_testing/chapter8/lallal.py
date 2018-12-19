# -*- coding: utf-8 -*-
# @Time       : 2018/12/19 8:07
# @Author     : Philly
# @File       : lallal.py
# @Description: 
import csv
import xlrd


def get_data(file_name):
    # create an empty list to store rows
    rows = []
    # open the CSV file
    data_file = open(file_name, "r")
    # create a CSV Reader from CSV file
    reader = csv.reader(data_file)
    # skip the headers
    next(reader, None)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows

def get_data2(file_name):
    # create an empty list to store rows
    rows = []
    # open the specified Excel spreadsheet as workbook
    book = xlrd.open_workbook(file_name)
    # get the first sheet
    sheet = book.sheet_by_index(0)
    # iterate through the sheet and get data from rows in list
    for row_idx in range(1, sheet.nrows):
        rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
    return rows
'''
Q: xlrd.biffh.XLRDError: Unsupported format, or corrupt file: Expected BOF record; found b'Category'
A: 文件格式出现问题
'''
if __name__ == '__main__':
    # print(get_data("testdata.csv"))
    print(get_data2("333.xlsx"))
