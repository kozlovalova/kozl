from flask import Flask 
from flask import render_template
import sqlite3
from flask import request

app = Flask(__name__)

connection = sqlite3.connect('my_database.db' , check_same_thread=False)
cursor = connection.cursor() 

def productDB(): 
    listDB = cursor.execute('SELECT * FROM product')
    return listDB.fetchall()

def one_productDB(id): 
    listDB = cursor.execute('SELECT * FROM product WHERE id='+id)
    result = listDB.fetchall()
    if result:
        # Преобразуем кортеж в словарь для удобства использования в шаблоне
        product = {
            'id': result[0][0],
            'name': result[0][1],
            'description': result[0][2],
            'price': result[0][3],
            'image_url': result[0][4],
            'category': result[0][5] if len(result[0]) > 5 else '',
            'size': result[0][6] if len(result[0]) > 6 else ''
        }
        return product
    return None

@app.route('/') #главная страница
def index ():
    shop= productDB()
    return render_template("index.html", shop = shop)

@app.route('/zaiavka/<id>') # Обработчик заявки
def zaiavka(id):
    tovar = one_productDB(id)
    return render_template ('zaivka.html',tovar= tovar) 


    

@app.route('/about') #о нас
def about():
    return render_template("about.html")



@app.route('/catalog') #каталог
def catalog ():
    return render_template("catalog.html")

@app.route('/account') #аккауент
def account ():
    return render_template("account.html")

@app.route('/shop now') #купить сейчас 
def shop_now ():
    return render_template("shop now.html")

@app.route('/contact') #контакты 
def contact():
    return render_template("contact.html")

@app.route('/user/<username>')
def user_profile(username):
    return render_template("index.html", name = username)

# Логин
@app.route("/login")
def login():
    return render_template("login.html", title="Вход и регистрация")


@app.route('/submit_order', methods=['POST'])
def submit_order():
    # Получаем данные из формы
    product_id = request.form.get('product_id')
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    address = request.form.get('address')
    quantity = request.form.get('quantity')
    
    # Здесь можно сохранить заказ в базу данных или отправить по email
    print(f"Новый заказ: Товар {product_id}, {name}, {phone}, {email}, {address}, количество: {quantity}")
    
    # Пока просто вернем сообщение об успехе
    return "Заявка успешно отправлена! Мы свяжемся с вами в ближайшее время."


@app.route('/search')
def search():
    query = request.args.get('q', '')
    
    # Полный список товаров с изображениями
    all_products = [
        
        {
            "name": " Кофта серая на завязках ", 
            "price": "699",
            "image": "https://i.pinimg.com/1200x/cd/a5/4e/cda54e4527eb191cd31be17f79363ea3.jpg"  
        },
        {
            "name": "Футболка белая базовая ", 
            "price": "399",
            "image": "https://i.pinimg.com/1200x/ee/8c/ee/ee8ceebeb3584cac09690544b9ec522c.jpg"
        },
        {
            "name": "Топ коричневый с рюшками", 
            "price": "299",
            "image": "https://i.pinimg.com/1200x/14/55/af/1455afccff410f338edc7385906fb3fd.jpg"
        },
        {
            "name": "Брюки серые базовые", 
            "price": "499",
            "image": "https://i.pinimg.com/736x/97/ba/c6/97bac640c06cdfea0fee273858f2be0e.jpg"
        },
        {
            "name": "Рубашка белая в полоску", 
            "price": "499",
            "image": "https://i.pinimg.com/1200x/27/27/c4/2727c4282a5b4be2eb304d08d550311b.jpg"
        },
        {
            "name": "Кардиган длинный серый ", 
            "price": "799",
            "image": "https://i.pinimg.com/736x/54/e4/80/54e480f81723c4913ef3c0c9d990dea8.jpg"
        },
        {
            "name": "Туфли черные", 
            "price": "399",
            "image": "https://i.pinimg.com/736x/a5/21/5e/a5215e6c89e1f607bfe8774ed072361b.jpg"
        },
        {
            "name": "Туфли черные ", 
            "price": "399",
            "image": "https://i.pinimg.com/736x/f0/7f/92/f07f92d8765859f5d41b76d26791fdee.jpg"
        },
        {
            "name": "Сумка черная маленькая", 
            "price": "799",
            "image": "https://i.pinimg.com/1200x/fa/29/fa/fa29fa94645ec6568c66d6cd610d9a3e.jpg"
        } 
    ]

    # Фильтрация товаров по запросу
    if query:
        filtered_products = [product for product in all_products 
                           if query.lower() in product['name'].lower()]
    else:
        filtered_products = []
    
    return render_template('search.html', 
                         query=query, 
                         products=filtered_products)


if __name__ == '__main__':  #точка входа нашей программы
    print("сервер запущен") #для проверки
    app.run (debug=True)
 