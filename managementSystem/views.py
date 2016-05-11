from django.shortcuts import render_to_response

from django.template import Context

from django.http import HttpResponse,HttpResponseRedirect

from urllib.request import quote

import os

from subprocess import call

from time import strftime

import time

import json

from managementSystem.models import *

import managementSystem.function

import managementSystem.MyForm as MyForm
#   #[0-9a-fA-F]{3,6}


def index(request):
    if request.method == 'GET':
        return render_to_response('login_Box.html')
    elif request.method == 'POST':
        u = Admin.objects.filter(
          userName=request.POST.get('userName', ''),
            passWord = request.POST.get('passWord', '')
        )[:1]
        rul, errID = False, 0
        if len(u) == 0:
            rul = False
            errID = 1
        elif len(u) == 1:
            rul = True
            errID = 0
        html = HttpResponse(json.dumps({
          'Success': rul,
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
              user_id=u.id,
              time=strftime('%Y-%m-%d %H:%M'),
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
          Context({'theme':request.COOKIES.get("theme", 'pale')})
        )
    elif request.method == 'POST':
      if managementSystem.function.jurisdiction('addReport.html', u.levelName):
        uf = MyForm.importReport(request.POST, request.FILES)
        if uf.is_valid():
          fileName = os.path.splitext(request.POST['name'])[0]
          e = experimental.objects.create(  # 写入数据库
            experimentalName=fileName,
            file=uf.cleaned_data['file'],
            PeopleUpload=u,
            uploadTime=int(time())
          )
          call(['soffice', '--headless', '--convert-to', 'html', os.path.split(e.file.name)[1]],
               cwd=os.path.join(os.getcwd(), 'managementSystem/static/data/experimental/'))
          mylogs.objects.create(
            user_id=u.id,
            time=strftime('%Y-%m-%d %H:%M'),
            content='上传了实验[' + request.POST['name'] + ']'
          )
      return HttpResponse()


def upload(request):
  if request.method != 'POST':
    return HttpResponse()
  b, u = managementSystem.function.verification_cookie(request)
  if not b:
    return HttpResponseRedirect('/')
  if managementSystem.function.jurisdiction('addEquipment.html', u.levelName):
    if request.POST.get("type", "") == "getForm":
      uf = MyForm.importReport()
      return render_to_response('loadTemplate.html', {'FileForm': uf})
    else:
      uf = MyForm.importReport(request.POST, request.FILES)
      if uf.is_valid():
        e  = Equipment.objects.create(  # 写入数据库
          EquipmentName=os.path.splitext(request.POST['name'])[0],
          file=uf.cleaned_data['file'],
          PeopleUpload=u,
          uploadTime=int(time())
        )
        call(['soffice', '--headless', '--convert-to', 'html', os.path.split(e.file.name)[1]],
               cwd=os.path.join(os.getcwd(), 'managementSystem/static/data/Equipment/'))
        mylogs.objects.create(
          user_id=u.id,
          time=strftime('%Y-%m-%d %H:%M'),
          content='上传了设备文件[' + request.POST['name'] + ']'
        )
        EquipmentLogs.objects.create(
              user = u,
              equ = EquipmentType.objects.all()[0],
              content = '上传了[' + request.POST['name'] + ']'
        )
  return HttpResponse()
def uploads(request):
  if request.method != 'POST':
    return HttpResponse()
  b, u = managementSystem.function.verification_cookie(request)
  if not b:
    return HttpResponseRedirect('/')
  if managementSystem.function.jurisdiction('addReport.html', u.levelName):
    if request.POST.get("type", "") == "postForm":
      uf = MyForm.importReport(request.POST, request.FILES)
      if uf.is_valid():
        experimental.objects.create(  # 写入数据库
          experimentalName=os.path.splitext(request.POST['name'])[0],
          file=uf.cleaned_data['file'],
          PeopleUpload=u,
          uploadTime=int(time()),
        )
        mylogs.objects.create(
          user_id=u.id,
          time=strftime('%Y-%m-%d %H:%M'),
          content='上传了实验文件[' + request.POST['name'] + ']'
        )
  return HttpResponse()
def uploadForm(request):
  if request.method != 'POST':
    return HttpResponse()
  b, u = managementSystem.function.verification_cookie(request)
  if not b:
    return HttpResponseRedirect('/')
  if managementSystem.function.jurisdiction('EquipmentManage.html', u.levelName):

    if request.POST.get("type", "") == "getForm":
      uf = MyForm.UpLoadForm()
      return render_to_response('addEquipmentX.html', {'uploadForm': uf})
    elif request.POST.get("type", "") == "postForm":
      uf = MyForm.UpLoadForm(request.POST, request.FILES)
      if uf.is_valid():
        equType = EquipmentType.objects.create(
          templateName = request.POST.get("name"),
          DirectParent = int(request.POST.get("id")),
          templatePositions = uf.cleaned_data['templatePositions']
        )
        mylogs.objects.create(
          user_id=u.id,
          time=strftime('%Y-%m-%d %H:%M'),
          content='上传了设备文件[' + request.POST['name'] + ']'
        )
        EquipmentLogs.objects.create(
          user = u,
          equ = equType,
          content = "添加了节点"
        )
  return HttpResponse()


#添加用户
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
            'registerForm': MyForm.RegisterForm(),
            'question': [
              '你的高中班主任叫什么？',
              '你第一任女朋友是谁？',
              '你与你养的第一只宠物叫什么？'
            ]
            }))
    elif request.POST.get('type', '') == 'sendForm':
        Admin.objects.create(
          userName=request.POST['userName'],
          passWord=request.POST.get('passWord', ''),
          nickName=request.POST.get('nickName', ''),
          question=int(request.POST.get('selectVal', '0')),
          answer=request.POST.get('answer', ''),
          levelName=0,
          checkAdmin=True,
          loginIP='0.0.0.0',
          loginTime = int(time())
        )
        rul = True
        html = HttpResponse(json.dumps({
          'Success': rul,
          'errID':0,
          'html': ''
        }))
        if rul:
            mylogs.objects.create(
              user_id=u.id,
              time=strftime('%Y-%m-%d %H:%M'),
              content = '添加用户[' + request.POST['nickName'] + ']'
            )
            u.loginTime = int(time())
            u.loginIP = request.META['REMOTE_ADDR']
            u.save()
        return html

#删除用户
def delUser(request):
    if request.method != 'POST':
      return HttpResponse()
    b, u = managementSystem.function.verification_cookie(request)
    if not b:
        return HttpResponseRedirect('/')
    Success, errID = False, 0
    if managementSystem.function.jurisdiction('userManagement.html', u.levelName):
      user = Admin.objects.get(id=int(request.POST.get('id', '')))
      userName = user.nickName
      user.delete()
      mylogs.objects.create(
        user_id=u.id,
        time=strftime('%Y-%m-%d %H:%M'),
        content='删除用户[' + userName + ']'
      )
      u.loginTime = int(time())
      u.loginIP = request.META['REMOTE_ADDR']
      u.save()
      Success = True
    else:
      errID = 303
      Success = False
    html = HttpResponse(json.dumps({
      'Success': Success,
      'errID': errID,
      'html': ''
    }))
    return html

#删除实验
def delReport(request):
  if request.method != 'POST':
    return HttpResponse()
  b, u = managementSystem.function.verification_cookie(request)
  if not b:
    return HttpResponseRedirect('/')
  Success, errID = False, 0
  reqList = request.POST.get("id", "")
  if len(reqList) <= 0:
    errID = 400
  elif managementSystem.function.jurisdiction('delReport.html', u.levelName):
    def mydel(x):
      e = experimental.objects.get(id=int(x))
      try:
        os.remove(e.file.name)
        os.remove(e.file.name.replace('.xls', '.html'))
      except FileNotFoundError:
        pass
      mylogs.objects.create(
        user_id=u.id,
        time=strftime('%Y-%m-%d %H:%M'),
        content='删除实验[' + e.experimentalName + ']'
      )
      e.delete()

    for _id in reqList.split(','):
      if _id:
        mydel(_id)
    Success = True
  else:
    errID = 303
  html = HttpResponse(json.dumps({
    'Success': Success,
    'errID': errID,
    'html': ''
  }))
  return html

#导出实验
def outputReport(request):
  if request.method != 'POST':
    return HttpResponse()
  b, u = managementSystem.function.verification_cookie(request)
  if not b:
    return HttpResponseRedirect('/')
  Success, errID, fileName = False, 0, ''
  fileList = request.POST.get("id", "")
  if len(fileList) <= 0:
    errID = 400
  elif managementSystem.function.jurisdiction('outputReport.html', u.levelName):
    fileName = managementSystem.function.zipPack(fileList, experimental)
    mylogs.objects.create(
      user_id=u.id,
      time=strftime('%Y-%m-%d %H:%M'),
      content='导出实验包'
    )
    Success = True
  else:
    errID = 303
  html = HttpResponse(json.dumps({
    'Success': Success,
    'errID': errID,
    'html': fileName
  }))
  return html

def delEqu(request):
  if request.method != 'POST':
    return HttpResponse()
  b, u = managementSystem.function.verification_cookie(request)
  if not b:
    return HttpResponseRedirect('/')
  Success, errID = False, 0
  reqList = request.POST.get("id", "")
  if len(reqList) <= 0:
    errID = 400
  elif managementSystem.function.jurisdiction('delEquipment.html', u.levelName):
    def mydel(x):
      e = Equipment.objects.get(id=int(x))
      try:
        os.remove(e.file.name)
        os.remove(e.file.name.replace('.xls', '.html'))
      except FileNotFoundError:
        pass
      mylogs.objects.create(
        user_id=u.id,
        time=strftime('%Y-%m-%d %H:%M'),
        content='下线设备[' + e.EquipmentName + ']'
      )
      EquipmentLogs.objects.create(
        user = u,
        equ = EquipmentType.objects.all()[0],
        content = "删除了[" + e.EquipmentName + "]"
      )
      e.delete()
    for _id in reqList.split(','):
      if _id:
        mydel(_id)
    Success = True
  else:
    errID = 303
  html = HttpResponse(json.dumps({
    'Success': Success,
    'errID': errID,
    'html': ''
  }))
  return html

def outEqu(request):
  if request.method != 'POST':
    return HttpResponse()
  b, u = managementSystem.function.verification_cookie(request)
  if not b:
    return HttpResponseRedirect('/')
  Success, errID, fileName = False, 0, ''
  fileList = request.POST.get("id", "")
  if len(fileList) <= 0:
    errID = 400
  elif managementSystem.function.jurisdiction('editEquipment.html', u.levelName):
    fileName = managementSystem.function.zipPack(fileList, Equipment)
    mylogs.objects.create(
      user_id=u.id,
      time=strftime('%Y-%m-%d %H:%M'),
      content='导出编辑设备'
    )
    Success = True
  else:
    errID = 303
  html = HttpResponse(json.dumps({
    'Success': Success,
    'errID': errID,
    'html': fileName
  }))
  return html

def changeEqu(request):
  if request.method != 'POST':
    return HttpResponse()
  b, u = managementSystem.function.verification_cookie(request)
  Success, errID = False, 0
  if not b:
    return HttpResponseRedirect('/')
  elif managementSystem.function.jurisdiction('EquipmentManage.html', u.levelName):
    d = request.POST.get("id", "")
    if request.POST.get("type", "") == 'del':
      obj = EquipmentType.objects.get(id=d)
      mylogs.objects.create(
        user_id=u.id,
        time=strftime('%Y-%m-%d %H:%M'),
        content='删除了节点[' + obj.templateName + ']'
      )
      obj.delete()
      Success = True
    elif request.POST.get("type", "") == 'change':
      obj = EquipmentType.objects.get(id=d)
      obj.templateName = request.POST.get("text", "")
      mylogs.objects.create(
        user_id=u.id,
        time=strftime('%Y-%m-%d %H:%M'),
        content='修改了节点[' + obj.templateName + ']的名称'
      )
      obj.save()
      Success = True
  else:
    errID = 303
  html = HttpResponse(json.dumps({
    'Success': Success,
    'errID': errID,
    'html': ""
  }))
  return html

def changePower(request):
  if request.method != 'POST':
    return HttpResponse()
  b, u = managementSystem.function.verification_cookie(request)
  Success, errID = False, 0
  if not b:
    return HttpResponseRedirect('/')
  elif managementSystem.function.jurisdiction('PowerDistribution.html', u.levelName):

    if request.POST.get("type", "") == 'del':
      d = request.POST.get("id", "")
      Power.objects.get(id=d).delete()
      Success = True
    elif request.POST.get("type", "") == 'add':
      uf = MyForm.importReport(request.POST, request.FILES)
      if uf.is_valid():
        Power.objects.create(  # 写入数据库
          imgName=os.path.splitext(request.POST['name'])[0],
          file=uf.cleaned_data['file'],
          PeopleUpload=u,
          uploadTime=int(time.time()),
        )
        mylogs.objects.create(
          user_id=u.id,
          time=strftime('%Y-%m-%d %H:%M'),
          content='删除了变配文件[' + request.POST['name'] + ']'
        )
      Success = True
  else:
    errID = 303
  html = HttpResponse(json.dumps({
    'Success': Success,
    'errID': errID,
    'html': ""
  }))
  return html

def getPage(request):
    if request.method != 'POST':
        return HttpResponse()
    b, u = managementSystem.function.verification_cookie(request)
    if not b:
        return HttpResponseRedirect('/')
    pageName = request.POST.get('getType', 'error.html')
    if managementSystem.function.jurisdiction(pageName, u.levelName):
      return render_to_response(
        pageName,
        Context(managementSystem.function.getDict(pageName))
      )
    else:
      return render_to_response('notJurisdiction.html')


def preview(request):
  if request.method != 'POST':
    return HttpResponse()
  b, u = managementSystem.function.verification_cookie(request)
  if not b:
    return HttpResponseRedirect('/')
  Success, errID = False, 0
  exp = ""
  if managementSystem.function.jurisdiction('addReport.html', u.levelName):
    fileid = request.POST.get("id", "0")
    exp = experimentalType.objects.get(id=fileid)
    Success = True
  else:
    errID = 303
    Success = False
  html = HttpResponse(json.dumps({
    'Success': Success,
    'errID': errID,
    'html': exp.templatePositions
  }))
  return html



#修改权限
def changeJuris(request):
  if request.method != 'POST':
    return HttpResponse()
  b, u = managementSystem.function.verification_cookie(request)
  if not b:
    return HttpResponseRedirect('/')
  Success, errID = False, 0
  if managementSystem.function.jurisdiction('JurisdictionManage.html', u.levelName):
    _id = request.POST.get('id', None)
    _lv = request.POST.get('lv', None)
    if _id is None or _lv is None:
      errID = 1
    elif int(_lv) > u.levelName:
      errID = 305  # 不能给予超过自身权限的权限
    elif Admin.objects.get(id=_id).levelName > u.levelName:
      errID = 304  # 不能修改超过自身权限的用户
    else:
      _u = Admin.objects.get(id=_id)
      _u.levelName = int(_lv)
      _u.save()

      mylogs.objects.create(
        user_id=u.id,
        time=strftime('%Y-%m-%d %H:%M'),
        content='修改了[' + _u.nickName + ']的级别'
      )
      Success = True
  else:
    errID = 303
  html = HttpResponse(json.dumps({
    'Success': Success,
    'errID': errID,
    'html': ''
  }))
  return html
# def myTest(request):
#   return HttpResponse('<h2>收到了你的' + request.method + '消息:</h2>' + ', '.join([str(x) for x in request.GET.items()]))
