import tkinter as tk

"""
Слайд 5
"""
print('Start')
window = tk.Tk()  # Создание главного окна приложения
canvas = tk.Canvas(window, bg='yellow', width=300, height=300)
canvas.pack()
window.mainloop()  # Главный цикл
print('Stop')

"""
Слайд 8
"""
# print('Start')
# window = tk.Tk()  # Создание главного окна приложения
# canvas = tk.Canvas(window, bg='#12f41f', width=700, height=700)
# canvas.create_oval((300, 400),
#                    (500, 500),
#                    fill='yellow')
# canvas.create_line((0, 0),
#                    (100,200),
#                    (300, 300),
#                    (200, 100),
#                    fill='black')
# canvas.pack()
# window.mainloop()  # Главный цикл
# print('Stop')


"""
Слайд 9
"""

# def move_by_keys(event):
#     if event.keysym == 'Up':
#         canvas.move(oval, 0, -20)
#     elif event.keysym == 'Down':
#         canvas.move(oval, 0, 20)
#     elif event.keysym == 'Left':
#         canvas.move(oval, -20, 0)
#     elif event.keysym == 'Right':
#         canvas.move(oval, 20, 0)
#
# window = tk.Tk()  # Создание главного окна приложения
# lable = tk.Label(window, text='INGINIRIUM')
# lable.pack()
# canvas = tk.Canvas(window, bg='#fff', width=700, height=700)
# oval = canvas.create_oval((300, 300),
#                    (500, 500),
#                    fill='green')
#
# canvas.pack()
# window.bind("<KeyPress>", move_by_keys)
# window.mainloop()  # Главный цикл

"""
Слайд 10
"""

# def move_by_keys(event):
#     info_coords = canvas.coords(oval)
#     x = info_coords[0]
#     y = info_coords[1]
#     lable.config(text=str(x) + ' ' + str(y))
#     if event.keysym == 'Up':
#         canvas.move(oval, 0, -20)
#     elif event.keysym == 'Down':
#         canvas.move(oval, 0, 20)
#     elif event.keysym == 'Left':
#         canvas.move(oval, -20, 0)
#     elif event.keysym == 'Right':
#         canvas.move(oval, 20, 0)
#
# window = tk.Tk()  # Создание главного окна приложения
# lable = tk.Label(window, text='INGINIRIUM')
# lable.pack()
# canvas = tk.Canvas(window, bg='#fff', width=700, height=700)
# oval = canvas.create_oval((300, 300),
#                    (500, 500),
#                    fill='green')
#
# canvas.pack()
# window.bind("<KeyPress>", move_by_keys)
# window.mainloop()  # Главный цикл