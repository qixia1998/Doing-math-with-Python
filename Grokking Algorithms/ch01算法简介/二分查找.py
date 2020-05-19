# 二分查找
def binary_search(list, item):
    low = 0
    high = len(list) - 1  # low 和 high用与跟踪要在其中查找的列表部分

    while low <= high:    # 只要范围没缩小到只包含一个元素,就继续循环
        mid = (low + high) // 2 # 检查中间的元素，必须是整除 // ，/会报错
        guess = list[mid]
        if guess == item: # 找到了元素
            return mid
        if guess > item:  # 猜的数字大了
            high = mid - 1
        else:             # 猜的数字小了
            low = mid + 1
    return None           # 没有指定的元素，返回None

my_list = [1, 3, 5, 7, 9] # 测试列表
print(binary_search(my_list, 3)) # 索引从0开始，第二个位置索引为1
print(binary_search(my_list, -1)) # None为空，表示没有找到指定的元素