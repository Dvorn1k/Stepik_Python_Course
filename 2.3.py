# 2.3.3
c = int(input())
d = int(input())
a = int(input())
b = int(input())
str_output = ""
for i in range(a, b + 1):
    str_output += '\t' + str(i)
print(str_output)
str_output = ""
for j in range(c, d + 1):
    str_output += str(j)
    for i in range(a, b + 1):
        str_output += '\t' + str(i * j)
    print(str_output)
    str_output = ""

# 2.3.7
a = int(input())
b = int(input())
sum = 0
count = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        sum += i
        count += 1
print(sum / count)
