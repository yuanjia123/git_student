from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from datetime import datetime

GENDER_CHOICES = (
        ("male","男"),
        ("female","女")
    )


class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    class Meta:
        #执行makemigratetion的时候不产生表
        abstract = True

class UserProfile(AbstractBaseUser):
    '''
    1、继承django自带的用户表  增加下面字段  nick_name、birthday、gender、address、mobile、image
    2、在Mxonline的setting中设置 86行的 AUTH_USER_MODEL = "users.UserProfile"如果不懂可以百度AUTH_USER_MODEL 是干嘛的
    '''
    identifier = models.CharField(max_length=40, unique=True)
    USERNAME_FIELD = 'identifier'

    # 报  AttributeError: type object 'UserProfile' has no attribute 'USERNAME_FIELD' 错误
    # 需要加上10 11行

    nick_name = models.CharField(max_length=50,verbose_name="昵称",default="")
    birthday = models.DateField(verbose_name="生日",null=True,blank=True) #null=True,blank=True可以为空
    gender = models.CharField(verbose_name="性别",choices=GENDER_CHOICES,max_length=6)
    address = models.CharField(max_length=100,verbose_name="地址",default="")
    mobile = models.CharField(max_length=11,unique = True,verbose_name="手机号码")  #unique = True手机号码唯一
    image = models.ImageField(upload_to="head_image/%Y/%m",default="default.jpg")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name


