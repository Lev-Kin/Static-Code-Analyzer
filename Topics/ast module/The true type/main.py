import ast

user_input = input()
result = ast.literal_eval(user_input)
print(type(result))