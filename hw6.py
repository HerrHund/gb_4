#Реализовать два небольших скрипта:
#а) итератор, генерирующий целые числа, начиная с указанного,
#б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#Подсказка: использовать функцию count() и cycle() модуля itertools. 
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. 
# Необходимо предусмотреть условие его завершения.
#Например, в первом задании выводим целые числа, начиная с 3, 
# а при достижении числа 10 завершаем цикл. 
# Во втором также необходимо предусмотреть условие, 
# при котором повторение элементов списка будет прекращено.

from itertools import cycle, count

sStart = int(input('Начинаем с: '))
sStop = sStart * 2 + 10 + 1

# v.1
for i in count(sStart):
    if i < sStop:
        print(i)
    else:
        break
del i

# v.2
my_list = [i for i in range(sStop)]
count = 0
for b in cycle(my_list):
    if count < sStop + 10:
        print(b)
        count += 1
    else:
        break

