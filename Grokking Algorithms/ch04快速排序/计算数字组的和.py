# 实现方法1
print(sum([1, 2, 3, 4]))
# 或者
def sumnum(array):
    if len(array) == 0:
        return None

    total = 0
    for i in array:
        total += i
    return total

print(sumnum([1, 2, 3, 4]))

# 4.1 4.1 请编写前述 sum 函数的代码
def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

print(sum([2, 4, 6]))

# 4.2 编写一个递归函数来计算列表包含的元素数。
def num(list):
    if list == []:
        return 0
    return 1 + num(list[1:])

print(num([2, 4, 6]))
# 4.3 找出列表中最大的数字

def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max
print(max([2, 4, 6]))