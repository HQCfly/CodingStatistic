import pymysql
from django.http import HttpResponse
from flask import Blueprint,render_template,Flask,request,redirect,session
from ..utils.md5 import md5
from ..utils import helper
# from geetest import GeetestLib


account = Blueprint('account',__name__)

@account.route('/login/',methods = ['GET','POST'])

def login():
    if request.method == 'POST':
        username = request.form.get('user')
        password = request.form.get('pwd')

        pwd_md5 = md5(password)
        data = helper.fetch_one("select id,nickname from userinfo where user=%s and pwd=%s",(username,pwd_md5))

        if not data:
            return render_template('login.html',error = '用户名密码错误')

        session['user_info'] = {'id':data['id'],'nickname':data['nickname']}

        return redirect('/index/')
    return render_template('login.html')


@account.route('/logout')
def logout():
    if 'user_info' in session:
        del session['user_info']

    return redirect('/login')