output = "Не цифра"
def convert_char_to_int(char):
    if char.isdigit():  # Проверяем, является ли символ цифрой
        return int(char)  # Преобразуем символ в целое число
    else:
        return output  # Если символ не является цифрой, возвращаем None или можно выбрать другое значение по умолчанию
#char = input("Введите символ: ")
#convert_char_to_int(char)
char = input("Введите символ: ")
result = convert_char_to_int(char)
print(result)