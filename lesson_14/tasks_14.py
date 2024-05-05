"""
Задание 1:
Напишите программу, в которой цель главного героя -
выбраться из ловушки (добраться до белого круга,
как только он добирается - выводит на Label - ты победил.
"""
################################################################################################
"""
1 вариант
"""
# import tkinter as tk
#
#
# def move(event):
#     key = event.keysym
#     if key == 'Up':
#         canvas.move(player, 0, -50)
#     elif key == 'Down':
#         canvas.move(player, 0, 50)
#     elif key == 'Left':
#         canvas.move(player, -50, 0)
#     elif key == 'Right':
#         canvas.move(player, 50, 0)
#
#     check_win()
#
#
# def check_win():
#     x1, y1, x2, y2 = canvas.coords(player)
#     overlap = canvas.find_overlapping(x1, y1, x2, y2)
#     if finish_circle in overlap:
#         result_label.config(text="Ты победил!")
#
#
# root = tk.Tk()
# root.title("Игра: выберись из ловушки!")
#
# canvas = tk.Canvas(root, width=500, height=500)
# canvas.pack()
#
# player = canvas.create_rectangle(50, 50, 100, 100, fill="blue")
# trap = canvas.create_rectangle(200, 200, 400, 400, fill="red")
# finish_circle = canvas.create_oval(450, 450, 500, 500, fill="white")
#
# result_label = tk.Label(root, text="")
# result_label.pack()
#
# canvas.focus_set()
# canvas.bind("<Key>", move)
#
# root.mainloop()

################################################################################################
"""
2 вариант
"""
# import tkinter as tk
# import random
#
# master = tk.Tk()
#
# step = 64
# N_X = 10
# N_Y = 10
#
# WIDTH = step * N_X
# HEIGHT = step * N_Y
# a = False
#
# player_pic = tk.PhotoImage(file=r".\dragon.png")
#
# canvas = tk.Canvas(master, bg='#FCAB08',
#                    width=WIDTH, height=HEIGHT)
# player_pos = (random.randint(0, N_X - 1) * step, random.randint(0, N_Y - 1) * step)
# print(player_pos)
#
# label = tk.Label(master, text="He попадись!")
#
#
# def prepare_and_start():
#     global player
#     global finish_circle
#
#     canvas.delete("all")
#
#     finish_circle = canvas.create_oval(200, 200, 250, 250, fill="white")
#
#     player_pos = (random.randint(1, N_X - 1) * step,
#                   random.randint(1, N_Y - 1) * step)
#     player = canvas.create_image((player_pos[0], player_pos[1]),
#                                  image=player_pic,
#                                  anchor='nw')
#     label.config(text="Haйди выход!")
#     master.bind("<KeyPress>", key_pressed)
#
#
# def move_wrap(obj, move_x, move_y):
#     xy = canvas.coords(obj)
#     canvas.move(obj, move_x, move_y)
#     print(xy)
#
#     if xy[0] <= 0:
#         canvas.move(obj, WIDTH, 0)
#     if xy[0] >= WIDTH:
#         canvas.move(obj, -WIDTH, 0)
#     if xy[1] <= 0:
#         canvas.move(obj, 0, HEIGHT)
#     if xy[1] >= HEIGHT:
#         canvas.move(obj, 0, -HEIGHT)
#     check_win()
#
#
# def check_win():
#     xy = canvas.coords(player)
#     overlap = canvas.find_overlapping(xy[0], xy[1], xy[0]+200, xy[1]+200)
#     if finish_circle in overlap:
#         print("winner")
#         label.config(text="Ты победил!")
#
#
# def key_pressed(event):
#     if event.keysym == 'Up':
#         move_wrap(player, 0, -step)
#     elif event.keysym == 'Down':
#         move_wrap(player, 0, step)
#     elif event.keysym == 'Right':
#         move_wrap(player, step, 0)
#     elif event.keysym == 'Left':
#         move_wrap(player, -step, 0)
#
#
# # Добавляем кнопку рестарт
# restart = tk.Button(master, text="Haчaть заново", command=prepare_and_start)
#
# # Упаковываем созданные объекты
# restart.pack()
# label.pack()
# canvas.pack()
# prepare_and_start()
#
# master.bind("<KeyPress>", key_pressed)
# master.mainloop()



"""
Задание 2:
Добавить в игру врага Enemy, который за каждый шаг игрока
ходит в произвольном направлении (одно из 4-ёх). При
совпадении координат врага и главного героя игра 
заканчивается в Label “Ты проиграл” и завершение работы
приложения
"""

