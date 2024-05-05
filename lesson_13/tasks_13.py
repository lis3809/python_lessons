"""
Задание 1:
Шахматное поле
Напишите программу, которая рисует на холсте размера 400х400
“шахматное” поле (8 на 8 клеток) и делает это оптимально
(использовать цикл).
"""
# import tkinter as tk
#
# size = 400
# amount = 16
#
# window = tk.Tk()
# canvas = tk.Canvas(window, bg='white', width=size, height=size)
# for x in range(0, size, size // amount):
#     canvas.create_line((x, 0),
#                        (x, size),
#                        fill='black')
#     canvas.create_line((0, x),
#                        (size, x),
#                        fill='black')
# canvas.pack()
# window.mainloop()  # Главный цикл

"""
Задание 2:
Нарисуйте доску с расставленными шашками.
"""
# import tkinter as tk
#
# size = 400
# amount = 8
# diameter = size / amount
#
# window = tk.Tk()
# canvas = tk.Canvas(window, bg='white', width=size, height=size)
# for x in range(0, size, size // amount):
#     canvas.create_line((x, 0),
#                        (x, size),
#                        fill='black')
#     canvas.create_line((0, x),
#                        (size, x),
#                        fill='black')
#
# for y in range(3):
#     for x in range(4):
#         x_real = (2 * x + (y % 2)) * diameter
#         y_real = y * diameter
#         canvas.create_oval((x_real, y_real),
#                            (x_real + diameter, y_real + diameter),
#                            fill='lightgreen')
#
# for y in range(5, amount):
#     for x in range(4):
#         x_real = (2 * x + (y % 2)) * diameter
#         y_real = y * diameter
#         canvas.create_oval((x_real, y_real),
#                            (x_real + diameter, y_real + diameter),
#                            fill='lightblue')
#
# canvas.pack()
# window.mainloop()  # Главный цикл
