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

# КОГДА ПРИМЕНЯТЬ ОПРЕДЕЛЕННЫЙ ТИП ДАННЫХ??

''' LIST лист
Списки стоит применять, когда мы хотим класть много данных в одно логическое место.
Например, список заказов одного клиента.
Если хотим добавлять элементы, следить за их взаимным порядком и удалять — самое то.
'''

""" TUPLE кортеж
Кортежи применяют когда требуются удобства списков, но в то же время важна неизменяемость данных.
"""

'''SET множества
Если нужно получить только уникальные элементы и порядок элементов не важен.
Самый частый на практике кейс.
Если нужно узнать пересечение и прочие операции над множествами.
'''

""" DICT словарь
Коллекция, которая упорядочена** и изменяема. Нет повторяющихся элементов.
"""
