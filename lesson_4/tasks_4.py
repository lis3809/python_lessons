"""
Задание 1
Напишите программу, которая считывает три строки.
Если эти три строки: “красный”, “жёлтый”, “зелёный”
или “3”, “2”, “1”, то программа выводит “ПОЕХАЛИ”, если нет, то “СТОЙ”
"""
# Считываем три строки
# string1 = input("enter string1")
# string2 = input("enter string2")
# string3 = input("enter string3")
#
# # Проверяем условие
# if (string1 == "red" and string2 == "yellow" and string3 == "green") or (
#         string1 == "3" and string2 == "2" and string3 == "1"):
#     print("GO")
# else:
#     print("STOP")

"""
Задание 2
Этим летом ваш друг планирует на 2 месяца уехать в путешествие, 
но быть 2 месяца в одном городе он не хочет, 
также известно, 
что в том году он был в Париже и Берлине, и ему очень понравилось, 
поэтому он готов посетить снова эти города, 
но не два города (повторять прошлогодний трип скучно). 
Напишите программу на Пайтон, которая поможет другу ответить на вопрос “Подходит ли такая поездка?”

Пользователь вводит 2 строки (2 города)
"""

# Считываем две строки
# city1 = input("enter city1")
# city2 = input("enter city2")
#
# # Проверяем условие
# if (city1 == "Париж" or city1 == "Берлин") and (city2 == "Париж" or city2 == "Берлин"):
#     print("Не подходит")
# elif city1 == city2:
#     print("Не подходит")
# else:
#     print("Подходит")

"""
Задание 3
Камень. Ножницы. Бумага.

Напишите программу, которая считывает от пользователя 
его выбор (камень, ножницы, либо бумагу), 
затем от второго пользователя аналогично. 
После программа выводит результат (кто победил).
"""
# Считываем выборы от двух игроков
# player1 = input("Player 1")
# player2 = input("Player 2")
#
# Правила игры: камень побеждает ножницы, ножницы побеждают бумагу, бумага побеждает камень
# if player1 == player2:
#     print("Ничья!")
# elif ((player1 == "камень" and player2 == "ножницы") or
#       (player1 == "ножницы" and player2 == "бумага") or
#       (player1 == "бумага" and player2 == "камень")):
#     print("Игрок 1 победил!")
# else:
#     print("Игрок 2 победил!")

"""
Задание 4 (Бонусное)
Получите от пользователя целое число от 1 до 100.
Если число нечетное, выведите «Weird».
Если число четное и находится в диапазоне 
от 2 до 5, выведите «Not Weird»
Если число четное и находится в диапазоне 
от 6 до 20, выведите «Weird».
Если четное и больше 20, выведите «Not Weird».
"""

# n = int(input())
# if n % 2 != 0:
#     print('Weird')
# else:
#     if n >= 6 and n <= 20:
#         print('Weird')
#     else:
#         print('Not Weird')
