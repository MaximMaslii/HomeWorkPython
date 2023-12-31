'''Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
50 -> 1, 2, 4, 8, 16, 32'''

N = int(input("Введите число N: "))
power_of_two = 1

while power_of_two <= N:
    print(power_of_two)
    power_of_two *= 2


'''Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
РРРОРООРОРР -> 4
ОРОРОРОРОРО -> 5'''

def min_flips(coins):
    count_heads = 0
    count_tails = 0

    for coin in coins:
        if coin == 'H':
            count_heads += 1
        else:
            count_tails += 1
    return min(count_heads, count_tails)

coins = input("Введите последовательность монет (например, 'HHHTTTHHH'): ")
result = min_flips(coins)
print("Минимальное количество переворотов:", result)


'''Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
7, 10 -> 2, 5 (2 + 5 == 7; 2 * 5 == 10)'''

def find_numbers(S, P):
    for x in range(1, S + 1):
        if P % x == 0:
            y = P // x
            if x + y == S:
                return x, y
    return None

S = int(input("Введите сумму S: "))
P = int(input("Введите произведение P: "))

result = find_numbers(S, P)

if result:
    print(f"Задуманные числа: {result[0]} и {result[1]}")
else:
    print("Нет натуральных чисел X и Y, которые соответствуют заданным S и P.")
