import zipfile

from flask import Blueprint, render_template, Flask, request, redirect, session, json
import os
import uuid
from ..utils import helper
import datetime
import shutil

ind = Blueprint('ind', __name__)


@ind.before_request
def process_request():
    if not session.get("user_info"):
        return redirect("/login")

    return None


@ind.route('/index/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

#用户列表
@ind.route('/user_list/', methods=['GET', 'POST'])
def user_list():
    data_list = helper.fetch_all("SELECT id,user,nickname FROM userinfo", [])

    return render_template('user_list.html', data_list=data_list)

#文件列表
@ind.route('/files_list/', methods=['GET', 'POST'])
def files_list():
    data_list = helper.fetch_all("SELECT id,file_name,target_path,ctime FROM files_upload", [])

    return render_template('files_list.html', data_list=data_list)

#上传文件列表页
@ind.route('/detail/<int:nid>')
def detail(nid):
    data_list = helper.fetch_all("SELECT id,file_name,target_path,ctime FROM files_upload where user_id=%s", (nid,))
    user_name = helper.fetch_one("SELECT nickname FROM userinfo WHERE id=%s", (nid,))
    # record_list = helper.fetch_all("SELECT id,line,ctime,note_line,blank_line,actual_line,actual_line_rate,note_line_rate,blank_line_rate,file_name FROM record where user_id=%s",(nid,))

    return render_template('detail.html', data_list=data_list, user_name=user_name,nid=nid)

#上传文件统计页
@ind.route('/files_detail/<int:nid>')
def files_detail(nid):
    record_list = helper.fetch_all("SELECT id,line,ctime,note_line,blank_line,actual_line,actual_line_rate,note_line_rate,blank_line_rate,file_name FROM record where file_id=%s",
        (nid,))
    print("record_list", record_list)
    files_id = helper.fetch_one("SELECT user_id FROM files_upload WHERE id=%s", (nid,))
    user_name = helper.fetch_one("SELECT nickname FROM userinfo WHERE id=%s", (files_id['user_id'],))
    return render_template('files_detail.html', record_list=record_list, user_name=user_name)

#上传文件
@ind.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == "GET":
        return render_template('upload.html')
    from werkzeug.datastructures import FileStorage
    file_obj = request.files.get('code')

    # 1. 检查上传文件后缀名
    name_ext = file_obj.filename.rsplit('.', maxsplit=1)
    if len(name_ext) != 2:
        return "请上传zip压缩文件"
    if name_ext[1] != 'zip':
        return "请上传zip压缩文件"

    # 2. 接收用户上传文件,并写入到服务器本地.
    # file_path = os.path.join("zips", file_obj.filename)
    # 从file_obj.stream中读取内容，写入到文件
    # file_obj.save(file_path)

    # 3. 解压zip文件
    import shutil
    # 通过open打开压缩文件，读取内容再进行解压。
    # shutil._unpack_zipfile(file_path, 'files')

    target_path = os.path.join('files', str(uuid.uuid4()))
    shutil._unpack_zipfile(file_obj, target_path)

    ctime = datetime.date.today()
    file_name = file_obj.filename.split('.')[0]
    helper.insert("insert into files_upload(file_name,target_path,user_id,ctime)values(%s,%s,%s,%s)",
                  (file_name, target_path, session['user_info']['id'], ctime))

    return "上传成功"

#文件分析计算
@ind.route('/file_analysis/<int:nid>', methods=['GET', 'POST'])
def file_analysis(nid):
    file_path = helper.fetch_all("SELECT target_path FROM files_upload where id=%s", (nid,))
    # str = 'There are %s, %s, %s on the table.' % (fruit1, fruit2, fruit3)
    # print("file_path:",file_path)
    file_sqlname = helper.fetch_all("SELECT file_name,id FROM files_upload where id=%s", (nid,))
    user_id_sql = helper.fetch_all("SELECT user_id FROM files_upload where id=%s", (nid,))
    user_id_sql = user_id_sql[0]['user_id']
    print("user_id_sql",user_id_sql)
    target_dir = file_path[0]['target_path']
    TARGET_PATH = './' + target_dir
    total_num = 0
    note_line = 0
    blank_line = 0
    actual_line = 0
    for base_path, folder_list, file_list in os.walk(TARGET_PATH):

        for file_name in file_list:
            file_path = os.path.join(base_path, file_name)
            file_ext = file_path.rsplit('.', maxsplit=1)
            if len(file_ext) != 2:
                continue
            if file_ext[1] != 'py':
                continue
            file_num = 0

            with open(file_path, 'rb') as f:

                for line in f:
                    line = line.strip()

                    if not line:
                        blank_line += 1
                        continue
                    if line.startswith(b'#') or line.startswith(b'""""""'):
                        note_line += 1
                        continue

                    file_num += 1
            total_num += file_num

    actual_line = total_num - note_line - blank_line

    # 实际代码比率
    actual_rate = 0
    # 注释比率
    note_rate = 0
    # 空行比率
    black_rate = 0
    # 实际代码比率
    if total_num != 0:

        actual_rate = float(actual_line / total_num)
        actual_rate = float('%.2f' % actual_rate)
        # 注释比率

        note_rate = float(note_line / total_num)
        note_rate = float('%.2f' % note_rate)
        # 空行比率
        black_rate = float(blank_line / total_num)
        black_rate = float('%.2f' % black_rate)
    else:
        actual_rate = 0
        note_rate = 0
        black_rate = 0


    file_name_sql = file_sqlname[0]['file_name']

    ctime = datetime.date.today()
    helper.insert("insert into record(line,ctime,note_line,blank_line,actual_line,actual_line_rate,note_line_rate,blank_line_rate,file_name,file_id,user_id)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(total_num, ctime,note_line,blank_line,actual_line,actual_rate,note_rate,black_rate,file_name_sql,nid,user_id_sql))



    return "统计成功"
#代码统计可视化
@ind.route('/visual/<int:nid>', methods=['GET', 'POST'])
def visual(nid):
    visual_data = helper.fetch_all("SELECT line,ctime,note_line,blank_line,actual_line,actual_line_rate,note_line_rate,blank_line_rate,file_name FROM record where user_id=%s", (nid,))
    # print("visual_data:",visual_data,type(visual_data))

    # ret = json.dumps(visual_data, ensure_ascii=False)



    ret = json.dumps(visual_data)
    # print("ret:",ret)
    return render_template('files_chart.html',ret=ret)