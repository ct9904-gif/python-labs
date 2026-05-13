
print("=== Лабораторная работа №1 — Ввод и вывод ===\n")

# 3.1 Задача «Сумма трёх чисел»
print("3.1 Сумма трёх чисел")
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)
print("-" * 50)

# 3.2 Задача «Площадь прямоугольного треугольника»
print("3.2 Площадь прямоугольного треугольника")
b = int(input("Введите длину первого катета: "))
h = int(input("Введите длину второго катета: "))
area = 0.5 * b * h
print(area)
print("-" * 50)

# 3.3 Задача «Апельсины в коробке»
print("3.3 Апельсины в коробке")
x = int(input())  # количество детей
y = int(input())  # количество апельсинов
print(y // x)     # каждому ребенку
print(y % x)      # в коробке
print("-" * 50)

# 3.4 Задача «Часы»
print("3.4 Часы")
m = int(input("Введите количество минут: "))
hours = m // 60 % 24
minutes = m % 60
print(hours, minutes)
print("-" * 50)

# 3.5 Задача «Hello, world!»
print("3.5 Hello, world!")
name = input()
print("Hello, " + name + "!")
print("-" * 50)

# 3.6 Задача «Следующее и предыдущее»
print("3.6 Следующее и предыдущее")
n = int(input())
print("The next number for the number", n, "is", n + 1)
print("The previous number for the number", n, "is", n - 1)
print("-" * 50)

# 3.7 Задача «Парты»
print("3.7 Парты")
a = int(input())
b = int(input())
c = int(input())
total = a + b + c
computers = (total + 1) // 2   # округляем вверх
print(computers)
print("-" * 50)

# 3.8 Задача «Шнурки»
print("3.8 Шнурки")
a = int(input())  # расстояние между рядами
b = int(input())  # расстояние между дырочками в ряду
l = int(input())  # длина свободного конца шнурка
N = int(input())  # количество дырочек в одном ряду

length = l * 2 + (N - 1) * 2 * b + (N - 1) * a + a
print(length)

print("\n" + "="*60)
print("Все 8 заданий лабораторной работы №1 выполнены!")