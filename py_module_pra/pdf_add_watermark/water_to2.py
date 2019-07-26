# -*- coding: utf-8 -*-
# @Time       : 2019/7/25 16:49
# @Author     : Philly
# @File       : water_to.py
# @Description: 
######## 基础准备 ########
import os

print(os.getcwd())
# os.chdir('E:\\test\\')
# os.getcwd()  # 获取当前工作目录

from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from os import walk
from py_module_pra.pdf_add_watermark.word_to_pdf import doc2pdf
from datetime import datetime

pdfmetrics.registerFont(TTFont('song', 'C:/Windows/Fonts/simsun.ttc'))  # 宋体
from PyPDF2 import PdfFileWriter, PdfFileReader


######## 1.生成水印pdf的函数 ########
def create_watermark(content):
    # 默认大小为21cm*29.7cm
    c = canvas.Canvas(shuiyin_path + 'mark.pdf', pagesize=(30 * cm, 30 * cm))
    c.translate(10 * cm,
                10 * cm)  # 移动坐标原点(坐标系左下为(0,0)))
    c.setFont('song', 32)  # 设置字体为宋体，大小22号
    c.setFillColorRGB(0.5, 0.5,
                      0.5)  # 灰色
    c.rotate(45)  # 旋转45度，坐标系被旋转
    c.drawString(-7 * cm, 0 * cm, content)
    # c.drawString(7 * cm, 0 * cm, content)
    # c.drawString(0 * cm, 7 * cm, content)
    # c.drawString(0 * cm, -7 * cm, content)
    c.save()  # 关闭并保存pdf文件


######## 2.为pdf文件加水印的函数 ########
def add_watermark2pdf(input_pdf, output_pdf, watermark_pdf):
    watermark = PdfFileReader(watermark_pdf)
    watermark_page = watermark.getPage(0)
    os.chdir(docs_path)
    pdf = PdfFileReader(input_pdf, strict=False)
    pdf_writer = PdfFileWriter()
    for page in range(pdf.getNumPages()):
        pdf_page = pdf.getPage(page)
        pdf_page.mergePage(watermark_page)
        pdf_writer.addPage(pdf_page)
    pdfOutputFile = open(output_pdf, 'wb')
    # pdf_writer.encrypt('123456')  # 设置pdf密码
    pdf_writer.write(pdfOutputFile)
    pdfOutputFile.close()



if __name__ == '__main__':

    shuiyin_path = 'E:\\test\\shuiyin\\'
    create_watermark('云康集团')
    newpdfs_path = 'E:\\test\\newpdfs\\'

    doc_files = []
    docs_path = "E:\\test\\docs\\"
    s = datetime.now()
    for root, dirs, filenames in walk(docs_path):
        for file in filenames:
            if file.endswith(".doc") or file.endswith(".docx"):
                # print(file)
                doc2pdf(str(root + "\\" + file))
    e = datetime.now()


    m = e - s
    print(m)    # 100个PDF时间 0:25:21.164653

    for root, dirs, filenames in walk(docs_path):
        for file in filenames:
            if file.endswith(".pdf"):
                add_watermark2pdf(file, newpdfs_path + file, shuiyin_path + 'mark.pdf')
