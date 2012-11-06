#!/usr/bin/env python
#coding=utf-8


from ktouch import read_ktouch_csv,convert





# 读三个文件
outbox_buffer=read_ktouch_csv('outbox.csv')
outbox_result=convert(outbox_buffer,'deliver')

inbox_buffer=read_ktouch_csv('inbox.csv')
inbox_result=convert(inbox_buffer,'submit')

draft_buffer=read_ktouch_csv('draft.csv')
draft_result=convert(draft_buffer)

file_to_write=open('message_for_wandoujia.csv','w')
for line in (outbox_result+inbox_result+draft_result):
    file_to_write.write(line+'\n')




