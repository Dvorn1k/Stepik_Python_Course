# 3.7.1
n = int(input())
dictoinary = {}
for j in range(n):
    string = str(input()).strip().split(';')
    if string[0] not in dictoinary.keys():
        dictoinary[string[0]] = [0, 0, 0, 0, 0]
    if string[2] not in dictoinary.keys():
        dictoinary[string[2]] = [0, 0, 0, 0, 0]

    if string[0] in dictoinary.keys():
        dictoinary[string[0]][0]+=1
    if string[2] in dictoinary.keys():
        dictoinary[string[2]][0]+=1

    if int(string[1]) < int(string[3]):
        dictoinary[string[2]][1] += 1
        dictoinary[string[2]][4] += 3
        dictoinary[string[0]][3] += 1
    elif int(string[1]) == int(string[3]):
        dictoinary[string[0]][2] += 1
        dictoinary[string[0]][4] += 1
        dictoinary[string[2]][2] += 1
        dictoinary[string[2]][4] += 1
    elif int(string[1]) > int(string[3]):
        dictoinary[string[0]][1] += 1
        dictoinary[string[0]][4] += 3
        dictoinary[string[2]][3] += 1

for key, val in dictoinary.items():
    answer=key+':'
    for i in val:
        answer+=str(i)+' '
    print(answer)

# 3.7.2
d_keys=str(input())
d_values=str(input())
dictionary1={}
dictionary2={}
for i in range(len(d_keys)):
    dictionary1[d_keys[i]]=d_values[i]
    dictionary2[d_values[i]]=d_keys[i]
word_to_cipher=str(input())
answer=""
for i in word_to_cipher:
    answer+=dictionary1[i]
print(answer)
answer=""
cipher_to_word=str(input())
for i in cipher_to_word:
    answer+=dictionary2[i]
print(answer)

# 3.7.3
word_count=int(input())
word_list=[]
for i in range(word_count):
    word=str(input()).strip().lower()
    word_list.append(word)
lines_count=int(input())
answer=[]
for i in range(lines_count):
    line=str(input()).lower().strip().split(' ')
    for i in line:
        if i not in word_list:
            answer.append(i)
answer=set(answer)
for i in answer:
    print(i)

# 3.7.4
n = int(input())
x=0
y=0
for i in range(n):
    line = str(input()).strip().split(' ')
    if line[0]=='север':
        y+=int(line[1])
    elif line[0]=='юг':
        y -= int(line[1])
    elif line[0] == 'запад':
        x -= int(line[1])
    elif line[0] == 'восток':
        x += int(line[1])
print(x,y)

# 3.7.5
output = open('output.txt', 'w')
d={}
for i in range(11):
    d[i+1]=[0,0]
with open('dataset_3380_5.txt') as fInput:
    for line in fInput:
        line_list=line.strip().split('\t')
        d[int(line_list[0])][0]+=int(line_list[2])
        d[int(line_list[0])][1] += 1


for key, val in d.items():
    answer=str(key)+' '
    if d[key][0] != 0:
        answer+=str(d[key][0]/d[key][1])+'\n'
    else:
        answer+='-\n'
    output.write(answer)
output.close()