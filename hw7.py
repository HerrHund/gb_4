# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. 
# При вызове функции должен создаваться объект-генератор. 
# Функция должна вызываться следующим образом: for el in fact(n). 
# Функция отвечает за получение факториала числа, 
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
#Подсказка: факториал числа n — произведение чисел от 1 до n. 
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.


def datanum(number):
    count = 1
    while count <= number:
        yield count
        count += 1
i = 1
dataList = []
for l in datanum(5):
    if i > 15:
        break
    else:
        dataList.append(l)
        i += 1
print(dataList)

