from django.db import models
from django.contrib.auth.models import AbstractUser,User

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(null=False,max_length=20,default="",verbose_name="用户名")
    password = models.CharField(null=False,max_length=20,default="",verbose_name="密码")
    avatar = models.FileField(upload_to="avatars/", default="avatars/default.png", verbose_name="头像")
    email = models.CharField(null=True,max_length=32,verbose_name="邮箱")
    create_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "9.用户信息"

class houseAccount(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(null=False,max_length=20,default="",verbose_name="房客姓名")
    sex = models.CharField(null=False,max_length=20,default="",verbose_name="房客性别")
    identity = models.CharField(null=False,max_length=20,default="",verbose_name="房客身份证")
    num_house = models.IntegerField(null=False,verbose_name="房间号")
    day_house = models.IntegerField(null=False,verbose_name="订房天数")
    price_house = models.IntegerField(null=False,verbose_name="房价")
    day_time = models.CharField(null=False, max_length=20,default="",verbose_name="住房时间")
    remark_house = models.CharField(null=False, max_length=225,default="",verbose_name="备注（住房）")
    cata_house = models.ForeignKey(to="cataHouse", on_delete=models.CASCADE,verbose_name="住房类型")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "1.住房"
class bathAccount(models.Model):
    # id = models.AutoField(primary_key=True)
    num_bath = models.IntegerField(null=False,verbose_name="洗浴人数")
    num_brand = models.IntegerField(null=False,default="",verbose_name="洗浴手牌号")
    num_back = models.IntegerField(null=False,verbose_name="搓背人数")
    remark_bath = models.CharField(null=False,max_length=225,default="",verbose_name="备注（洗浴）")
    day_bath = models.CharField(null=False,max_length=32,default="",verbose_name="洗浴时间")
    price_bath = models.IntegerField(null=False,verbose_name="洗浴价格")
    def __str__(self):
        return self.num_brand
    class Meta:
        verbose_name_plural = "2.洗浴"
class cataHouse(models.Model):
    # id = models.AutoField(primary_key=True)
    house_name = models.CharField(null=False,max_length=20,default="",verbose_name="住房类型")
    def __str__(self):
        return self.houseName
    class Meta:
        verbose_name_plural = "3.房间类型"

class expenseAccount(models.Model):
    # id = models.AutoField(primary_key=True)
    expen_cate = models.CharField(null=False,max_length=20,default="",verbose_name="支出类型")
    price_account = models.IntegerField(null=False,verbose_name="支出金额")
    day_expense = models.CharField(null=False,max_length=20,default="",verbose_name="时间")
    remark_account = models.CharField(null=False,max_length=225,default="",verbose_name="支出（备注）")
    def __str__(self):
        return self.expenCate
    class Meta:
        verbose_name_plural = "4.支出"

class incomeAccount(models.Model):
    # id = models.AutoField(primary_key=True)
    day_income = models.CharField(null=False,max_length=32,default="",verbose_name="住房类型")
    total_bath = models.IntegerField(null=True,verbose_name="洗浴总收入")
    total_House = models.IntegerField(null=True,verbose_name="住房总收入")
    total_store = models.IntegerField(null=True,verbose_name="百货总收入")
    total_bath_house = models.IntegerField(null=True,verbose_name="住房和洗浴总收入")
    total_pay = models.IntegerField(null=True,verbose_name="总支出")
    total_income = models.IntegerField(null=True,verbose_name="总收入")
    remark_income = models.CharField(null=False,max_length=225,default="",verbose_name="备注（收入）")
    def __str__(self):
        return self.id
    class Meta:
        verbose_name_plural = "5.总收入"


class storeAccount(models.Model):
    # id = models.AutoField(primary_key=True)
    cata_store = models.CharField(null=False,max_length=32,default="",verbose_name="百货类型")
    price_store = models.IntegerField(null=True,verbose_name="百货价格")
    day_store = models.CharField(null=False,max_length=32,default="",verbose_name="时间")
    remark_store = models.CharField(null=False,max_length=225,default="",verbose_name="备注（百货）")
    def __str__(self):
        return self.cataStore
    class Meta:
        verbose_name_plural = "6.百货收入"

class otherAccount(models.Model):
    # id = models.AutoField(primary_key=True)
    cata_other = models.CharField(null=False,max_length=32,default="",verbose_name="其他收入类型")
    price_other = models.IntegerField(null=True,verbose_name="住房其他收入价格")
    day_other = models.CharField(null=False,max_length=32,default="",verbose_name="时间")
    remark_other = models.CharField(null=False,max_length=225,default="",verbose_name="备注（其他）")
    def __str__(self):
        return self.cataOther
    class Meta:
        verbose_name_plural = "7.其他收入"
class electricityAccount(models.Model):
    # id = models.AutoField(primary_key=True)
    day_elect = models.CharField(null=False,max_length=60,default="",verbose_name="缴费时间")
    num_elect = models.CharField(null=False,max_length=60,default="",verbose_name="用电度数")
    price_elect = models.IntegerField(null=True,verbose_name="电费")

    def __str__(self):
        return self.dayElect
    class Meta:
        verbose_name_plural = "8.电费"