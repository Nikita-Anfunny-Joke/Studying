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


