from flask import render_template, request, session, redirect, url_for
from .models import *
import requests as rq
import json, os

data_user = UserModel('user')
data_item = style('style')

def index():
    return render_template('root/index.html')

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        #do authentications
        res = data_user.authUser(username, password)
        if res != 'N' and res != '':
            session['user_id'] = res
            return 'User <{user_id}:{user}> is successfully logged in. Go to <a href="http://localhost:5000/">main</a>. <a href="logout">Logout</a>'.format(user_id=res ,user=username)
        elif res == 'N':
            return "Database Error"
        else:
            return "Record not found"
    else:
        if 'user_id' in session:
            res = data_user.authUserQuick(session['user_id'])
            if res != '':
                return 'User <{user_id}:{user}> is successfully logged in. Go to <a href="http://localhost:5000/">main</a>. <a href="logout">Logout</a>'.format(user_id=session['user_id'] ,user=res)
            else:
                session.pop('user_id')
                return render_template('root/login.html')
        return render_template('root/login.html')

def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        age = int(request.form['age'])
        gender = request.form['gender']

        res = data_user.createUser(username, password, age, gender)

        if res == 'SUCCESS':
            return 'User {user} is successfully registered. Go to <a href="http://localhost:5000/">main</a>'.format(user=username)
        elif res == 'NOT_UNIQUE_USERNAME':
            return 'Invalid Username. <a href="http://localhost:5000/register">Try again</a>'
        else:
            return 'User creation unsuccessful, please <a href="http://localhost:5000/register">Try again</a>.'
    else:
        return render_template('root/register.html')

def upload():
    if request.method == 'POST':
        img = request.files["filename"]
        print(img)
        img.save('file.png')

    # Path of image (jpg/jpeg/png)
    file = str(os.path.abspath("download1.jpg"))

    # url name
    url = "https://face.recoqnitics.com/analyze"
    accessKey = "c2da496b4f1922f1274f"
    secretKey = "e792831aa0aa4f33af651a083f8dd200fc0ab383"

    # access_key and secret_key
    data = {'access_key': accessKey, 'secret_key': secretKey}

    filename = {'filename': open(file,'rb')}
    r = rq.post(url, files = filename, data=data)
    print(r.content)
    content = json.loads(r.content)

    print(content)

    return r.content

def logout():
    session.pop('user_id')
    return redirect(url_for('root.login'))

def search():
    if request.method == 'POST':
        #null
        return None
    else:
        return render_template('root/search.html')

def upload_search():
    if request.method == 'POST':
        img = request.files["filename"]
        img.save('file.png')

    # Path of image (jpg/jpeg/png)
    file = str(os.path.abspath("download1.jpg"))

    # url name
    url = "https://face.recoqnitics.com/analyze"
    accessKey = "c2da496b4f1922f1274f"
    secretKey = "e792831aa0aa4f33af651a083f8dd200fc0ab383"

    # access_key and secret_key
    data = {'access_key': accessKey, 'secret_key': secretKey}

    filename = {'filename': open(file,'rb')}
    r = rq.post(url, files = filename, data=data)
    content = json.loads(r.content)

    file = str(os.path.abspath("90s.jpg"))
    filename = {'filename': open(file,'rb')}
    url = "https://fashion.recoqnitics.com/analyze"
    p = rq.post(url, files = filename, data=data)
    print(p.content)
    content_p = json.loads(p.content)

    content.update(content_p)

    print(content)

    style = content["person"]["styles"][0]["styleName"]
    if(style=="Casual"):
        style = 1
    elif(style=="Bohemian"):
        style = 2
    elif(style=="Business"):
        style = 3
    elif(style=="Elegant"):
        style = 4
    elif(style=="Romantic"):
        style = 5
    elif(style=="Vintage"):
        style = 6
    elif(style=="Eclectic"):
        style = 7
    elif(style=="Rocker"):
        style = 8
    elif(style=="Sexy"):
        style = 9
    elif(style=="Denim"):
        style = 10
    elif(style=="Outdoor"):
        style = 11
    elif(style=="90s"):
        style = 12
    res = data_item.searchStyle(style)
    #do something with the result

    if(len(res)!=0):
        session['res'] = json.dumps(res)
        return json.dumps(res)
    return "Not Found"

def result():
    print(session['res'])
    result = json.loads(session['res'])
    result = [a[0] for a in result]
    print(result)
    session.pop('res')
    return render_template('root/result.html', results=result)