import sqlite3
from random import choice

connection = sqlite3.connect('school.db')
cursor = connection.cursor()

# query_create = '''
# CREATE TABLE IF NOT EXISTS class (
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     surname TEXT,
#     mark INTEGER
# )
# '''

# query_insert = '''
# INSERT INTO class (name, surname, mark) VALUES
#     ('Василий', 'Пупукин', 3),
#     ('Денис', 'Синицин', 4),
#     ('Ангелина', 'Соколова', 5),
#     ('Александр', 'Петров', 2)
# '''

query_insert = '''
INSERT INTO class (name, surname, mark) VALUES
    ('{}', '{}', {})
'''

pool_name = ('Василий', 'Денис', 'Костя', 'Саша')
pool_surname = ('Синицин', 'Соколов', 'Петров', 'Крылов')
pool_nums = tuple(range(2, 6))

for i in range(5):
    name_insert = choice(pool_name)
    surname_insert = choice(pool_surname)
    mark_insert = choice(pool_nums)
    cursor.execute(query_insert.format(name_insert, surname_insert, mark_insert))

connection.commit()
connection.close()
