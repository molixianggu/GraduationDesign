from django.db import models

from django.contrib import admin

class Admin(models.Model):
    userName = models.CharField(max_length = 30)    #用户名
    passWord = models.CharField(max_length = 32)    #密码
    nickName = models.CharField(max_length = 32)    #昵称
    question = models.IntegerField(default = 0)     #问题
    answer = models.CharField(max_length = 50)      #答案
    levelName = models.IntegerField(default = 0)    #用户权限
    checkAdmin = models.BooleanField()              #审核中
    loginIP = models.CharField(max_length = 20)     #登录IP
    loginTime = models.IntegerField()               #登录时间


class adminGroup(models.Model):
    groupname = models.CharField(max_length = 30)   #管理组名
    description = models.TextField()                #描述
    groupsite = models.CharField(max_length = 30)   #默认进入
    checkinfo = models.BooleanField()               #审核中


class device(models.Model):
    initdeviceid = models.CharField(max_length = 32, null = True)
    testformkey = models.CharField(max_length = 1024, null = True)
    substationid = models.CharField(max_length = 32)
    devicetypeid = models.CharField(max_length = 32)
    devicerunid = models.CharField(max_length = 128, null = True)
    devicename = models.CharField(max_length = 200, null = True)
    olinedate = models.DateField(null = True)
    offlinedate = models.DateField(null = True)
    devicesno = models.CharField(max_length = 200, null = True)
    deviceplace = models.CharField(max_length = 1024, null = True)
    dataindex = models.CharField(max_length = 1024, null = True)
#    deviceinfo = blob
#    deviceruler = blob
    pdfkey   = models.CharField(max_length = 1024, null = True)


class deviceType(models.Model):
    parentid = models.CharField(max_length = 32, null = True)
    pathcode = models.CharField(max_length = 200, null = True)
    devicetypename = models.CharField(max_length = 200, null = True)
#    devicetyperuler = blob
    dataindex = models.CharField(max_length = 1024, null = True)
    dataenabled = models.IntegerField(null = True)
    deviceformkey = models.CharField(max_length = 1024, null = True)
    testformkey = models.CharField(max_length = 1024, null = True)
    pdfkey = models.CharField(max_length = 1024, null = True)
    xlskey = models.CharField(max_length = 1024, null = True)


class subStation(models.Model):
    substationid = models.CharField(max_length = 200, null = True)
    substationname = models.CharField(max_length = 200, null = True)
    substationadrr = models.CharField(max_length = 128, null = True)
    substationman = models.CharField(max_length = 128, null = True)
    mobile = models.CharField(max_length = 128, null = True)
    teloffice = models.CharField(max_length = 128, null = True)
    fax = models.CharField(max_length = 128, null = True)
    email = models.CharField(max_length = 128, null = True)
    dataindex = models.CharField(max_length = 1024, null = True)
    dataenabled = models.IntegerField(null = True)

class mylogs(models.Model):
    user = models.ForeignKey(Admin, related_name='actions')
    time = models.CharField(max_length = 128)
    content = models.CharField(max_length = 200, null = True)

class experimentalType(models.Model):
  category = models.CharField(max_length=200)  # 所属分类
  templatePositions = models.FileField(upload_to='./managementSystem/static/data/experimentalType')  # 模板位置
  templateName = models.CharField(max_length=200, null=True, default="")
  indexKey = models.CharField(max_length=200, null=True, default="")


class experimental(models.Model):
  experimentalName = models.CharField(max_length=200)
  file = models.FileField(upload_to='./managementSystem/static/data/experimental')
  PeopleUpload = models.ForeignKey(Admin, related_name='experimentals')
  uploadTime = models.IntegerField(null=True, default=0)


# devicetyperuler = blob
#    dataindex = models.CharField(max_length = 1024, null = True)
#    dataenabled = models.IntegerField(null = True)
#    deviceformkey = models.CharField(max_length = 1024, null = True)
#    testformkey = models.CharField(max_length = 1024, null = True)
#    pdfkey = models.CharField(max_length = 1024, null = True)
#    xlskey = models.CharField(max_length = 1024, null = True)


admin.site.register(mylogs)
admin.site.register(Admin)
admin.site.register(experimentalType)
admin.site.register(experimental)
