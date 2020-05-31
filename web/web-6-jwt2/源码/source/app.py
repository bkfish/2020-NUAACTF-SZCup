# -*- coding: utf-8 -*-  
from flask import Flask,session,redirect,url_for,request,render_template_string
import os
from datetime import timedelta
app = Flask(__name__)
app.config['SECRET_KEY']='admin'   #设置为24位的字符,每次运行服务器都是不同的，所以服务器启动一次上次的session就清除。
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=7) #设置session的保存时间。


#获取session
@app.route('/')
def get():
    if 'username' not in session:
        session.permanent=True  #默认session的时间持续31天
        session['username'] = 'guest'
        return 'You need become admin first <!--flag in /flag-->'
    elif session.get('username')== 'guest':
        return 'You need become admin first <!--flag in /flag-->'
    elif session.get('username')== 'admin':
        return redirect('./user?username=admin')
    return 'error'

@app.route('/user',methods=['GET'])
def user():
    if 'username' in session:
        if session.get('username')== 'admin':
            username = request.args.get("username")
            html = '''
                <h4>Welcome %s</h4>
            '''%(username)
            return render_template_string(html)
        redirect('/')
    return redirect('/')

if __name__ == '__main__':
    app.run('0.0.0.0',8000,debug=False)
