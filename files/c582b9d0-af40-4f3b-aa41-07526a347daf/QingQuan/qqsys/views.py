import datetime
from django.core import serializers
from django.core.serializers import serialize
from django.contrib.sessions import serializers
from django.http import JsonResponse
from django.shortcuts import HttpResponse, render, redirect
from qqsys import models
from django.db.models import Sum,Count
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json
from geetest import GeetestLib
from qqsys import forms
# Create your views here.

# 使用极验滑动验证码的登录
#
# def login(request):
#     # if request.is_ajax():  # 如果是AJAX请求
#     if request.method == "POST":
#         # 初始化一个给AJAX返回的数据
#         ret = {"status": 0, "msg": ""}
#         # 从提交过来的数据中 取到用户名和密码
#         username = request.POST.get("username")
#         pwd = request.POST.get("password")
#         # 获取极验 滑动验证码相关的参数
#         gt = GeetestLib(pc_geetest_id, pc_geetest_key)
#         challenge = request.POST.get(gt.FN_CHALLENGE, '')
#         validate = request.POST.get(gt.FN_VALIDATE, '')
#         seccode = request.POST.get(gt.FN_SECCODE, '')
#         status = request.session[gt.GT_STATUS_SESSION_KEY]
#         user_id = request.session["user_id"]
#
#         if status:
#             result = gt.success_validate(challenge, validate, seccode, user_id)
#         else:
#             result = gt.failback_validate(challenge, validate, seccode)
#         if result:
#             # 验证码正确
#             # 利用auth模块做用户名和密码的校验
#             user = auth.authenticate(username=username, password=pwd)
#             if user:
#                 # 用户名密码正确
#                 # 给用户做登录
#                 auth.login(request, user)
#                 ret["msg"] = "/index/"
#             else:
#                 # 用户名密码错误
#                 ret["status"] = 1
#                 ret["msg"] = "用户名或密码错误！"
#         else:
#             ret["status"] = 1
#             ret["msg"] = "验证码错误"
#
#         return JsonResponse(ret)
#     return render(request, "login.html")
# # 请在官网申请ID使用，示例ID不可使用
# pc_geetest_id = "67e8343bf6024db330680b4dd70c0bd0"
# pc_geetest_key = "2cbedf94513e238e43eef4051efc580e"
#
#
# # 处理极验 获取验证码的视图
# def get_geetest(request):
#     user_id = 'test'
#     gt = GeetestLib(pc_geetest_id, pc_geetest_key)
#     status = gt.pre_process(user_id)
#     request.session[gt.GT_STATUS_SESSION_KEY] = status
#     request.session["user_id"] = user_id
#     response_str = gt.get_response_str()
#     return HttpResponse(response_str)
#
#
# # 注册的视图函数
# def register(request):
#     if request.method == "POST":
#         ret = {"status": 0, "msg": ""}
#         form_obj = forms.RegForm(request.POST)
#         print(request.POST)
#         # 帮我做校验
#         if form_obj.is_valid():
#             # 校验通过，去数据库创建一个新的用户
#             form_obj.cleaned_data.pop("re_password")
#             avatar_img = request.FILES.get("avatar")
#             models.UserInfo.objects.create_user(**form_obj.cleaned_data, avatar=avatar_img)
#             ret["msg"] = "/index/"
#             return JsonResponse(ret)
#         else:
#             print(form_obj.errors)
#             ret["status"] = 1
#             ret["msg"] = form_obj.errors
#             print(ret)
#             print("=" * 120)
#             return JsonResponse(ret)
#     # 生成一个form对象
#     form_obj = forms.RegForm()
#     print(form_obj.fields)
#     return render(request, "admin_register.html", {"form_obj": form_obj})





# 后台房间列表显示


# 请在官网申请ID使用，示例ID不可使用
pc_geetest_id = "67e8343bf6024db330680b4dd70c0bd0"
pc_geetest_key = "2cbedf94513e238e43eef4051efc580e"

def adminLogin(request):
    # if request.is_ajax():  # 如果是AJAX请求
    if request.method == "POST":
        # 初始化一个给AJAX返回的数据
        ret = {"status": 0, "msg": ""}
        # 从提交过来的数据中 取到用户名和密码
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        # 获取极验 滑动验证码相关的参数
        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        challenge = request.POST.get(gt.FN_CHALLENGE, '')
        validate = request.POST.get(gt.FN_VALIDATE, '')
        seccode = request.POST.get(gt.FN_SECCODE, '')
        status = request.session[gt.GT_STATUS_SESSION_KEY]
        user_id = request.session["user_id"]

        if status:
            result = gt.success_validate(challenge, validate, seccode, user_id)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
        if result:
            # 验证码正确
            # 利用auth模块做用户名和密码的校验
            user = auth.authenticate(username=username, password=pwd)
            if user:
                # 用户名密码正确
                # 给用户做登录
                auth.login(request, user)
                ret["msg"] = "/adminHouse/"
            else:
                # 用户名密码错误
                ret["status"] = 1
                ret["msg"] = "用户名或密码错误！"
        else:
            ret["status"] = 1
            ret["msg"] = "验证码错误"

        return JsonResponse(ret)
    return render(request, "admin_login.html")


def get_geetest(request):
    user_id = 'test'
    gt = GeetestLib(pc_geetest_id, pc_geetest_key)
    status = gt.pre_process(user_id)
    request.session[gt.GT_STATUS_SESSION_KEY] = status
    request.session["user_id"] = user_id
    response_str = gt.get_response_str()
    return HttpResponse(response_str)

# 注册的视图函数
def adminRegister(request):
    if request.method == "POST":
        ret = {"status": 0, "msg": ""}
        form_obj = forms.RegForm(request.POST)
        print(request.POST)
        # 帮我做校验
        if form_obj.is_valid():
            # 校验通过，去数据库创建一个新的用户
            form_obj.cleaned_data.pop("re_password")
            avatar_img = request.FILES.get("avatar")
            User.objects.create_user(**form_obj.cleaned_data)
            ret["msg"] = "/adminHouse/"
            return JsonResponse(ret)
        else:
            ret["status"] = 1
            ret["msg"] = form_obj.errors
            return JsonResponse(ret)
    # 生成一个form对象
    form_obj = forms.RegForm()
    print(form_obj.fields)
    return render(request, "admin_register.html", {"form_obj": form_obj})



def adminHouse(request):
    page_num = request.GET.get("page")
    print(page_num, type(page_num))

    # 总数据是多少
    total_count = models.houseAccount.objects.all().count()
    # print(total_count)
    from utils.mypage import Page
    page_obj = Page(page_num, total_count, per_page=10, url_prefix="/adminHouse/", max_page=9, )

    ret = models.houseAccount.objects.all().order_by("-dayTime","-id")[page_obj.start:page_obj.end]

    page_html = page_obj.page_html()

    return render(request, "admin_houselist.html", {"house_list": ret, "page_html": page_html})
    # now = datetime()
    # print(now)
    # ret = models.houseAccount.objects.all().order_by("id")
    # return render(request,"admin_houselist.html",{"house_list":ret})
# 添加住房
def adminAddhouse(request):
    error_msg = ""
    if request.method == "POST":
        new_house_name = request.POST.get("house_name", None)
        new_house_sex = request.POST.get("house_sex", None)
        new_house_id = request.POST.get("house_id", None)
        new_house_cata = request.POST.get("cata_list", None)
        new_house_num = request.POST.get("house_num", None)
        new_house_time = request.POST.get("house_time", None)
        new_house_price = request.POST.get("house_price", None)
        new_dayTime = request.POST.get("dayTime", None)
        new_house_remark = request.POST.get("house_remark", None)
        models.houseAccount.objects.create(name=new_house_name, sex=new_house_sex,
                                        identity=new_house_id, cataHouse_id=new_house_cata,
                                        numHouse=new_house_num, dayHouse=new_house_time,
                                           priceHouse=new_house_price,dayTime=new_dayTime,remarkHouse=new_house_remark)
        return redirect("/adminHouse/")

    # when requesting pages, back last page
    cata_ret = models.cataHouse.objects.all().order_by("id")
    return render(request, "admin_addhouse.html", {"error": error_msg,"cata_list":cata_ret})
#编辑住房
def adminEdithouse(request):
    if request.method == "POST":
        # ======get laste========
        new_house_id = request.POST.get("id",None)
        new_house_name = request.POST.get("house_name", None)
        new_house_sex = request.POST.get("house_sex", None)
        new_house_idcar = request.POST.get("house_id", None)
        new_house_cata = request.POST.get("cata_list", None)
        new_house_num = request.POST.get("house_num", None)
        new_house_time = request.POST.get("house_time", None)
        new_house_price = request.POST.get("house_price", None)
        new_dayTime = request.POST.get("dayTime", None)
        new_house_remark = request.POST.get("house_remark", None)
        # ========update=========
        edit_house_obj = models.houseAccount.objects.get(id=new_house_id)
        edit_house_obj.name = new_house_name
        edit_house_obj.sex = new_house_sex
        edit_house_obj.identity = new_house_idcar
        edit_house_obj.cataHouse_id = new_house_cata
        edit_house_obj.numHouse = new_house_num
        edit_house_obj.dayHouse = new_house_time
        edit_house_obj.priceHouse = new_house_price
        edit_house_obj.dayTime = new_dayTime
        edit_house_obj.remarkHouse = new_house_remark
        edit_house_obj.save()
        return redirect("/adminHouse/")

    edit_id = request.GET.get("id")
    if edit_id:
        edit_house = models.houseAccount.objects.get(id=edit_id)
        ret = models.cataHouse.objects.all()
        return render(request, "admin_edithouse.html", {"cata_list": ret, "house_obj": edit_house})
    else:
        return HttpResponse("Unsuccess")

# 删除住房
def adminDelhouse(request):
    del_id = request.GET.get("id", None)
    if del_id:
        del_obj = models.houseAccount.objects.get(id=del_id)
        del_obj.delete()
        return redirect("/adminHouse/")
    else:
        return HttpResponse("data not exist")

# 后台洗澡列表显示========================================

def adminBath(request):
    page_num = request.GET.get("page")
    print(page_num, type(page_num))

    # 总数据是多少
    total_count = models.bathAccount.objects.all().count()
    # print(total_count)
    from utils.mypage import Page
    page_obj = Page(page_num, total_count, per_page=10, url_prefix="/adminBath/", max_page=9, )
    # print("bath:",page_obj.end)
    ret = models.bathAccount.objects.all().order_by("-dayBath","-id")[page_obj.start:page_obj.end]
    # print("ret:",ret)
    page_html = page_obj.page_html()
    # ret = models.bathAccount.objects.all().order_by("id")
    return render(request,"admin_bathlist.html",{"bath_list": ret,"page_html": page_html})

# 添加洗浴
def adminAddbath(request):
    error_msg = ""
    if request.method == "POST":
        new_bath_num = request.POST.get("bath_num", None)
        new_bath_back = request.POST.get("bath_back", None)
        new_bath_price = request.POST.get("bath_price", None)
        new_bath_time = request.POST.get("bath_time", None)
        new_bath_remark = request.POST.get("bath_remark", None)
        models.bathAccount.objects.create(numBath=new_bath_num, numBack=new_bath_back,
                                        priceBath=new_bath_price, dayBath=new_bath_time,
                                        remarkBath=new_bath_remark)
        return redirect("/adminBath/")

    # when requesting pages, back last page
    return render(request, "admin_addbath.html", {"error": error_msg})
#删除洗浴
def adminDelbath(request):
    del_id = request.GET.get("id", None)
    if del_id:
        del_obj = models.bathAccount.objects.get(id=del_id)
        del_obj.delete()
        return redirect("/adminBath/")
    else:
        return HttpResponse("data not exist")
    return render(request,"admin_bathlist.html")

# 编辑洗浴
def adminEditbath(request):
    if request.method == "POST":
        # ======get laste========
        new_bath_id = request.POST.get("id",None)
        new_bath_num = request.POST.get("bath_num", None)
        new_bath_back = request.POST.get("bath_back", None)
        new_bath_price = request.POST.get("bath_price", None)
        new_bath_time = request.POST.get("bath_time", None)
        new_bath_remark = request.POST.get("bath_remark", None)
        # ========update=========
        edit_bath_obj = models.bathAccount.objects.get(id=new_bath_id)
        edit_bath_obj.numBath = new_bath_num
        edit_bath_obj.numBack = new_bath_back
        edit_bath_obj.priceBath = new_bath_price
        edit_bath_obj.dayBath = new_bath_time
        edit_bath_obj.remarkBath = new_bath_remark
        edit_bath_obj.save()
        return redirect("/adminBath/")

    edit_id = request.GET.get("id")
    if edit_id:
        edit_bath = models.bathAccount.objects.get(id=edit_id)
        return render(request, "admin_editbath.html", {"bath_obj": edit_bath})
    else:
        return HttpResponse("Unsuccess")
# 支出显示
def adminExpensive(request):
    page_num = request.GET.get("page")
    print(page_num, type(page_num))
    
    # 总数据是多少
    total_count = models.expenseAccount.objects.all().count()
    # print(total_count)
    from utils.mypage import Page
    page_obj = Page(page_num, total_count, per_page=10, url_prefix="/adminExpensive/", max_page=9, )

    ret = models.expenseAccount.objects.all().order_by("-dayExpense","-id")[page_obj.start:page_obj.end]

    page_html = page_obj.page_html()

    return render(request,"admin_Expensivelist.html",{"expensive_obj":ret,"page_html":page_html})
# 删除支出
def adminDelexpen(request):
    del_id = request.GET.get("id", None)
    if del_id:
        del_obj = models.expenseAccount.objects.get(id=del_id)
        del_obj.delete()
        return redirect("/adminExpensive/")
    else:
        return HttpResponse("data not exist")
    return render(request, "admin_Expensivelist.html")
# 添加支出
def adminAddexpense(request):
    error_msg = ""
    if request.method == "POST":
        new_expenCate = request.POST.get("expense_cata", None)
        new_priceAccount = request.POST.get("expense_money", None)
        new_remarkAccount = request.POST.get("expense_remark", None)
        new_dayTime = request.POST.get("dayTime", None)
        models.expenseAccount.objects.create(expenCate=new_expenCate, priceAccount=new_priceAccount,
                                           remarkAccount=new_remarkAccount,dayExpense=new_dayTime)
        return redirect("/adminExpensive/")

    # when requesting pages, back last page
    return render(request, "admin_addexpense.html", {"error": error_msg})



# 编辑支出
def adminEditexpen(request):
    if request.method == "POST":
        # ======get laste========
        new_expense_id = request.POST.get("id")
        new_expense_cata = request.POST.get("expense_cata",None)
        new_expense_money = request.POST.get("expense_money", None)
        new_dayTime = request.POST.get("dayTime", None)
        new_expense_remark = request.POST.get("expense_remark", None)
        # ========update=========
        edit_expense_obj = models.expenseAccount.objects.get(id=new_expense_id)
        edit_expense_obj.expenCate = new_expense_cata
        edit_expense_obj.priceAccount = new_expense_money
        edit_expense_obj.dayExpense = new_dayTime
        edit_expense_obj.remarkAccount = new_expense_remark
        edit_expense_obj.save()
        return redirect("/adminExpensive/")

    edit_id = request.GET.get("id")
    if edit_id:
        edit_expense = models.expenseAccount.objects.get(id=edit_id)
        return render(request, "admin_editexpense.html", {"expense_obj": edit_expense})
    else:
        return HttpResponse("Unsuccess")

# 每日收入
def adminDayIncome(request):
    error_msg = ""
    if request.method == "POST":
        new_dayincome = request.POST.get("dayincome_time", None)

        total_bath = models.bathAccount.objects.filter(dayBath=new_dayincome).aggregate(bath=Sum('priceBath'))
        if total_bath['bath']:
            total_bathn =total_bath['bath']
        else:
            total_bathn = 0

        total_numback = models.bathAccount.objects.filter(dayBath=new_dayincome).aggregate(back=Sum('numBack'))
        if total_numback['back']:
            total_numbackn = total_numback['back']
        else:
            total_numbackn = 0
        print(total_numbackn)

        total_incomebath = total_bathn - total_numbackn*10 #除去搓背的洗浴收入

        total_house = models.houseAccount.objects.filter(dayTime=new_dayincome).aggregate(house=Sum('priceHouse'))
        if total_house['house']:
            total_housen = total_house['house']
        else:
            total_housen = 0
        total_Store = models.storeAccount.objects.filter(dayStore=new_dayincome).aggregate(store=Sum('priceStore'))
        if total_Store['store']:
            total_Store = total_Store['store']
        else:
            total_Store = 0
        total_other = models.otherAccount.objects.filter(dayOther=new_dayincome).aggregate(other=Sum('priceOther'))
        if total_other['other']:
            total_other = total_other['other']
        else:
            total_other = 0


        total_bathStoreHouse = total_housen + total_incomebath + total_Store + total_other #洗浴收入、住房收入、其他收入和百货收入

        total_pay = models.expenseAccount.objects.filter(dayExpense=new_dayincome).aggregate(expense=Sum('priceAccount'))
        if total_pay['expense']:
            total_payn = total_pay['expense']
        else:
            total_payn = 0

        total_income = total_bathStoreHouse - total_payn # 每日净收入

        models.incomeAccount.objects.create(dayIncome=new_dayincome, totalBath=total_incomebath,
                                             totalBathHouse=total_bathStoreHouse, totalHouse=total_housen,
                                            totalPay=total_payn,totalIncome =total_income,totalStore = total_Store)
        return redirect("/adminIncome/")
        # print("total_bath:",total_bath['bath'],"total_numback:",total_numback['back'],"total_incomebath:",total_incomebath,"total_house:",total_house['house'],"")

        # total_income =  models.bathAccount.objects.values('priceBath').annotate(nums=Sum('priceBath')).filter(dayBath=new_dayincome)
        # print("total_income",total_income['nums'])

        # models.expenseAccount.objects.create(expenCate=new_expenCate, priceAccount=new_priceAccount,
        #                                      remarkAccount=new_remarkAccount, dayExpense=new_dayTime)
        # return redirect("/adminExpensive/")

    # when requesting pages, back last page
    return render(request, "admin_dayincome.html", {"error": error_msg})

def adminIncome(request):
    page_num = request.GET.get("page")
    print(page_num, type(page_num))

    # 总数据是多少
    total_count = models.incomeAccount.objects.all().count()
    # print(total_count)
    from utils.mypage import Page
    page_obj = Page(page_num, total_count, per_page=10, url_prefix="/adminIncome/", max_page=9, )

    ret = models.incomeAccount.objects.all().order_by("-dayIncome", "-id")[page_obj.start:page_obj.end]

    page_html = page_obj.page_html()



    return render(request, "admin_incomelist.html", {"income_list": ret, "page_html": page_html})


def adminDelincome(request):
    del_id = request.GET.get("id", None)
    if del_id:
        del_obj = models.incomeAccount.objects.get(id=del_id)
        del_obj.delete()
        return redirect("/adminIncome/")
    else:
        return HttpResponse("data not exist")
    return render(request, "admin_incomelist.html")


def adminEchartIncome(request):

    ret = models.incomeAccount.objects.all().order_by("dayIncome","id")
    # ret = serialize("json",ret)
    # print(ret)

    json_list = []

    for i in ret:
        json_dict = {}
        json_dict["id"] = i.id
        json_dict["totalIncome"] = i.totalIncome
        json_dict["dayIncome"] = i.dayIncome
        json_dict["remarkIncome"] = i.remarkIncome
        json_dict["totalBath"] = i.totalBath
        json_dict["totalBathHouse"] = i.totalBathHouse
        json_dict["totalHouse"] = i.totalHouse
        json_dict["totalPay"] = i.totalPay
        json_dict["totalStore"] = i.totalStore

        json_list.append(json_dict)

    ret1 = json.dumps(json_list)
    # ret1 = serialize("json", ret)
    # print(ret1,type(ret1))
    return render(request,'admin_chartIncome.html',{"ret": json.dumps(ret1)})

def adminStore(request):
    page_num = request.GET.get("page")
    print(page_num, type(page_num))

    # 总数据是多少
    total_count = models.storeAccount.objects.all().count()
    # print(total_count)
    from utils.mypage import Page
    page_obj = Page(page_num, total_count, per_page=10, url_prefix="/adminStore/", max_page=9, )

    ret = models.storeAccount.objects.all().order_by("-dayStore", "-id")[page_obj.start:page_obj.end]

    page_html = page_obj.page_html()

    return render(request, "admin_storelist.html", {"store_list": ret, "page_html": page_html})


def adminAddstore(request):
    error_msg = ""
    if request.method == "POST":
        new_store_cata = request.POST.get("store_cata", None)
        new_store_price = request.POST.get("store_price", None)
        new_store_time = request.POST.get("store_time", None)
        new_store_remark = request.POST.get("store_remark", None)
        models.storeAccount.objects.create(cataStore=new_store_cata,priceStore=new_store_price, dayStore=new_store_time,
                                           remarkStore=new_store_remark)
        return redirect("/adminStore/")

    # when requesting pages, back last page
    return render(request, "admin_addstore.html", {"error": error_msg})

def adminDelstore(request):
    del_id = request.GET.get("id", None)
    if del_id:
        del_obj = models.storeAccount.objects.get(id=del_id)
        del_obj.delete()
        return redirect("/adminStore/")
    else:
        return HttpResponse("data not exist")
    return render(request, "admin_storelist.html")


def adminEditstore(request):
    if request.method == "POST":
        # ======get laste========

        new_store_id = request.POST.get("id", None)
        new_store_cata = request.POST.get("store_cata", None)
        new_store_price = request.POST.get("store_price", None)
        new_store_time = request.POST.get("store_time", None)
        new_store_remark = request.POST.get("store_remark", None)
        # ========update=========
        edit_store_obj = models.storeAccount.objects.get(id=new_store_id)
        edit_store_obj.cataStore = new_store_cata
        edit_store_obj.priceStore = new_store_price
        edit_store_obj.dayStore = new_store_time
        edit_store_obj.remarkStore = new_store_remark
        edit_store_obj.save()
        return redirect("/adminStore/")

    edit_id = request.GET.get("id")
    if edit_id:
        edit_store = models.storeAccount.objects.get(id=edit_id)
        return render(request, "admin_editstore.html", {"store_obj": edit_store})
    else:
        return HttpResponse("Unsuccess")


def adminOther(request):
    page_num = request.GET.get("page")
    print(page_num, type(page_num))

    # 总数据是多少
    total_count = models.otherAccount.objects.all().count()
    # print(total_count)
    from utils.mypage import Page
    page_obj = Page(page_num, total_count, per_page=10, url_prefix="/adminOther/", max_page=9, )

    ret = models.otherAccount.objects.all().order_by("-dayOther", "-id")[page_obj.start:page_obj.end]

    page_html = page_obj.page_html()

    return render(request, "admin_otherlist.html", {"other_list": ret, "page_html": page_html})


def adminDelsother(request):
    del_id = request.GET.get("id", None)
    if del_id:
        del_obj = models.otherAccount.objects.get(id=del_id)
        del_obj.delete()
        return redirect("/adminOther/")
    else:
        return HttpResponse("data not exist")
    return render(request, "admin_storelist.html")

def adminEditother(request):
    if request.method == "POST":
        # ======get laste========

        new_other_id = request.POST.get("id", None)
        new_other_cata = request.POST.get("other_cata", None)
        new_other_price = request.POST.get("other_price", None)
        new_other_time = request.POST.get("other_time", None)
        new_other_remark = request.POST.get("other_remark", None)
        # ========update=========
        edit_other_obj = models.otherAccount.objects.get(id=new_other_id)
        edit_other_obj.cataOther = new_other_cata
        edit_other_obj.priceOther = new_other_price
        edit_other_obj.dayOther = new_other_time
        edit_other_obj.remarkOther = new_other_remark
        edit_other_obj.save()
        return redirect("/adminOther/")

    edit_id = request.GET.get("id")
    if edit_id:
        edit_other = models.otherAccount.objects.get(id=edit_id)
        return render(request, "admin_editother.html", {"other_obj": edit_other})
    else:
        return HttpResponse("Unsuccess")


def adminAddother(request):
    error_msg = ""
    if request.method == "POST":
        new_other_cata = request.POST.get("other_cata", None)
        new_other_price = request.POST.get("other_price", None)
        new_other_time = request.POST.get("other_time", None)
        new_other_remark = request.POST.get("other_remark", None)
        models.otherAccount.objects.create(cataOther=new_other_cata, priceOther=new_other_price,
                                           dayOther=new_other_time,
                                           remarkOther=new_other_remark)
        return redirect("/adminOther/")

    # when requesting pages, back last page
    return render(request, "admin_addother.html", {"error": error_msg})

