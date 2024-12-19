import sqlite3

def initiate_db():
    connection = sqlite3.connect('DB_module_14_5.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );
    ''')

    connection.commit()
    connection.close()

def add_user(username, email, age):
    connection = sqlite3.connect('DB_module_14_5.db')

    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (f'{username}', f'{email}', age, 1000))

    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect('DB_module_14_5.db')

    cursor = connection.cursor()
    check_user = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    data_ = check_user.fetchone()
    connection.close()

    if data_ is None:
        return True
    else:
        return False

def check_db(id, title, description, price):
    connection = sqlite3.connect('DB_module_14_5.db')
    cursor = connection.cursor()

    check_db = cursor.execute('SELECT * FROM Products WHERE title=?', (title,))

    if check_db.fetchone() is None:
        cursor.execute(f'''
    INSERT INTO Products (id, title, description, price) VALUES('{id}', '{title}', '{description}', '{price}')
''')
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('DB_module_14_5.db')

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products WHERE id > ?', (0,))
    data_ = cursor.fetchall()
    connection.close()

    return data_


if __name__ == '__main__':
    initiate_db()
    check_db(1,'Продукт 1', 'описание 1', 100)
    check_db(2,'Продукт 2', 'описание 2', 200)
    check_db(3,'Продукт 3', 'описание 3', 300)
    check_db(4, 'Продукт 4', 'описание 4', 400)

    add_user('newuser', 'user@mail.ru', 33)