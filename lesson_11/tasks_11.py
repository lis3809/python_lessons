"""
Задание 1:
Напишите функцию, которая принимает координаты x и y точки
на плоскости и печатает “I”, “II”, “III”, “IV”.

"""

# def identify_quadrant(x, y):
#     if x > 0 and y > 0:
#         print("I")
#     elif x < 0 and y > 0:
#         print("II")
#     elif x < 0 and y < 0:
#         print("III")
#     elif x > 0 and y < 0:
#         print("IV")
#     else:
#         print("Point lies on the axis")
#
#
# # Пример использования
# identify_quadrant(3, 4)  # Вывод: I
# identify_quadrant(-3, 4)  # Вывод: II
# identify_quadrant(-3, -4)  # Вывод: III
# identify_quadrant(3, -4)  # Вывод: IV

"""
Задание 2:
Напишите функцию ask_password(), которая запрашивает у пользователя 
пароль и сверяет его со строкой, в которой записано слово “password”. 
Пользователю дается три попытки. Как только пароль совпал 
с правильным значением, функция должна выводить «Пароль принят» 
и игнорировать дальнейший ввод.

 Если с трех попыток пользователь не смог угадать пароль, 
 функция должна вывести на экран «В доступе отказано» и игнорировать 
 ввод новых паролей.
"""

# def ask_password():
#     password = "qwerty"
#     attempts = 3
#
#     while True:
#         if attempts > 0:
#             user_input = input("Введите пароль: ")
#
#             if user_input == password:
#                 print("Пароль принят")
#                 attempts = 0
#                 continue
#
#             else:
#                 attempts -= 1
#
#             if attempts == 0:
#                 print("В доступе отказано")
#
#
# ask_password()


"""
Задание 3:
У вас есть список продуктов.
Напишите функцию, которая проверяет наличие продукта 
в списке и отвечает пользователю покупать или нет.
Проверяемый продукт должен вводить пользователь.
Прорамма должна работать пока не введено слово "stop"
"""
# products = ['milk', 'coffee', 'apples', 'sugar', 'potato']
#
#
# def check_list(product):
#     if product in products:
#         print('buy')
#     else:
#         print('no money')
#
#
# while True:
#     my_prod = input('Введите продукт: ')
#
#     if my_prod == 'stop':
#         break
#
#     check_list(my_prod)
