from django.shortcuts import render, render_to_response

from django.template import loader, Context

from django.http import HttpResponse,HttpResponseRedirect

from django.template import RequestContext      #验证

from urllib.request import quote

import os

from datetime import date

from time import strftime, time

import json

from managementSystem.models import *

import managementSystem.function

import managementSystem.MyForm as MyForm

def index(request):
    if request.method == 'GET':
        return render_to_response('login_Box.html')
    elif request.method == 'POST':
        u = Admin.objects.filter(
            userName = request.POST.get('userName', ''), 
            passWord = request.POST.get('passWord', '')
        )[:1]
        if len(u) == 0:
            rul = False
            errID = 1
        elif len(u) == 1:
            rul = True
            errID = 0
        html = HttpResponse(json.dumps({
            'Success':rul, 
            'errID':errID
        }))
        if rul:
            u = u[0]
            html.set_cookie('userName', u.userName, 3600)
            html.set_cookie('nickName', quote(u.nickName), 3600)
            html.set_cookie('levelName', str(u.levelName), 3600)
            html.set_cookie('key', managementSystem.function.h_md5(u), 3600)
            
            #载入日志
            mylogs.objects.create(
                user_id = u.id, 
                time = strftime('%Y-%m-%d %H:%M'), 
                content = '登录成功'
            )
            u.loginTime = int(time())
            u.loginIP = request.META['REMOTE_ADDR']
            u.save()
        return html
        
def Console(request):
    b, u = managementSystem.function.verification_cookie(request)
    if not b:
        return HttpResponseRedirect('/')
    if request.method == 'GET':
        return render_to_response(
            'index.html', 
            Context({})
        )

def addUser(request):
    if request.method != 'POST':
        return HttpResponse()
    b, u = managementSystem.function.verification_cookie(request)
    if not b:
        return HttpResponseRedirect('/')
    if request.POST.get('type', '') == 'getForm':
        return render_to_response(
            'addUser.html', 
            Context({
                'registerForm':MyForm.RegisterForm(), 
                'question': [
                    '你的高中班主任的儿子叫你隔壁王叔叔什么？', 
                    '你第一任女朋友的现任老公身高是多少？', 
                    '你与你养的第一只宠物一起吃的食物什么？', 
                    'Are you a virgin?', 
                ]
            }))
    elif request.POST.get('type', '') == 'sendForm':
        rul = False
        try:
            Admin.objects.create(
                userName = request.POST['userName'], 
                passWord = request.POST.get('passWord', ''), 
                nickName = request.POST.get('nickName', ''), 
                question = int(request.POST.get('selectVal', '0')), 
                answer = request.POST.get('answer', ''), 
                levelName = 0, 
                checkAdmin = True, 
                loginIP = '0.0.0.0', 
                loginTime = int(time())
            )
            rul = True
        except BaseException:
            pass
        html = HttpResponse(json.dumps({
            'Success':rul, 
            'errID':0,
            'html': ''
        }))
        if rul:
            mylogs.objects.create(
                user_id = u.id, 
                time = strftime('%Y-%m-%d %H:%M'), 
                content = '添加用户[' + request.POST['nickName'] + ']'
            )
            u.loginTime = int(time())
            u.loginIP = request.META['REMOTE_ADDR']
            u.save()
        return html
def delUser(request):
    if request.method != 'POST':
        return HttpResponse()    
    b, u = managementSystem.function.verification_cookie(request)
    if not b:
        return HttpResponseRedirect('/')
    user = Admin.objects.get(id = int(request.POST.get('id', '')))
    userName = user.nickName
    user.delete()
    mylogs.objects.create(
        user_id = u.id, 
        time = strftime('%Y-%m-%d %H:%M'), 
        content = '删除用户[' + userName + ']'
    )
    u.loginTime = int(time())
    u.loginIP = request.META['REMOTE_ADDR']
    u.save()
    
    html = HttpResponse(json.dumps({
        'Success':True, 
        'errID':0,
        'html': ''
    }))
    return html
    
    
def getPage(request):
    if request.method != 'POST':
        return HttpResponse()
    b, u = managementSystem.function.verification_cookie(request)
    if not b:
        return HttpResponseRedirect('/')
    pageName = request.POST.get('getType', 'error.html')
    return render_to_response(
        pageName, 
        Context(managementSystem.function.getDict(pageName))
    )

def getExcel(request):
    if request.method != 'POST':
        return HttpResponse()
    b, u = managementSystem.function.verification_cookie(request)
    if not b:
        return HttpResponseRedirect('/')
    fileName = 'SF6 断路器（变）.xls.html'#'experimentalType\\' + request.POST.get('fileName', 'error.html') + '.html'
    print(fileName)
    return render_to_response(
        fileName
    )
    