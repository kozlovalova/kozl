import sqlite3

#создаем подключение к базе данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

def productDB(): #возвращать данные про товары
    listDB = cursor.execute('SELECT * FROM product')
    return listDB.fetchall()

