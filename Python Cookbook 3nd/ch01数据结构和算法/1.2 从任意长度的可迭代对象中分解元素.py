'''
需要从某个可迭代对象中分解出 N 个元素,
但是这个可迭代对象的长度可能超过 N,
这会导致出现“分解的值过多
(too many values to unpack)”的异常
'''

# Python *表达式
# def drop_first_last(grades):
#     first, *middle, last = grades
#     return avg(middle)

'''用户记录 记录由姓名和电子邮件地址组成,后面跟着任意
数量的电话号码'''
user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record
print(name)
print(email)
print(phone_numbers)

'''
用一系列的值来代表公司
过去 8 个季度的销售额。
如果想对最近一个季度的销售额同
前7个季度的平均值做比较
'''
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current) # 3

# 元组序列的*
records = [('foo', 1, 2),
           ('bar', 'hello'),
           ('foo', 3, 4)
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# 字符串的拆分(splitting)
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)

# 使用几个常用来表示待丢弃值的变量名
record = ('ACEM', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)

# 列表的分解
items = [1, 10, 7, 4, 5, 9]
head, *tail = items # 分解为头部和尾部
print(head)
print(tail)

# 拆分功能函数
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print(sum(items))