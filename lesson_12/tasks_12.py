"""
Задание:
Напишите функцию check_string_brackets(input_string), 
которая проверяет, является ли поступившая на вход строка 
правильной скобочной последовательностью. Если да, 
она должна печатать YES, в противном случае — NO. 
Обратите внимание, что пустая строка также является 
правильной скобочной последовательностью.
"""

def check_string_brackets(input_string):
    stack = []
    for char in input_string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0:
                print("NO")
                return
            stack.pop()

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")


check_string_brackets("()")
check_string_brackets("(()())")
check_string_brackets("(()(()")
check_string_brackets(")(")
