
from managementSystem.models import *

import hashlib                                  #md5 验证

import json

import os

import time

import zipfile

def h_md5(u):
    s = (str(u.id) + '盐' + u.userName + u.loginIP)
    return hashlib.md5(s.encode()).hexdigest()

def verification_cookie(request):
    userName = request.COOKIES.get('userName', '')
    key = request.COOKIES.get('key', '')
    u = Admin.objects.filter(
        userName = userName
    )[:1]
    if len(u) == 1:
        return all((key, userName, key == h_md5(u[0]))), u[0]
    return False, None

def getDict(pageName):
    d = {}
    if pageName == 'home.html':
        d = {
            'logs':mylogs.objects.all().order_by('-time')[:8]
        }
    elif pageName == 'userManagement.html':
        d = {
            'users':Admin.objects.all()
        }
    elif pageName == 'JurisdictionManage.html':
      d = {
        'users': Admin.objects.all(),
        'juris': [            #添加身份
          (0, '游客'),
          (2, '实验员'),
          (4, '维护人员'),
          (5, '管理员'),
          (10, '超级用户'),
        ]
      }
    elif pageName == 'addReport.html':
        d = {
            'templateList':experimentalType.objects.all()
        }
    elif pageName == 'findReport.html':
      d = {
        'templateList': experimental.objects.all()
      }
    elif pageName == 'logsManage.html':
      d = {
        'logsList': mylogs.objects.all().order_by('-time')
      }
    elif pageName == 'delReport.html':
      d = {
        'templateList': experimental.objects.all()
      }
    elif pageName == 'outputReport.html':
      d = {
        'templateList': experimental.objects.all()
      }
    elif pageName == 'addEquipment.html':
      d = {
        'templateList': EquipmentType.objects.all()
      }
    elif pageName == 'findEquipment.html':
      d = {
        'templateList': Equipment.objects.all()
      }
    elif pageName == 'delEquipment.html':
      d = {
        'templateList': Equipment.objects.all()
      }
    elif pageName == 'EquipmentManage.html':
      f = [
        {
          'id': x.id,
          'pid': x.DirectParent,
          'inf': {
            'templateName': x.templateName,
            'category': x.category,
            'templatePositions': x.templatePositions.name,
            'indexKey': x.indexKey
          }
        } for x in EquipmentType.objects.all()
        ]
      w = json.dumps(f, indent=4, ensure_ascii=False)
      d = {
        'tree': w
      }
    elif pageName == 'editEquipment.html':
      d = {
        'templateList': Equipment.objects.all()
      }
    elif pageName == 'EquipmentLogs.html':
      d = {
        'logsList':EquipmentLogs.objects.all()
      }
    elif pageName == 'a.html':
      d = {
        'txt':'''0.1.3版本 更新说明:
1. 修复锁屏无效问题
2. 更改权限时不能给与超过自身的权限
3. 实现上传页面的批量上传模块, 优化用户上传体验
4. 添加了只刷新当前页面的功能, 屏蔽了再次点击当前页面会触发加载

0.2.0版本 更新说明:
1. 实现导出和删除实验
2. 添加查找页面按时间查找
3. 修复部分预览后选择项丢失的问题
4. 修复Home页面日志过长超出页面的问题
5. 修改部分密码验证问题
6. 增强针对了SQL注入的防护性能

0.2.1版本 更新说明:     #2016年4月8日
1. 优化在[删除和导出]界面已经多选后预览会丢失选项的问题.
2. 实现单文件上传的小型弹窗
3. 实现设备类型管理的树形列表
4. 新增导出设备文件
5. 新增添加设备类型, 树的子项功能

0.3.0版本 更新 : #2016年4月18日01:46:25
1. 新增设备历史页面
2. 实现设备树添加子项弹窗
3. 新增更新日志
4. 优化了程序启动速度
5. 新增可以以 new 参数启动来清理多余的文件并生成新的预览缓存

0.4.5版本 更新 : #2016年4月19日23:22:38
1. 新增主题颜色改变, 目前有蓝色和灰白两个主题; (可以点击名字下的修改主题修改)
2. 新增变配电所检索及预览

0.5.1版本 更新 : #2016年4月20日23:42:35
1. 新增变配电所预览时的拖动和缩放功能



'''
      }
    return d


def jurisdiction(pageName, lv):     #修改权限
  d = {
    'home.html': 0,
    'addReport.html': 2,  # 新建实验
    'importReport.html': 2,
    'userManagement.html': 4,  # 管理用户
    'JurisdictionManage.html': 5,
    'logsManage.html': 3,
    'findReport.html': 2,
    'delReport.html': 4,
    'outputReport.html': 2,
    'addEquipment.html': 4,
    'findEquipment.html': 4,
    'delEquipment.html': 4,
    'EquipmentManage.html': 5,
    'editEquipment.html': 4,
    'EquipmentLogs.html':4,
    'PowerDistribution.html':4,
    'a.html':4,         #查看更新日志
  }
  return d.get(pageName, 10) <= lv


def zipPack(fileList):
  l = [x for x in fileList.split(',') if x]
  if len(l) <= 1:
    return experimental.objects.get(id=int(l[0])).file.name[17:]
  filename = os.path.join(r'managementSystem\static\data\zipPack', str(int(time.time())) + '.zip')
  with zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED) as f:
    for _id in fileList.split(','):
      if _id:
        e = experimental.objects.get(id=int(_id))
        f.write(e.file.name, arcname=e.experimentalName)
  return filename[17:]
