# Написать функцию, аргументы имена сотрудников,
# возвращает словарь, ключи — первые буквы имён, значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 
# 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

name_lst = "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
print(name_lst)

name_dict = {}
for name in name_lst:
    key = name[0]
    if key not in name_dict:
        name_dict[key] = []
    name_dict[key].append(name)
print (name_dict)