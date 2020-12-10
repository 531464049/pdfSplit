#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 2020-12-10
# @Author  : mh

import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import time

SUBFILEPAGE = 20  # 分割页数


def subsplit(a, reader, pageCount):
    output = PdfFileWriter()
    outfile = "split" + str(a) + ".pdf"  # 分割后的文件

    for ipage in range(SUBFILEPAGE):
        kp = ipage + SUBFILEPAGE * a
        if kp < pageCount:
            output.addPage(reader.getPage(kp))

    # 写入到目标PDF文件
    outputStream = open(outfile, "wb")
    output.write(outputStream)
    outputStream.close()


def split():
    pdf_file = "test.pdf"  # 原始文件
    reader = PdfFileReader(open(pdf_file, "rb"))
    pageCount = reader.getNumPages()

    subFileNum = (int)(pageCount / SUBFILEPAGE)
    if pageCount % SUBFILEPAGE > 0:
        subFileNum += 1

    for k in range(subFileNum):
        subsplit(k, reader, pageCount)


if __name__ == '__main__':
    time1 = time.time()
    split()
    time2 = time.time()
    print('time consumed %s s.' % (time2 - time1))
