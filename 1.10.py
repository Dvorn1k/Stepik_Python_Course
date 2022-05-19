# 1.10.5
A = int(input())
B = int(input())
H = int(input())
if H < A:
    print("Недосып")
elif A <= H < B:
    print("Это нормально")
elif A < H <= B:
    print("Это нормально")
elif B < H:
    print("Пересып")

# 1.10.6
year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Високосный")
else:
    print("Обычный")
