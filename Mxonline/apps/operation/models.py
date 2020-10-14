from django.db import models
from apps.users.models import BaseModel

from django.contrib.auth import get_user_model
from apps.courses.models import Course

#使用django自带的users表
UserProfile = get_user_model()

class UserAsk(BaseModel):
    name = models.CharField(max_length=20, verbose_name="姓名")
    mobile = models.CharField(max_length=11, verbose_name="手机")
    course_name = models.CharField(max_length=50, verbose_name="课程名")

    class Meta:
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name



class CourseComments(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    comments = models.CharField(max_length=200, verbose_name="评论内容")

    class Meta:
        verbose_name = "课程评论"
        verbose_name_plural = verbose_name

class UserFavorite(BaseModel):
    #收藏
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    #收藏数据id
    fav_id = models.IntegerField(verbose_name="数据id")
    fav_type = models.IntegerField(choices=((1,"课程"),(2,"课程机构"),(3,"讲师")), default=1, verbose_name="收藏类型")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name

class UserMessage(BaseModel):
    #系统给用户发的消息
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    message = models.CharField(max_length=200, verbose_name="消息内容")
    has_read = models.BooleanField(default=False, verbose_name="是否已读")

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name

class UserCourse(BaseModel):
    '''
    多对多  用户学习了哪些课程
    '''
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")

    class Meta:
        verbose_name = "用户课程"
        verbose_name_plural = verbose_name