#!/usr/bin/env python
#coding=utf-8
# 将旧的时间转换为新的android豌豆荚导出格式的时间
# 2012/11/03 13:18:23 -> 2012.11.05 16:41,20
def convert_time(old_time):
    # print '时间:',old_time
    tmp=old_time.split(' ')
    # print '时间',tmp[1][6:]
    return tmp[0].replace('/','.')+' '+tmp[1][:5]+','+tmp[1][6:]

# 两种type:deliver|submit
def convert(lines,type=None):
    ret=[]
    # 跳过首行标志
    flag=True
    for x in lines:
        if flag:
            flag=False
            continue
        line=x.split('\t')

        if not line[0] and not line[1] and not line[2]:
            print '发生错误',x
            continue

       
        # 首先是个固定的头
        # sms,deliver,13201691692,,,2012.11.05 16:41,20,短信正文

        ret_line='sms,'+(type or 'deliver')+','

        # 然后接电话号码
        if type is 'submit':
            ret_line+=','+line[0]+',,'
        elif type is 'deliver':
            ret_line+=line[0]+',,,'
        else:
            ret_line+=',,,'
        # 接下来是时间
        ret_line+=convert_time(line[1])+','
        # 正文
        ret_line+=line[2]
        ret.append(ret_line)

    return ret

def read_ktouch_csv(file_path):
    try:
        f=open(file_path,'rb')
        file_buffer=f.read()
        f.close()
        # 定义输出结果list
        ret=[]
        # 定义引号计数器
        counter=0
        # 一行是否开始的标记
        start=False
        # 当前行的指针
        line=[]
        # 开始遍历文件，每6个双引号就是一行
        for char in file_buffer:
            # 如果一行还未开始，则一遇到双引号就是一行开始的时候了
            if start is False and char is '"':
                start=True
            # 如果一行还未开始就直接执行下一个
            if not start:
                continue
            if char is '"':
                # 如果遇到双引号，则计数器增加
                counter+=1
                if counter%6 is 0:
                    # 保存当前行到结果中
                    ret.append(''.join(line))
                    # 开始新行
                    line=[]
                    start=False
            else:
                # 如果遇到的不是双引号，那么就把字符保存到当前行中
                line.append(char)

    except IOError,e:
        print e
    return ret
