# from random import choice
#
# from lesson_25.db_manager import DataBase

# name_db = 'game.db'
# table_name = 'scores'
#
# my_db_manager = DataBase(name_db)
# my_db_manager.create_table()
#
# # pool_name = ('Василий', 'Денис', 'Костя', 'Саша')
# # pool_nums = tuple(range(2, 6))
# #
# # for i in range(len(pool_name)):
# #     my_db_manager.insert(table_name, choice(pool_name), choice(pool_nums))
#
# qwery = f'''SELECT name, score_points FROM {table_name} WHERE score_points > 3 ORDER BY score_points DESC
# '''
#
# response = my_db_manager.get(qwery)
#
# print(response)

