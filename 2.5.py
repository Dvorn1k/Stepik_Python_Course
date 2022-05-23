# 2.5.9
nums = [int(i) for i in input().split()]
sum = 0
for i in nums:
    sum += i
print(sum)


nums = [int(i) for i in input().split()]
sum_nums = []
if len(nums) != 1:
    nums = [nums[len(nums) - 1]] + nums + [nums[0]]
    for i in range(1, len(nums)-1):
        sum_nums += [nums[i - 1] + nums[i + 1]]
    for i in sum_nums:
        print(i,end=' ')
else:
    print(nums[0])

# 2.5.11
nums = [int(i) for i in input().split()]
answer_list = []
nums.sort()
num_old = nums[0]
count = 1
for i in range(1, len(nums)):
    if nums[i] != num_old:
        if count > 1:
            answer_list += [num_old]
        num_old = nums[i]
        count = 1
    else:
        count += 1
if count > 1:
    answer_list += [num_old]
for i in answer_list:
    print(i, end=' ')
