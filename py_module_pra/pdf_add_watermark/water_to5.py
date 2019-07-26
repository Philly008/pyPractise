# -*- coding: utf-8 -*-
# @Time       : 2019/7/25 16:49
# @Author     : Philly
# @File       : water_to.py
# @Description: 
######## 基础准备 ########
import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime
from PyPDF2 import PdfFileWriter, PdfFileReader
from win32com.client import Dispatch
from os import walk

wdFormatPDF = 17
pdfmetrics.registerFont(TTFont('song', 'C:/Windows/Fonts/simsun.ttc'))  # 宋体


def doc2pdf(input_file):
    word = Dispatch('Word.Application')
    doc = word.Documents.Open(input_file)
    doc.SaveAs(input_file.replace(".docx", ".pdf"), FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()

######## 1.生成水印pdf的函数 ########
def create_watermark(content):
    # 默认大小为21cm*29.7cm
    c = canvas.Canvas(shuiyin_path + 'mark.pdf')
    c.translate(10 * cm,
                10 * cm)  # 移动坐标原点(坐标系左下为(0,0)))
    c.setFont('song', 32)  # 设置字体为宋体，大小22号
    c.setFillColorRGB(0.9, 0.9,
                      0.9)  # 灰色
    c.rotate(45)  # 旋转45度，坐标系被旋转
    c.drawString(-7 * cm, 0 * cm, content)
    c.drawString(7 * cm, 0 * cm, content)
    c.drawString(0 * cm, 7 * cm, content)
    c.drawString(0 * cm, -7 * cm, content)
    c.drawString(13 * cm, 7 * cm, content)
    c.drawString(0 * cm, -3 * cm, content)
    # c.drawString(0 * cm, 0 * cm, content)
    c.drawString(-5 * cm, 5 * cm, content)
    c.drawString(-3 * cm, 10 * cm, content)

    c.drawString(3 * cm, 15 * cm, content)
    c.drawString(7 * cm, 12 * cm, content)

    # c.drawString(20 * cm, 0 * cm, content)

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
    pdf_writer.encrypt(password)  # 设置pdf密码
    pdf_writer.write(pdfOutputFile)
    pdfOutputFile.close()



if __name__ == '__main__':

    cur_path = os.getcwd()
    os.chdir(cur_path)
    password = input('请输入要加密的PDF密码后按回车键：')
    if not os.path.exists('shuiyin'):
        os.mkdir('shuiyin')
    if not os.path.exists('newpdfs'):
        os.mkdir('newpdfs')
    # os.mkdir('docs')
    shuiyin_path = cur_path + '\\shuiyin\\'
    content = input('\n请输入水印内容后按回车键：')
    create_watermark(content)
    newpdfs_path = cur_path + '\\newpdfs\\'

    doc_files = []
    docs_path = cur_path + "\\docs\\"
    s = datetime.now()
    print('生成PDF中...')
    # word转换为PDF
    for root, dirs, filenames in walk(docs_path):
        for file in filenames:
            if file.endswith(".doc") or file.endswith(".docx"):
                # print(file)
                doc2pdf(str(root + "\\" + file))
    e = datetime.now()


    m = e - s
    # print(m)    # 100个PDF时间 0:25:21.164653
    print('加水印中...')
    # PDF加上水印
    for root, dirs, filenames in walk(docs_path):
        for file in filenames:
            if file.endswith(".pdf"):
                add_watermark2pdf(file, newpdfs_path + file, shuiyin_path + 'mark.pdf')

    print('OK！完成word转PDF并加上水印')
    input('\n按回车键关闭窗口')
