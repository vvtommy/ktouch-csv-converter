#!/usr/bin/env python
#coding=utf-8

import sys
from ktouch import read_ktouch_message_csv,convert_message,

from optparse import OptionParser

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == '__main__':
    parser=OptionParser()
    # parser.set_usage('转换天宇手机的导出文件为豌豆荚格式，短信请按照收件箱、发件箱、草稿箱分别导出。')
    parser.add_option('-i','--inbox',dest=u'inbox',
        metavar='FILE',help=u'天宇手机的收件箱导出文件',default='inbox.csv')
    parser.add_option('-t','--outbox',dest=u'outbox',
        metavar='FILE',help=u'天宇手机的发件箱导出文件',default='outbox.csv')
    parser.add_option('-d','--draft',dest=u'draft',
        metavar='FILE',help=u'天宇手机的草稿箱导出文件',default='draft.csv')
    parser.add_option('-o','--output',dest=u'output',
        metavar='FILE',help=u'生成文件',default='message_for_wandoujia.csv')

    (options,args)=parser.parse_args()

    outbox_buffer=read_ktouch_message_csv(options.outbox)
    outbox_result=convert_message(outbox_buffer,'deliver')

    inbox_buffer=read_ktouch_message_csv(options.inbox)
    inbox_result=convert_message(inbox_buffer,'submit')

    draft_buffer=read_ktouch_message_csv(options.draft)
    draft_result=convert_message(draft_buffer)

    file_to_write=open(options.output,'w')
    for line in (outbox_result+inbox_result+draft_result):
        file_to_write.write(line+'\n')





