"""QingQuan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from qqsys.views import  adminHouse,adminBath,adminAddhouse,\
    adminDelhouse,adminEdithouse,adminAddbath,adminDelbath,\
    adminEditbath,adminExpensive,adminAddexpense,adminEditexpen,\
    adminDelexpen,adminIncome,adminDelincome,adminDayIncome,\
    adminEchartIncome,adminStore,adminAddstore,adminDelstore,\
    adminEditstore,adminOther,adminAddother,adminEditother, \
    adminDelsother,adminLogin,get_geetest,adminRegister


urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminHouse/', adminHouse),
    path('adminAddhouse/', adminAddhouse),
    path('adminDelhouse/', adminDelhouse),
    path('adminEdithouse/', adminEdithouse),
    path('adminBath/', adminBath),
    path('adminAddbath/', adminAddbath),
    path('adminDelbath/', adminDelbath),
    path('adminEditbath/', adminEditbath),
    path('adminExpensive/', adminExpensive),
    path('adminAddexpense/', adminAddexpense),
    path('adminEditexpen/', adminEditexpen),
    path('adminDelexpen/', adminDelexpen),
    path('adminIncome/', adminIncome),
    path('adminDelincome/', adminDelincome),
    path('adminDayIncome/', adminDayIncome),
    path('adminEchartIncome/', adminEchartIncome),
    path('adminStore/', adminStore),
    path('adminAddstore/', adminAddstore),
    path('adminDelstore/', adminDelstore),
    path('adminEditstore/', adminEditstore),
    path('adminOther/', adminOther),
    path('adminAddother/', adminAddother),
    path('adminEditother/', adminEditother),
    path('adminDelsother/', adminDelsother),
    path('adminLogin/', adminLogin),
    path('pc-geetest/register/', get_geetest),
    path('adminRegister/', adminRegister),
]



