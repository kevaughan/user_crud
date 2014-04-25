from flask import Flask, request, g,render_template,url_for, redirect, flash

import sqlite3, os

SECRET_KEY = "the global object 'g' needs this"

app = Flask(__name__)

app.config.from_object(__name__)

# database method, which is triggered

# before each request

def connect_db():

 return sqlite3.connect('./users.db')

@app.before_request

def before_request():

 g.db = connect_db()

@app.teardown_request

def teardown_request(exception):

 g.db.close()

@app.route('/create', methods=['POST'])

def create():

 fullname = request.form['fullname']

 username = request.form['username']

 photo = request.form['photo']

 g.db.execute('insert into users (fullname, username, photo) values (?, ?, ?)',[fullname, username, photo])

 g.db.commit()

 flash('New entry was successfully posted')

 return redirect(url_for('read'))

@app.route('/read')

@app.route('/')

def read():

 cur = g.db.execute('select fullname,username,photo from users order by id desc')

 users = [dict(fullname=row[0], username=row[1],photo=row[2]) for row in cur.fetchall()]

 return render_template('users.html',users=users)

@app.route('/update')

def update():

 # we will add this code later

 pass

@app.route('/delete')

def delete():

 # we will add this code later

 pass

if __name__ == "__main__":

 app.debug = True

 app.run(port=8080,host='0.0.0.0')