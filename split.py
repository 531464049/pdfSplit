#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 2020-12-10
# @Author  : mh

import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import time

INPUT_FILE = "test.pdf"   # 待分割文件
OUTOUT_FILE_NAME = "split"  # 分割后的文件名
SUBFILE_PAGE_NUM = 20  # 分割页数


def subsplit(a, reader, pageCount):
    output = PdfFileWriter()
    outfile = OUTOUT_FILE_NAME + str(a) + ".pdf"  # 分割后的文件

    for ipage in range(SUBFILE_PAGE_NUM):
        kp = ipage + SUBFILE_PAGE_NUM * a
        if kp < pageCount:
            output.addPage(reader.getPage(kp))

    # 写入到目标PDF文件
    outputStream = open(outfile, "wb")
    output.write(outputStream)
    outputStream.close()


def split():
    reader = PdfFileReader(open(INPUT_FILE, "rb"))
    pageCount = reader.getNumPages()

    subFileNum = (int)(pageCount / SUBFILE_PAGE_NUM)
    if pageCount % SUBFILE_PAGE_NUM > 0:
        subFileNum += 1

    for k in range(subFileNum):
        subsplit(k, reader, pageCount)


if __name__ == '__main__':
    time1 = time.time()
    split()
    time2 = time.time()
    print('time consumed %s s.' % (time2 - time1))
