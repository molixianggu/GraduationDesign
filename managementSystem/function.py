
from managementSystem.models import *

import hashlib                                  #md5 验证

import os

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
  }
  return d.get(pageName, 10) <= lv
