'''
任何序列(或可迭代的对象)都可以通过一个简单的赋值操作来分解为单独的变量。
唯一的要求是变量的总数和结构要与序列相吻合
'''
p = (4, 5)
x, y = p
print(x)
print(y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, pirce, date = data
print(name)
print(date)

name, shares, price, (year, mon, day) = data
print(name)
print(year)
print(mon)
print(day)

# 如果元素不匹配，将得到一个错误
# ValueError: not enough values to unpack
# p = (4, 5)
# x, y , z = p

# 只要对象恰好是可迭代的，那么就可以执行分解操作
s = 'Hello'
a, b, c, d, e = s
print(a)
print(b)
print(e)

'''
分解操作时，丢弃某些特定的值可以选一个用不到的变量名,
以此来作为要丢弃的值的名称
'''
# 确保选择的变量名没有在其他地方用到过
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print(shares)
print(price)