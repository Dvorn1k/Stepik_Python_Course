# 3.4.2
output = open('output.txt', 'w')
with open('dataset_3363_2.txt') as input:
    for line in input:
        line = line.strip()
        answer_line = ""
        multy_char = line[0]
        multy = ''
        for i, char in enumerate(line):
            if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and i!=0:
                answer_line+=multy_char*int(multy)
                multy_char = char
                multy=''
            else:
                if i!=0:
                    multy += char
        answer_line += multy_char * int(multy)
        output.write(answer_line)
output.close()

# 3.4.3
output = open('output.txt', 'w')
dict = {}
with open('dataset_3363_3.txt') as input:
    for line in input:
        line = line.strip().lower()
        line = line.split(' ')
        for i in line:
            if i in dict.keys():
                dict[i]+=1
            else:
                dict[i]=1
    max_count=max(dict.values())
    answer =[]
    for i in dict.keys():
        if dict[i]==max_count:
            answer.append(i)
    answer.sort()
output.write(answer[0])
output.write(' '+str(dict[answer[0]]))
output.close()

# 3.4.4
output = open('output.txt', 'w')
with open('dataset_3363_4.txt', "r", encoding='utf-8') as fInput:
    sumF = 0
    sumM = 0
    sumR = 0
    count = 0
    for line in fInput:
        count += 1
        line = line.strip()
        line = line.split(';')
        sum = 0
        for i in range(1, len(line)):
            sum += int(line[i])
            if i == 1:
                sumM += int(line[i])
            elif i == 2:
                sumF += int(line[i])
            else:
                sumR += int(line[i])
        output.write(str(sum / 3) + '\n')
    output.write(str(round(sumM/count, 9))+' '+str(round(sumF/count, 9))+' '+str(round(sumR/count, 9)))
output.close()
