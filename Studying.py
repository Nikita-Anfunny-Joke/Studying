"""
Здесь я буду изучать Python и машинное обучение
"""

# ТИПЫ ДАННЫХ
""" НЕИЗМЕЯЕМЫЕ ТИПЫ ДАННЫХ
1) строка - str
2) целые числа - int
3) числа с 'плавающей' точкой - float
4) кортежи - tuple
5) логические типы данных - bool
"""
my_string = "Hello"
print(type(my_string))

number = 3
print(type(number))

float_number = 3.141592
print(type(float_number))

my_tuple = ("Strings", "Numbers", "Tuples", "Boolean")
print(type(my_tuple))

logical_val = True
print(type(logical_val))

logical_val = False
print(type(logical_val))

""" ИЗМЕНЯЕМЫЕ ТИПЫ ДАННЫХ
1) лист - list
2) словарь - dict
3) множества - set
"""

my_list = ["Strings", "Numbers", "Tuples", "Boolean"]
print(type(my_list))

my_dict = {
"Lists": "mutable",
"Strings": "immutable",
"Numbers": "immutable"
}

print(type(my_dict))

my_set = {"Strings", "Numbers", "Tuples", "Boolean"}
print(type(my_set))

""" ЛОГИЧЕСКИЕ ОПЕРАТРЫ
true AND true = true
true AND false = false

true OR false = true

NOT true = false
false OR NOT false = true

() > not > and > or
"""

