# -*- coding: utf-8 -*-
# @Time       : 2019/7/25 17:34
# @Author     : Philly
# @File       : word_to_pdf.py
# @Description: 
from win32com.client import Dispatch
from os import walk

wdFormatPDF = 17


def doc2pdf(input_file):
    word = Dispatch('Word.Application')
    doc = word.Documents.Open(input_file)
    doc.SaveAs(input_file.replace(".docx", ".pdf"), FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()


if __name__ == "__main__":
    doc_files = []
    directory = "E:\\test\\"
    for root, dirs, filenames in walk(directory):
        for file in filenames:
            if file.endswith(".doc") or file.endswith(".docx"):
                doc2pdf(str(root + "\\" + file))

