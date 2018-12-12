"""2.C4

Дан набор из N целых положительных чисел. Из них нужно выбрать и вывести два числа так, чтобы их сумма была нечётна, а произведение делилось на 5 и при этом было максимально возможным. Выбранные числа можно выводить в любом порядке. Если есть несколько подходящих пар, можно выбрать любую из них. Если подходящих пар нет, нужно вывести 0.
Напишите эффективную по времени и по памяти программу для решения этой задачи.
Программа считается эффективной по времени, если при увеличении количества исходных чисел N в k раз время работы программы увеличивается не более чем в k раз.
Программа считается эффективной по памяти, если память, необходимая для хранения всех переменных программы, не превышает 1 килобайта и не увеличивается с ростом N.
Максимальная оценка за правильную (не содержащую синтаксических ошибок и дающую правильный ответ при любых допустимых входных данных) программу, эффективную по времени и по памяти, — 4 балла.
Максимальная оценка за правильную программу, эффективную только по времени или только по памяти, — 3 балла.
Максимальная оценка за правильную программу, не удовлетворяющую требованиям эффективности, — 2 балла.
Вы можете сдать одну или две программы решения задачи. Если Вы сдадите две программы, каждая из них будет оцениваться независимо от другой, итоговой станет бо́льшая из двух оценок.
Перед текстом программы кратко опишите алгоритм решения. Укажите использованный язык программирования и его версию.
Описание входных и выходных данных.
В первой строке входных данных задаётся количество чисел N (1 ≤ N ≤ 1000). В каждой из последующих N строк записано одно натуральное число, не превышающее 100.
Пример входных данных:
5
1
2
4
5
7
Пример выходных данных для приведённого выше примера входных данных:
4 5
Из 5 чисел можно составить 10 пар. В данном случае условиям удовлетворяют две пары: (2, 5) и (4, 5). Суммы чисел в этих парах (7 и 11) нечётны, а произведения (10 и 20) делятся на 5. У всех остальных пар как минимум одно из этих условий не выполняется. Из двух возможных пар выводим ту, в которой больше произведение элементов."""

a=0
"""первое число должно быть кратно 5"""
b=0
"""второе число должно быть чётным"""
n = int(input())
for i in range(n):
    x = int(input())
    if x % 5 ==0 and x>a:
        a=x
    elif x%2 ==0 and x>b:
        b=x
print(a,b,sep=" ")
