# app.py 

# Auther: hhh5460
# Time: 2018/10/05
# Address: DongGuan YueHua

from functools import wraps
from flask import Flask, request, render_template, redirect, url_for, flash, session,jsonify, make_response
import jwt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_
import os

app = Flask(__name__,static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL','sqlite:///' + os.path.join(app.root_path, 'data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = '\xc9ixnRb\xe40\xd4\xa5\x7f\x03\xd0y6\x01\x1f\x96\xeao+\x8a\x9f\xe4'
db = SQLAlchemy(app)
JWT_secret="NuAa"


############################################
# 数据库
############################################

# 定义ORM
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return '<User %r>' % self.username
        

# 创建表格、插入数据
@app.before_first_request
def create_db():
    db.drop_all()  # 每次运行，先删除再创建
    db.create_all()
    
    admin = User(username='admin', password='nuaactf{haojiGuoGuoTql}', email='admin@example.com')
    db.session.add(admin)

    guestes = [User(username='guest', password='guest', email='guest@example.com')]
    db.session.add_all(guestes)
    db.session.commit()
    

############################################
# 辅助函数、装饰器
############################################

# 登录检验（用户名、密码验证）
def valid_login(username, password):
    user = User.query.filter(and_(User.username == username, User.password == password)).first()
    if user:
        return True
    else:
        return False


# 注册检验（用户名、邮箱验证）
def valid_regist(username, email):
    user = User.query.filter(or_(User.username == username, User.email == email)).first()
    if user:
        return False
    else:
        return True

# 登录
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        username=""
        jwt_str=request.cookies.get('JWT')
        if len(jwt_str) > 10:
            username=jwt.decode(jwt_str, JWT_secret, algorithms=['HS256'])["username"]
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login', next=request.url)) # 
    return wrapper


############################################
# 路由
############################################

# 1.主页
@app.route('/')
def home():
    username=""
    jwt_str=request.cookies.get('JWT')
    if jwt_str:
        if len(jwt_str)>10:
            username=jwt.decode(jwt_str, JWT_secret, algorithms=['HS256'])["username"]
    response = make_response(render_template('home.html', username=username))
    response.headers["hint"] = "Flag-is-admins-password"
    return response

# 2.登录
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            flash("成功登录！")
            response = make_response(redirect('/'))
            response.set_cookie('JWT', jwt.encode({'username':request.form.get('username')}, JWT_secret, algorithm='HS256'))
            return response
        else:
            error = '错误的用户名或密码！'

    return render_template('login.html', error=error)

# 3.注销
@app.route('/logout')
def logout():
    response = make_response(redirect('/'))
    response.set_cookie('JWT', '')
    return response

# 4.注册
@app.route('/regist', methods=['GET','POST'])
def regist():
    error = None
    if request.method == 'POST':
        if request.form['password1'] != request.form['password2']:
            error = '两次密码不相同！'
        elif valid_regist(request.form['username'], request.form['email']):
            user = User(username=request.form['username'], password=request.form['password1'], email=request.form['email'])
            db.session.add(user)
            db.session.commit()
            
            flash("成功注册！")
            return redirect(url_for('login'))
        else:
            error = '该用户名或邮箱已被注册！'
    
    return render_template('regist.html', error=error)

# 5.个人中心
@app.route('/panel')
@login_required
def panel():
    username=""
    jwt_str=request.cookies.get('JWT')
    if len(jwt_str) > 10:
        username=jwt.decode(jwt_str, JWT_secret, algorithms=['HS256'])["username"]
    user = User.query.filter(User.username == username).first()
    return render_template("panel.html", user=user)



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug = False)