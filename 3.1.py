# 3.1.8
def f(x):
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        return -(x / 2)
    elif 2 < x:
        return (x - 2) ** 2 + 1


# 3.1.9
def modify_list(l):
    delete_index_list = []
    for i, num in enumerate(l):
        if num % 2 != 0:
            delete_index_list.append(i)
        elif num % 2 == 0:
            l[i] = num // 2
    for i in range(len(delete_index_list)-1, -1, -1):
        l.pop(delete_index_list[i])
