"""
Задание 1:
Дана строка '0123456789'.
Удалите из нее первый, пятый и последний символы.
Выведите результат на экран.
"""
# s = '0123456789'
# new_s = s[1:4] + s[6:9]
# print(new_s)

"""
Задание 2:
Дана строка 'QwErTyU'.
Выведите на экран каждый второй (строчный) символ
"""
# s = 'QwErTyU'
# new_s = s[1::2]
# print(new_s)

"""
Дана строка
'C:\\Users\\foto\\горы.jpg'
Выведите на экран расширение файла
"""

# s = 'C:\\Users\\foto\\горы.jpg'
# print(s[-3:])

"""
Задание 4
Напишите программу,
которая шифрует строку с помощью системы Юникод (ASCII table)
"""

# string = "Hello world!"
# for i in string:
#     print(ord(i), end=', ')

"""
2 вариант
"""
# string = "Hello world!"
# for i in range(len(string)):
#     if i < len(string) - 1:
#         print(ord(string[i]), end=', ')
#     else:
#         print(ord(string[i]))

"Ещё вариант"
# string = "Hello world!"
# encrypted_string = ''
# for char in string:
#     encrypted_char = chr(ord(char) + 3)  # сдвиг на 3 позиции вправо
#     encrypted_string += encrypted_char
# print(f'Encrypted string: {encrypted_string}')
