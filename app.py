# Піключаємо бібліотеки
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
import psycopg2

# Стартуємо flask
app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

# Клас користувач з полями(ім'я і т.д.)
class User:
# Конструктор створення екземпляру класа (об'єкта)
    def __init__(self,name,surname,lastname,group,group_id):
        self.name = name
        self.surname = surname
        self.lastname = lastname
        self.group = group
        self.group_id = group_id
        
# Створення єкземпляру підключення до бази даних
def getConnection():
    return psycopg2.connect(dbname='ping', user='postgres', password='root', host='localhost')

# Коміт та закритя екземпляру підключення до БД
def commitAndClose(connection):
    connection.commit()
    connection.close()

# Отримання всіх користувачів з БД
def getAllUsers():
    try:
        conn =  getConnection()
        cursor = conn.cursor()
        cursor.execute("select * from public.users")
        users = cursor.fetchall()
        commitAndClose(conn)
        return users
    except:
        print('Can`t establish connection to database')

# Збереження нового користувача до БД
def save(user):
    try:
        conn =  getConnection() 
        cursor = conn.cursor()
        cursor.execute("INSERT INTO public.users(name, surname, lastname, user_group, group_id) values(%s, %s, %s, %s, %s);",(user.name, user.surname, user.lastname ,user.group, user.group_id))
        commitAndClose(conn)

    except:
        print('Can`t establish connection to database')

# Зміна користувача в БД
def update(user):
    try:
        conn =  getConnection() 
        cursor = conn.cursor()
        print(user.id + " " + user.name + " " + user.surname + " " + user.lastname + " " + user.group + " " + user.group_id)
        cursor.execute("UPDATE public.users set name = '" + user.name +"', surname = '" + user.surname + "', lastname = '" + user.lastname + "', user_group = '" + user.group + "', group_id = '"+ user.group_id + "' where id =" + user.id +"")
        commitAndClose(conn)

    except:
        print('Can`t establish connection to database')

# Видалення користувача з БД
def delete(id):
    try:
        conn =  getConnection() 
        cursor = conn.cursor()
        cursor.execute("DELETE FROM public.users where id = "+ id +" ")
        commitAndClose(conn)
    except:
        print('Can`t establish connection to database')
    
    
# Контролер отримання всіх користувачів
@app.route("/")
def getUsers():
    users = getAllUsers()
    return render_template('index.html',users = users)

# Контроллер додавання нового користувача до БД
@app.route("/add" , methods=['POST'])
def saveUser():
    user = User(request.form['name'], request.form['surname'], request.form['lastname'], request.form['group'] , request.form['group_id'])
    save(user)
    return redirect("/")

# Контроллер зміни існуючого користувача в БД
@app.route("/update/<id>" , methods=['POST'])
def updateUser(id):
    user = User(request.form['name'], request.form['surname'], request.form['lastname'], request.form['group'] , request.form['group_id'])
    user.id = id
    update(user)
    return redirect("/")

# Контроллер видаленя користувача з БД
@app.route("/delete/<id>" , methods=['POST'])
def deleteUser(id):
    delete(id)
    return redirect("/")
