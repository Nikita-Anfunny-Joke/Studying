""" ЗАДАНИЯ ПО КУРСУ """

# Создаю переменные с именем, возрастом и булевым выражением
name = "Nikita"
age = 27
is_student = True
print(name, age, is_student)



total_money = 1000
price = 26
jar_count = total_money // price
print(jar_count)

tasks = {
    1 : ['Полить цветы', 'Забрать посылку'],
    0 : ['Покормить кота'],
    2 : ['Почитать книгу по программированию'],
    3 : ['Ответить на письмо двоюродной тети']
}
print(tasks)


for keys in tasks:
    if 0 in tasks:
        print("есть срочные дела")
    else:
        print("можно отдохнуть")

values = []
for keys in tasks:
    values.append(tasks[keys])
print(values)

doings = []
for keys in tasks:
    for doin in tasks[keys]:
        doings.append(doin)

print(doings)
"""
doings = []

for a in tasks.values():
    for b in a:
        doings.append(b)
doings

"""


answer = []
for a in tasks.keys():
    if a > 2:  # Если приоритет меньше нуля надо добавить задачи
        continue
    else:
        for i in tasks.values():
            if len(answer) >= 1:
                break
            for j in i:
                if 'кот' in j:
                    answer.append(j)

answer


tasks = {
    0: ["Покормить кота","Покормить кота"],
    1: ["Покормить кота", "Забрать посылку"]
}
"""# Результат
new_tasks = {
    0: ['Покормить кота'],
    1: ['Покормить кота', 'Забрать посылку']
}
"""
new_tasks = {}
for key, value in tasks.items():
    new_tasks[key] = list(set(value))
new_tasks

# задание: расчет площади круга
def circle_square(radius):
    S = (radius ** 2) * 3.14
    return S

circle_square(3)

# задание: сшивание двух листов
new_list = []
def zip_(list_1, list_2):
    if len(list_1) > len(list_2):
        smol_list = list_2
        big_list = list_1
    else:
        smol_list = list_1
        big_list = list_2
    min_len = len(smol_list)
    for i in range(min_len):
        new_list.append((list_1[i], list_2[i]))
    return (new_list)
zip_([1, 5, 3, 8, 35],[2, 7, 9])


# задание: расчет суммы выплаты по кредиту
def final_balance(init_sum, interest_rate, years, round_num=2):
    end_sum = round((init_sum * ((100 + interest_rate) / 100) ** years), round_num)
    return end_sum

final_balance(1000, 5, 10)


# Задание исправления ошибки
def math_task(data):
    answer = []
    # возводим в третью степень
    for elem in data:
        answer += [elem ** 3]
    print("###")
    print(answer)
    print("###")
    # берем остаток от деления на 7
    for i in range(len(answer)):
        answer[i] = answer[i] % 7
    print("###")
    print(answer)
    print("###")
    # прибавляем к остатку изначальный массив
    for i in range(len(answer)):
        answer[i] = answer[i] + data[i]
    # возвращаем результат
    print("###")
    print(answer)
    print("###")
    return answer

#math_task(test_data)
print(math_task([1, 4, 5, 9])) # пример для самопроверки


# Улучшение кода с ошибкой
def math_task(data):
    answer = []
    # возводим в третью степень
    for elem in data:
        answer += [elem ** 3]
    print_array(answer)
    # берем остаток от деления на 7
    for i in range(len(answer)):
        answer[i] = answer[i] % 7
    print_array(answer)
    # прибавляем к остатку изначальный массив
    for i in range(len(answer)):
        answer[i] = answer[i] + data[i]
    # возвращаем результат
    print_array(answer)
    return answer

def print_array(answer):
    print("###")
    print(answer)
    print("###")


#math_task(test_data)
print(math_task([1, 4, 5, 9])) # пример для самопроверки


# ЗАДАЧА С ПОДСЧЕТОМ ЧИСЛА ИЗ СПИСКОВ

int_value = []
def sum_as_ints(list_):
    for element in list_:
        try:
            int_value.append(int(element))
        except ValueError:
            print("Can't be converted to int")
    return sum(int_value)


# ЗАДАЧА С РАЗВОРОТОМ ТЕКСТА

def reversed_(array):
    rv = []
    for i in range(len(array)):
        rv.append(array[i])
    return rv

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if reversed_(reversed_([1, 2, 3])) == [1, 2, 3]:
    print("Все хорошо")
else:
    raise RuntimeError("Ошибка, после обращения дважды не получается исходный массив!")

arr = [1, 2, 3]
if reversed_(reversed_(arr)) == arr:
    print("Все хорошо")
else:
    raise RuntimeError("Ошибка, после обращения дважды не получается исходный массив!")



def find_substr(unstr, full_str):
    first_znac = unstr[0]
    last_znac = unstr[len(unstr)-1]
    print(first_znac, last_znac)
    if unstr in full_str:
        return (full_str.index(first_znac), full_str.index(last_znac) +1)
    else:
        pass

find_substr("ма", "маленькая машина")


def find_substr(substring, string):
    for i in range(len(string) - len(substring) + 1):

        candidate = string[i:i + len(substring)]
        if candidate == substring:
            return (i, i + len(substring))

find_substr("ма", "маленькая машина")



# ЗАДАЧА С ВЫВОДОМ КАЖДОГО 5го ЭЛЕМЕНТА С КОНЦА СПИСКА

test1 = ['e',6,8,'A','>','^','S','$','R','C',6,'+','#',9,'/',1,'T','!','%','K',7,'-','O','*','<',2,'h',4,'g']

answer = []
def fifth_element(full_list: list) -> list:
    for n in range(len(full_list) // 5):
        print(n)
        answer.append(full_list[(len(full_list)) - (5 * (n + 1))])
        print(answer)
    return answer

fifth_element(test1)


# ЗАДАЧА С СМЕНОЙ СЛОВ И ИЗМЕНЕНИЕМ РЕГИСТРА

answer = []
def process_string(string):
    answer = string[1:].lower()
    if 'intern' in answer:
        answer = answer.replace('intern', 'junior')
        print(answer)
    return answer

process_string('IIntern reads a lot of books')


# ЗАДАЧА НА НАХОЖДЕНИЕ ОШИБОК В ТЕКСТЕ

def check_string(string):
    if (string[0] or string[(len(string) - 1)]) == ' ':
        return False
    if string[0].isupper() == True and string[1:-1].islower() == True:
        return True
    else:
        return False
    if string[- 1] == '.':
        return True
    else:
        return False

check_string('В этом году будет особенно теплое море.')


# ЗАДАЧА СОЗДАНИЯ ОБЪЕКТА С DATETIME

import datetime as dt

launch_date = dt.date(day=10, month=2, year=2022)

from datetime import timedelta,datetime

times = datetime(month=3, day=8, year=2022) + timedelta(days=3, hours=5, minutes=6)

# ПОДКЛЮЧЕНИЕ К БД

# pip install psycopg2 если библиотека не установлена
import psycopg2

database="startml",
user="robot-startml-ro",
password="pheiph0hahj1Vaif",
host="postgres.lab.karpov.courses",
port=6432

import pandas as pd

df = pd.read_sql(
    """SELECT * FROM "feed_action" LIMIT 10 """,
    con="postgresql://robot-startml-ro:pheiph0hahj1Vaif@"
        "postgres.lab.karpov.courses:6432/startml"
)
df.head(5)

# ЗАДАНИЕ ТРЕУГОЛЬНИКА ЧЕРЕЗ КЛАСС

from dataclasses import dataclass

@dataclass
class Triangle():
    n_dots = 3
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
tr_1 = Triangle(1, 2, 2.5)
tr_2 = Triangle(6, 8, 1)
