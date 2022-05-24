#2.6.7
sum=0
sum_sqrt=0
while True:
    num=int(input())
    sum+=num
    sum_sqrt+=num**2
    if sum == 0:
        break
print(sum_sqrt)

# 2.6.8
num = int(input())
if num == 1:
    print(1)
else:
    answer = ""
    count = 0
    for i in range(num):
        if count !=num:
            for j in range(i):
                answer += str(i) + ' '
                count += 1
                if count == num:
                    break
    print(answer)

# 2.6.9
nums = [int(i) for i in input().split()]
find_num = int(input())
answer = []
for i in range(len(nums)):
    if nums[i] == find_num:
        answer += [i]
if len(answer) == 0:
    print('Отсутствует')
else:
    print(*answer)

# 2.6.10
matrix = []
line = []
while True:
    for i in input().split():
        line.append(i)
    if line == ["end"]:
        break
    matrix += [line]
    line = []
answer_matrix = []
for i,line in enumerate(matrix):
    temp=[]
    for j,num in enumerate(matrix[i]):
        a =int(matrix[i-1][j])
        b =int(matrix[(i+1)%len(matrix)][j])
        c =int(matrix[i][(j+1)%len(matrix[0])])
        d =int(matrix[i][j-1])
        temp.append(a+b+c+d)
    answer_matrix.append(temp)
for i,a in enumerate(matrix):
    print(*answer_matrix[i])

# 2.6.11
n = int(input())
matrix=[]
for i in range(n):
    temp=[]
    for j in range(n):
        temp.append(0)
    matrix.append(temp)
i = 0
j = -1
num = 1
direction = 'right'  # up, down, right, left
while num <= n ** 2:
    if direction == 'right':
        j += 1
        if -1<j<len(matrix)and matrix[i][j]==0 :
            matrix[i][j]=nums
        else:
            j-=1
            direction = "down"
            i+=1
            matrix[i][j] = num
    elif direction == "left":
        j -= 1
        if -1 < j < len(matrix) and matrix[i][j]==0:
            matrix[i][j] = num
        else:
            j += 1
            direction = "up"
            i -= 1
            matrix[i][j] = num
    elif direction == "up":
        i -= 1
        if -1 < i < len(matrix) and matrix[i][j]==0:
            matrix[i][j] = num
        else:
            i += 1
            direction = "right"
            j += 1
            matrix[i][j] = num
    elif direction == "down":
        i += 1
        if -1 < i < len(matrix)and matrix[i][j]==0:
            matrix[i][j] = num
        else:
            i -= 1
            direction = "left"
            j -= 1
            matrix[i][j] = num
    num += 1
for i in matrix:
    print(*i)
