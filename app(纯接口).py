# -*- coding: utf-8 -*-
from flask import Flask, render_template, abort, request, make_response,jsonify
from flask import send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER='upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['txt','png','jpg','xls','JPG','PNG','xlsx','gif','GIF'])

# 用于判断文件后缀
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

# 上传文件
@app.route('/upload',methods=['POST'],strict_slashes=False)
def api_upload():
    if request.method == 'POST':
        f=request.files['file']  # 从表单的file字段获取文件，myfile为该表单的name值
        userid = request.form.get('userid')
        file_dir=os.path.join(basedir,app.config['UPLOAD_FOLDER'],userid)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        if f and allowed_file(f.filename):  # 判断是否是允许上传的文件类型
            file = f.filename
            f.save(os.path.join(file_dir,file))  #保存文件到upload目录
            data = {'msg':'success','status_code':200}
            return jsonify(data)
        else:
            data = {'msg':'fail','status_code':300}   # 文件格式不正确
            return jsonify(data)
    return jsonify({'msg':'fail','status_code':400})  # 请求方式不正确

@app.route('/download', methods=['GET'])
def download():
    if request.method =="GET":
        filename = request.values.get('filename')
        userid = request.values.get('userid')
        file_path = os.path.join(basedir,app.config['UPLOAD_FOLDER'],userid)
        # 解决中文乱码问题
        response = make_response(send_from_directory(file_path, filename, as_attachment=True))
        response.headers["Content-Disposition"] = "attachment; filename{}".format(filename.encode().decode('latin-1'))
        return response
    return abort(404)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8067,debug=True)
