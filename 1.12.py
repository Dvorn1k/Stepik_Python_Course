# 1.12.1
a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
print((p * (p - a) * (p - b) * (p - c)) ** 0.5)

# 1.12.2
input_number = int(input())
if -15 < input_number <= 12 or 14 < input_number < 17 or 19 <= input_number:
    print(True)
else:
    print(False)

# 1.12.3
input_number_1 = float(input())
input_number_2 = float(input())
math_operation = input()
if math_operation == "+":
    print(input_number_1 + input_number_2)
elif math_operation == "-":
    print(input_number_1 - input_number_2)
elif math_operation == "*":
    print(input_number_1 * input_number_2)
elif math_operation == "/":
    if input_number_2 == 0:
        print("Деление на 0!")
    else:
        print(input_number_1 / input_number_2)
elif math_operation == "mod":
    if input_number_2 == 0:
        print("Деление на 0!")
    else:
        print(input_number_1 % input_number_2)
elif math_operation == "pow":
    print(input_number_1 ** input_number_2)
elif math_operation == "div":
    if input_number_2 == 0:
        print("Деление на 0!")
    else:
        print(input_number_1 // input_number_2)

# 1.12.4
figure = input()
if figure == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif figure == "прямоугольник":
    a = int(input())
    b = int(input())
    print(a * b)
elif figure == "круг":
    r = int(input())
    print(3.14 * r ** 2)

# 1.12.5
first_number = int(input())
second_number = int(input())

if first_number > second_number:
    max_num = first_number
    min_num = second_number
else:
    max_num = second_number
    min_num = first_number

third_number = int(input())

if third_number >= max_num:
    last_num = max_num
    max_num = third_number
elif max_num > third_number > min_num:
    last_num = third_number
elif third_number <= min_num:
    last_num = min_num
    min_num = third_number

print(max_num)
print(min_num)
print(last_num)

# 1.12.6
programmers = int(input())
if programmers % 10 == 1 and programmers % 100 != 11:
    print(programmers, "программист")
elif (2 <= programmers % 10 <= 4) and (14 < programmers % 100 or programmers % 100 < 12):
    print(programmers, "программиста")
else:
    print(programmers, "программистов")

# 1.12.7
bus_number = int(input())
if bus_number // 100000 + bus_number // 10000 % 10 + bus_number // 1000 % 10 == bus_number // 100 % 10 + bus_number // 10 % 10 + bus_number % 10:
    print("Счастливый")
else:
    print("Обычный")

