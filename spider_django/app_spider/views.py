
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from  django.forms import Form
from django import forms
from time import sleep
import re,json
import math,pymysql

# Create your views here.
'''
1:那种职位的人需求最多
2:那种职位的工资相对比较最高
3：那种工作的待遇最好
4：对学历和经验的要求
6：工作地点
'''
def find(request):
    con=pymysql.connect(host='127.0.0.1', port=3306, db='tang2', user='root', password='root',
                    charset='utf8')
    link=con.cursor(pymysql.cursors.DictCursor)
    #1工作类型的工作数量=========================================
    s1,s2=[],[]
    coun=link.execute('select id from job_type')
    for i in range(2,coun+2):
        sql='select (job_msg.id) from job_msg where type_id=%s'
        num = (link.execute(sql, (i,)))
        s1.append(num)
    link.execute('select type_name from job_type')
    name=link.fetchall()
    for i in name:
        s2.append(i['type_name'][2:4])
    # print(s2,s1)
    return render(request, 'type_num1.html', {'s1': s1, 's2': s2})
#2工资情况=====================================
def find2(request):
    con = pymysql.connect(host='127.0.0.1', port=3306, db='tang2', user='root', password='root',
                              charset='utf8')
    link = con.cursor(pymysql.cursors.DictCursor)
    s1=[2,3,4,20,27,40,49]
    salary=[]
    for i in s1:
        sql = 'select max(job_salary),min(job_salary),job_name from job_msg where job_salary!="薪资面议" and job_salary!="培训" and type_id=%s'
        link.execute(sql,i)
        ll=link.fetchall()
        salary+=ll
    lists1,lists2,lists3=[],[],['销售','计算机','教育','餐饮','房产','电子电气','保险']
    for i in salary:
            lists2+=([i['max(job_salary)'][0:4]])#工资
            lists1 += ([i['job_name']])

    return render(request, 'unique2.html', {'lists1': lists1, 'lists2': lists2, 'lists3': lists3})
#3工作待遇=================================================
def find3(request):
        con = pymysql.connect(host='127.0.0.1', port=3306, db='tang2', user='root', password='root',
                              charset='utf8')
        link = con.cursor(pymysql.cursors.DictCursor)
        sql2='select job_status from job_msg where job_status in ("五险一金","包住","年底双薪","包吃","周末双休","加班补助")'
        link.execute(sql2)
        status=link.fetchall()
        a,b,c,d,e,f=0,0,0,0,0,0
        dic,dic1,dic2,dic3,dic4,dic5= {},{},{},{},{},{}
        for i in status:
            x=i['job_status']
            if x=="五险一金":
                a+=1
                dic["name"]="五险一金"
                dic["value"] = a
            if x=="包住":
                b+=1
                dic1["name"] = "包住"
                dic1["value"] = b
            if x=="年底双薪":
                c+=1
                dic2["name"] = "年底双薪"
                dic2["value"] = c
            if x=="包吃":
                d+=1
                dic3["name"] = "包吃"
                dic3["value"] = d
            if x=="周末双休":
                e+=1
                dic4["name"] = "周末双休"
                dic4["value"] = e
            if x=="加班补助":
                f+=1
                dic5["name"] = "加班补助"
                dic5["value"] = f
        s=[dic,dic1,dic2,dic3,dic4,dic5]
        return render(request, 'status3.html', {'s': s})
#4学历和经验的要求===================================================================
def find4(request):
    con = pymysql.connect(host='127.0.0.1', port=3306, db='tang2', user='root', password='root',
                          charset='utf8')
    link = con.cursor(pymysql.cursors.DictCursor)
    sql = 'select * from job_msg'
    a = link.execute(sql)  # a是数量
    education= link.fetchall()
    a1,a2,a3,a4,b1,b2,b3,b4=0,0,0,0,0,0,0,0
    c1, c2, c3, c4, d1, d2, d3, d4,e1,e2,e3,e4 = 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0
    l1, l2,l3,l4,names= [], [],[],[],[]
    names=['销售','计算机','教育','餐饮','房产']
    educations=['学历不限','高中','大专','本科']
    for i in education:
        if i['type_id']==2:
            if i['job_education']=="学历不限":
                a1+=1
            if i['job_education']=="高中":
                a2+=1
            if i['job_education']=="大专":
                a3+=1
            if i['job_education']=="本科":
                a4+=1
        if i['type_id']==3:
            if i['job_education']=="学历不限":
                b1+=1
            if i['job_education']=="高中":
                b2+=1
            if i['job_education']=="大专":
                b3+=1
            if i['job_education']=="本科":
                b4+=1
        if i['type_id']==4:
            if i['job_education']=="学历不限":
                d1+=1
            if i['job_education']=="高中":
                d2+=1
            if i['job_education']=="大专":
                d3+=1
            if i['job_education']=="本科":
                d4+=1
        if i['type_id']==20:
            if i['job_education']=="学历不限":
                c1+=1
            if i['job_education']=="高中":
                c2+=1
            if i['job_education']=="大专":
                c3+=1
            if i['job_education']=="本科":
                c4+=1
        if i['type_id']==27:
            if i['job_education']=="学历不限":
                e1+=1
            if i['job_education']=="高中":
                e2+=1
            if i['job_education']=="大专":
                e3+=1
            if i['job_education']=="本科":
                e4+=1
    l1=[a1]+[b1]+[c1]+[d1]+[e1]
    l2 = [a2] + [b2] + [c2] + [d2] + [e2]
    l3 = [a3] + [b3] + [c3] + [d3] + [e3]
    l4 = [a4] + [b4] + [c4] + [d4] + [e4]
    return render(request,'education4.html',{'names':names,'educations':educations,'l1':l1,'l2':l2,'l3':l3,'l4':l4})
#5公司地点的分布====================================
def find5(request):
    con = pymysql.connect(host='127.0.0.1', port=3306, db='tang2', user='root', password='root',
                          charset='utf8')
    link = con.cursor(pymysql.cursors.DictCursor)
    s1,ss1=['%高新%','%雁塔%','%灞桥%','%长安%','%莲湖%','%未央%','%碑林%'],['高新','雁塔','灞桥','长安','莲湖','未央','碑林']
    s2 = []
    for i in s1:
        sql = 'select * from company_msg where job_address like %s '
        s = link.execute(sql, (i,))
        s2.append(s)
    l1,l2=['name','name','name','name','name','name'],['value', 'value', 'value', 'value', 'value', 'value']
    l=[{x1:y,x2:z} for x1,y,x2,z in zip(l1,ss1,l2,s2)]#列表推导式
    return render(request,'address5.html',{'ss1':ss1,'l':l})





