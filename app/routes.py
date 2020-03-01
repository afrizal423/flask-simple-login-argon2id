import pymysql, time
from app import app
from app.db_config import mysql
from flaskext.mysql import MySQL
from flask import jsonify, flash, request, redirect, url_for, session, g, render_template
from argon2 import PasswordHasher

ph = PasswordHasher()

#hanya untuk menghitung running time
@app.before_request
def before_request():
    g.request_start_time = time.time()
    g.request_time = lambda: "%.5fs" % (time.time() - g.request_start_time)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/login',methods=["GET","POST"])
def login():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password'].encode('utf-8')
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM users where email=%s",(email,))
		user = cursor.fetchone()
		if len(user) > 0:
			if ph.verify(user['password'], password) == True:
				# print(user)
				session['name'] = user['username']
				session['email'] = user['email']
				return redirect('/')
			else:
				return " password and email tidak sama"
		else:
			return "User tidak ditemukan"
	else:
		return render_template("login.html")

@app.route('/register', methods=["GET", "POST"])
def register():
	if request.method == 'GET':
		return render_template("register.html") 
	else:
		username = request.form['username']
		email = request.form['email']
		password = request.form['password'].encode('utf-8')
		hash_password = ph.hash(password)
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("INSERT INTO users (username, email, password) VALUES (%s,%s,%s)",(username,email,hash_password,))
		conn.commit()
		session['name'] = request.form['username']
		session['email'] = request.form['email']
		return redirect('/')

@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.clear()
    return render_template("home.html")
@app.route('/home/<name>')  

def home(name):  
   return 'Hello %s!' % name

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
		