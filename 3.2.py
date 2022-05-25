# 3.2.5
def update_dictionary(d, key, value):
    for key_d in d.keys():
        if key_d == key:
            d[key].append(value)
            return
    for key_d in d.keys():
        if key_d == 2 * key:
            d[2 * key].append(value)
            return
    d[2 * key] = [value]

# 3.2.6
dict = {}
flag=False
list_of_words = [str(i).lower() for i in input().split()]
for i in list_of_words:
    for key_dict in dict.keys():
        flag = False
        if key_dict == i:
            flag = True
            break
    if flag:
        dict[i]+=1
    else:
        dict[i]=1
for i in dict.items():
    print(*i)

# 3.2.7
dict={}
n=int(input())
for i in range(n):
    num=int(input())
    if num in dict.keys():
        print(dict[num])
    else:
        dict[num]=f(num)
        print(dict[num])