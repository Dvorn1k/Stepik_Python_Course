#2.4.3
string=str(input())
string=string.lower()
print((string.count('c')+string.count("g"))/len(string)*100)

# 2.4.7
string = str(input())
char_old = ""
count = 1
string_answer = ''
for i in range(len(string)):
    if i == 0:
        char_old = string[i]
        continue
    elif string[i] == char_old:
        count += 1
        continue
    elif string[i] != char_old:
        string_answer += char_old + str(count)
        count=1
        char_old = string[i]
string_answer += char_old + str(count)
print(string_answer)