# 2.1.11
sum = 0
number = int(input())
while number != 0:
    sum += number
    number = int(input())
print(sum)

# 2.1.12
a = int(input())
b = int(input())
if a > b:
    greater = a
else:
    greater = b
while True:
    if (greater % a == 0) and (greater % b == 0):
        lcm = greater
        break
    greater += 1
print(lcm)