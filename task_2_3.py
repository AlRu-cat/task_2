# 3. Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
# Как модифицировать это условие для чисел со знаком?

#Выявляем число среди элементов списка
numbers = [3000.0, 1580.0, 3000.0, 2785.8, 'one', 85, 'two']
i = 0
for i in range(len(numbers)):
    if type(numbers[i]) == float or type(numbers[i]) == int :
        print(numbers[i])

#Выявляем числа со знаком среди элементов списка

numbers = [3000.0, 1580.0, 3000.0, 2785.8, 'one', 85, 'two', -89, -96]
i = 0
for i in range(len(numbers)):
    if (type(numbers[i]) == float or type(numbers[i]) == int) and numbers[i] >= 0 :
        print('В списке есть положительные числа: ', numbers[i])

    elif (type(numbers[i]) == float or type(numbers[i]) == int) and numbers[i] < 0:
        print ('В списке есть отрицательные числа: ', numbers[i])

# Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'
# Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
# Можно ли при этом не создавать новый список?

first = workers[0].split()
second = workers[1].split()
a = second[2].title()
third = workers[2].split()
b = third[3].title()
forth = workers[3].split()
c = forth[1].title()


name = []
name.extend([first[1], a, b, c])

for i in range(len(name)):
    welcome = f'{name[i]}, привет!'
    print(welcome)