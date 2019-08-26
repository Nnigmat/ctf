from flask import Flask, request, redirect
from tasks import task1 as t1, task2 as t2, task3 as t3, check
import os
import sqlite3

if not os.path.exists('db'):
    os.mknod('db')

conn = sqlite3.connect('db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''
        CREATE TABLE if not exists users (login text primary key, task1 int default 0,
         task2 int default 0 ,task3 int default 0 , task4 int default 0)
''')
conn.commit()

app = Flask(__name__)
index_html = open('html/index.html').read()

@app.route('/')
def index():
    return index_html

@app.route('/task1', methods=['GET', 'POST'])
def task1():
    if request.method == 'GET':
        return '''
        <form method="post">
            <input name="login" placeholder="Login">
            <input name="password" placeholder="Password">
            <button type="submit">Submit</button>
        </form>
               '''
    else:
        login = request.form.get('login')
        password = request.form.get('password')

        result = t1(login, password)
        return f'{"Invalid password" if not result else "Your flag: " + result } dear friend'

@app.route('/task2', methods=['GET', 'POST'])
def task2():
    if request.method == 'GET':
        return '''
        <head><title>4 цифры</title></head>
        <body>
        <form method="post">
            <input name="login" placeholder="Login">
        <div hidden="true">Eto ne login</div><div hidden="true">Eto ne login</div><div hidden="true">Eto ne login</div><div hidden="true">Eto ne
        login</div><div hidden="true">Eto ne login</div><div hidden="true">Eto ne login</div><div hidden="true">Eto ne login</div><div
        hidden="true">Eto ne login</div><div hidden="true">Eto ne login</div><div hidden="true">Eto ne login</div><div hidden="true">Eto ne
        login</div><div hidden="true">Eto ne login</div><div hidden="true">Eto ne login</div><div hidden="true">Eto ne login</div><div
        hidden="true">Eto ne login</div><div hidden="true">Eto ne login</div><div hidden="true">Eto ne login</div><div hidden="true">E<div
        hidden="true">Eto ne login</div><!-- Salavat udoli pliz, chtob ne spalit' login: "Cruassilio"--><div hidden="true">Eto ne login</div><!--
        Salavat udoli pliz, chtob ne spalit' login: "Cruassilio"--><div hidden="true">Eto ne login</div><!-- Salavat udoli pliz, chtob ne spalit'
        login: "Cruassilio"--><div hidden="true">Eto ne login</div><!-- Salavat udoli pliz, chtob ne spalit' login: "Cruassilio"--><div
        hidden="true">Eto ne login</div><!-- Salavat udoli pliz, chtob ne spalit' login: "Cruassilio"--><div hidden="true">Eto ne login</div><!--
        Salavat udoli pliz, chtob ne spalit' login: "Cruassilio"--><div hidden="true">Eto tochno ne login</div><!-- Salavat udoli pliz, chtob ne spalit' login: "Cruassilio"--><div hidden="true">Eto ne login</div><!-- Salavat udoli pliz, chtob ne spalit' login: "Cruassilio"-->to ne login</div><div hidden="true">Eto ne login</div><div hidden="true">Eto ne login</div>
                    <div hidden="true">Eto ne login</div>
            <input name="password" placeholder="Password">
            <button type="submit">Submit</button>
        </form>
        </body>
               '''
    else:
        login = request.form.get('login')
        password = request.form.get('password')

        result = t2(login, password)
        return f'{"Invalid password" if not result else "Your flag: " + result } dear friend'

@app.route('/task3', methods=['GET'])
def task3():
    result = t3(request.headers.get('User-Agent'))
    return f'{"Wrong device " if not result else "Your flag: " + result } dear friend'

@app.route('/wp-content/themes/twentyeleven/content-aside.php')
@app.route('/wp-admin/index-extra.php')
@app.route('/wp-admin/network/setup.php')
@app.route('/wp-content/themes/twentyeleven/images/headers/wheel-thumbnail.jpgkj')
@app.route('/wp-content/themes/twentyeleven/content-aside.php')
@app.route('/wp-content/themes/twentyeleven/images/headers/wheel-thumbnail.jpg')
@app.route('/administrator/components/com_config/views/close/index.html')
@app.route('/install.php')
@app.route('/modules/simpletest/tests/upgrade/upgrade.taxonomy.test')
def gorin():
    return '''
    <head><title>Вы кто такие? Я вас не звал</title></head>
    <body>
    <img
    src="https://memepedia.ru/wp-content/uploads/2017/12/%D0%BC%D0%B5%D0%BC%D1%8B-%D0%B3%D0%B5%D0%BD%D0%BD%D0%B0%D0%B4%D0%B8%D0%B9-%D0%B3%D0%BE%D1%80%D0%B8%D0%BD-7.jpg"/>
    </body>'''

@app.route('/wp-content/themes/twentyeleven/content-aside.php')
def task4_1():
    return "1/4 flag: hvatit'"

@app.route('/administrator/components/com_admin/script.php')
def task4_2():
    return "2/4 flag: dvigat'"

@app.route('/administrator/components/com_installer/controller.php')
def task4_3():
    return '3/4 flag: svoimi'

@app.route('/administrator/components/com_content/models/fields/modal/index.html')
def task4_4():
    return '4/4 flag: TABURETKAMI'

@app.route('/flag', methods=['GET', 'POST'])
def flag():
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute('''
            select * from users;
        ''')
        table = '\n'.join([f'{i[0]}: {i[1]} {i[2]} {i[3]} {i[4]}' for i in cursor.fetchall()])
        return '''
                <form method="post">
                    <input name="login" placeholder="Login">
                    <input name="flag" placeholder="Flag">
                    <button type="submit">Submit</button>
                </form>
                ''' + table 
                
    else:
        login = request.form.get('login')
        key = request.form.get('flag')
        result = check(key)
        if result != 0:
            cursor.execute(f'''
            insert or ignore into users (login, task{result}) values(?,1)
            ''', [login])
            conn.commit()
            cursor.execute(f'''update users set task{result}=1 where login=?
            ''', [login])
            conn.commit()
        return redirect('/flag')


