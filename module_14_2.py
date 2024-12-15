import sqlite3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     username TEXT NOT NULL,
#     email TEXT NOT NULL,
#     age INTEGER,
#     balance INTEGER NOT NULL
# )
#  ''')
# #Создание
# for i in range(10):
#      cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{i}', f'example{i}@gmail.com',  f'{i*10}', '1000'))


# #Изменение
# for i in range(1, 11, 2):
#     cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (500 , f'User{i}'))

# #Удаление
# for i in range(1, 11, 3):
#     cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{i}', ))


# #выборка
# cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))
# users = cursor.fetchall()
# for user in users:
#     print(f'Имя:{user[0]} | Почта:{user[1]} | Возраст:{user[2]} | Баланс:{user[3]}')

# ###########
# cursor.execute('SELECT * FROM Users')
# users = cursor.fetchall()
# for user in users:
#     print(f'username:{user[1]} | email:{user[2]} | age:{user[3]} | balance:{user[4]}')

cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

#Подсчёт 
cursor.execute('SELECT COUNT(*) FROM Users')
total = cursor.fetchone()[0]
print(total)

#Подсчёт 
cursor.execute('SELECT SUM(balance) FROM Users')
total2 = cursor.fetchone()[0]
print(total2)

# Средний баланс пользователей в БД 
cursor.execute('SELECT AVG(balance) FROM Users')
total3 = cursor.fetchone()[0]
print(total3) # средняя сумма через встроенную функцию
print(total2/total)


connection.commit()
connection.close()