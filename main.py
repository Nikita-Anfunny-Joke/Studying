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

def circle_square(radius):
    S = (radius ** 2) * 3.14
    return S

circle_square(3)

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