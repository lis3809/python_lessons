"""
Задание 1:
Рост космонавта не может быть больше 180 см и меньше 160 см.
Напишите программу, которая считывает рост претендентов
в отряд космонавтов до тех пор, пока не будет введен «!».
А затем выводит на первой строчке количество подходящих
кандидатур, а на второй строке – минимальный и максимальный
рост участников, отобранных в новый отряд космонавтов.
"""
# heights = []
# while True:
#     height = input("Введите рост космонавта (в см) или введите '!' для завершения: ")
#     if height == '!':
#         break
#     height = int(height)
#     if height >= 160 and height <= 180:
#         heights.append(height)
#
# if len(heights) == 0:
#     print("Нет подходящих кандидатур")
# else:
#     print("Количество подходящих кандидатур:", len(heights))
#     print("Минимальный рост участников:", min(heights), "см")
#     print("Максимальный рост участников:", max(heights), "см")


"""
Задание 2:
Напишите программу для генерации горизонтальных столбчатых диаграмм.
Список значений:
mylist = [3, 7, 1, 10, 8, 5]
"""

# 1 вариант
# mylist = [3, 7, 1, 10, 8, 5]
# for i in range(len(mylist)):
#     for x in range(mylist[i]):
#         print("*", end='')
#     print()

# 2 вариант
# mylist = [3, 7, 1, 10, 8, 5]
# for i in mylist:
#     print("*" * i)


"""
Задание 3:
Пользователь вводит одно число - высота пирамиды.
"""
# height = int(input("Введите высоту пирамиды: "))
# for i in range(1, height + 1):
#     print(" " * (height - i) + "*" * (2 * i - 1))

"""
Задание 4:
Напишите программу для генерации вертикалных столбчатых диаграмм в рамке.
Список значений:
mylist = [3, 7, 1, 10, 8, 5]
"""

# mylist = [3, 7, 1, 10, 8, 5]  # данные для столбчатой диаграммы
# max_num = max(mylist)
#
# print("+" + "-" * (max_num * 2) + "+")
# for i in range(max_num, 0, -1):
#     row = ""
#     for num in mylist:
#         if num >= i:
#             row += " * "
#         else:
#             row += "   "
#     print("|" + row + "|")
# print("+" + "-" * (max_num * 2) + "+")

"""
Задание 5:
Реализуйте шифр Цезаря
"""
# 1 вариант
# text = "Hello, World!"
# shift = 5
#
# encrypted_text = ""
# for char in text:
#     encrypted_text += chr(ord(char) + shift)
#
# print("Зашифрованный текст:", encrypted_text)


# 2 вариант
# text = "Hello, World!"
# shift = 5
#
# encrypted_text = ""
# for char in text:
#     if char.isalpha():
#         if char.islower():
#             encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
#         elif char.isupper():
#             encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
#     else:
#         encrypted_text += char
#
# print("Зашифрованный текст:", encrypted_text)
