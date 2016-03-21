
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
    elif pageName == 'addReport.html':
        d = {
            'templateList':experimentalType.objects.all()
        }
    return d