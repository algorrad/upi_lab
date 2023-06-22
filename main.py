output = "Не цифра"
def convert_char_to_int(char):
    if char.isdigit():  # Проверяем, является ли символ цифрой
        return int(char)  # Преобразуем символ в целое число
    else:
        return output
#char = input("Введите символ: ")
#convert_char_to_int(char)
char = input("Введите символ: ")
result = convert_char_to_int(char)
print(result)

import sqlite3

# создаем подключение
con = sqlite3.connect("students.db")

# получаем курсор
cursor = con.cursor()
cursor.execute("SELECT DATA FROM zachetka")
results = cursor.fetchall()

# Вывод результатов
for row in results:
    data = row[0]  # Получение значения колонки "DATA"
    print(data)

# Закрытие курсора
cursor.close()

# Закрытие соединения
con.close()
