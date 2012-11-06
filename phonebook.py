#!/usr/bin/env python
#coding=utf-8

import sys
from ktouch import read_ktouch_phone_book_csv,generate_icard

from optparse import OptionParser

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    parser=OptionParser()
    # parser.set_usage('转换天宇手机的导出文件为豌豆荚格式，短信请按照收件箱、发件箱、草稿箱分别导出。')
    parser.add_option('-p','--phonebook',dest=u'phonebook',
        metavar='FILE',help=u'天宇手机的收件箱导出文件',default='phonebook.csv')
    parser.add_option('-o','--output',dest=u'output',
        metavar='FILE',help=u'生成文件',default='phonebook_for_wandoujia.iCard')

    (options,args)=parser.parse_args()

    output=open(options.output,'w')
    output.write(generate_icard(read_ktouch_phone_book_csv(options.phonebook)))
    output.close()





