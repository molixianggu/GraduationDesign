
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
        'juris': [
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
    return d


def jurisdiction(pageName, lv):
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
