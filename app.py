# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
import requests
import time

app = Flask(__name__)

# 学生数据（可后台导入Excel）
students = {
    "100001": {"name":"陈则名","class":"三年级二班","phone":"13800138000"},
    "100002": {"name":"李明","class":"一年级一班","phone":"13900139000"}
}

# 短信配置（互亿无线，中文模板）
SMS_API_URL = "http://api.v2.sms.com/send"
SMS_USER = "你的账号"
SMS_PASS = "你的密码"

def send_sms(phone, name):
    msg = f"【XX小学】您的孩子{name}已安全离校，请知悉。"
    try:
        requests.get(SMS_API_URL, params={
            "account": SMS_USER,
            "password": SMS_PASS,
            "phone": phone,
            "msg": msg
        })
    except:
        pass

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/admin')
def admin():
    return render_template("admin.html", students=students)

@app.route('/rfid', methods=['POST'])
def rfid():
    rid = request.form.get("rfid","").strip()
    if rid not in students:
        return jsonify({"code":-1,"msg":"未找到学生"})
    s = students[rid]
    send_sms(s["phone"], s["name"])
    return jsonify({
        "code":0,
        "msg":"成功",
        "data":s
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
