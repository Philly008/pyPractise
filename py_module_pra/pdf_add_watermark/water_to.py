# -*- coding: utf-8 -*-
# @Time       : 2019/7/25 16:49
# @Author     : Philly
# @File       : water_to.py
# @Description: 
######## 基础准备 ########
import os

os.getcwd()
os.chdir('E:\\test\\pdf批量加水印\\')
os.getcwd()  # 获取当前工作目录

from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('song', 'C:/Windows/Fonts/simsun.ttc'))  # 宋体
from PyPDF2 import PdfFileWriter, PdfFileReader
import xlrd


######## 1.生成水印pdf的函数 ########
def create_watermark(content):
    # 默认大小为21cm*29.7cm
    c = canvas.Canvas('mark.pdf', pagesize=(30 * cm, 30 * cm))
    c.translate(10 * cm,
                10 * cm)  # 移动坐标原点(坐标系左下为(0,0)))
    c.setFont('song', 22)  # 设置字体为宋体，大小22号
    c.setFillColorRGB(0.5, 0.5,
                      0.5)  # 灰色
    c.rotate(45)  # 旋转45度，坐标系被旋转
    c.drawString(-7 * cm, 0 * cm, content)
    c.drawString(7 * cm, 0 * cm, content)
    c.drawString(0 * cm, 7 * cm, content)
    c.drawString(0 * cm, -7 * cm, content)
    c.save()  # 关闭并保存pdf文件


######## 2.为pdf文件加水印的函数 ########
def add_watermark2pdf(input_pdf, output_pdf, watermark_pdf):
    watermark = PdfFileReader(watermark_pdf)
    watermark_page = watermark.getPage(0)
    pdf = PdfFileReader(input_pdf, strict=False)
    pdf_writer = PdfFileWriter()
    for page in range(pdf.getNumPages()):
        pdf_page = pdf.getPage(page)
        pdf_page.mergePage(watermark_page)
        pdf_writer.addPage(pdf_page)
    pdfOutputFile = open(output_pdf, 'wb')
    pdf_writer.encrypt('123456')  # 设置pdf密码
    pdf_writer.write(pdfOutputFile)
    pdfOutputFile.close()


######## 3.导入excel：325家投放商家明细10.30 ########
ExcelFile = xlrd.open_workbook('E:\\test\\商家名单.xlsx')
sheet = ExcelFile.sheet_by_name('Sheet1')  # 打开有商家名单那个sheet
print('———————已导入商家名单———————')
col = sheet.col_values(3)  # 第4列内容为商家名称
id = sheet.col_values(0)  # 第1列内容为ID
del col[0]
del id[0]  # 去掉标题
id2 = [str(int(i)) for i in id]
merchant_as_mark_content = [(i + '  ') * 4 if len(i) <= 5 else i for i in col]  # 如果名称太短则重复4个为一行

######## 4.调用前面的函数制作商家水印pdf ########
if __name__ == '__main__':
    for i, j, k in zip(merchant_as_mark_content, merchant_as_mark_content, id2):  # i制作水印，j文件名，k对应ID
        create_watermark(i)  # 创造了一个水印pdf：mark.pdf
        add_watermark2pdf('新建 Microsoft Word 文档.pdf', k + '通知(' + j + ').pdf', 'mark.pdf')
        print('———————已制作好第' + k + '个pdf，正在准备下一个———————')
    print('———————所有文件已转化完毕———————')

