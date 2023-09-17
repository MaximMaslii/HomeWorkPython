'''Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.'''

n = int(input("Введите количество элементов в первом множестве: "))
m = int(input("Введите количество элементов во втором множестве: "))

set1 = set()
set2 = set()

print("Введите элементы первого множества:")
for i in range(n):
    element = int(input())
    set1.add(element)

print("Введите элементы второго множества:")
for i in range(m):
    element = int(input())
    set2.add(element)

intersection = set1.intersection(set2)

result = sorted(list(intersection))
print("Числа, которые встречаются в обоих множествах в порядке возрастания:")
for num in result:
    print(num)

