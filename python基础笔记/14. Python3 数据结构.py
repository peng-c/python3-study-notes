
# 首先 是 列表的一些内嵌方法嘛


# 然后 列表 还可以 当成 堆栈来使用

# stack=[3,4,5]
# stack.append(6)
# stack.append(7)
# print(stack)
#
# print(stack.pop())
# print(stack)


# 将列表  当做 队列 来用

# from collections import deque
# # deque可以在双向实现 插入或者删除
# queue=deque(["Eric", "John", "Michael"])
# queue.append("Terry")
# queue.append("Graham")
# print(queue.popleft())
# print(queue.popleft())
# print(queue)


# 列表推导式，
# 说白了，其实 就是 在原有列表的基础上 做一些 筛选 或者 是处理


# 列表 嵌套，其实也就是  多维数组 嘛
# matrix=[
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
#
# print(matrix)
# print(matrix[0][0])
# for i in matrix:
#     for j in i:
#         print(j,end=' ')
#     print("\n")


# del 语句
# 使用 del 语句可以从一个列表中依索引而不是值来删除一个元素。这与使用 pop() 返回一个值不同。
# 可以用 del 语句从列表中删除一个切割，或清空整个列表（我们以前介绍的方法是给该切割赋一个空列表）。

# a=[1,2,3,4,5,6,7,8]
# del a[0]
# print(a)
#
# del a[2:4]
# print(a)


# 然后 元组和序列 集合 字典 这些 就不再说了



# 遍历技巧得重视一下

# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来：
# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k,v in knights.items():
#     print(k,v)

# 序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
# for i,v in enumerate(['tic', 'tac', 'toe']):
#     print(i,v)

# for i,v in enumerate("string"):
#     print(i,v)

# 同时遍历两个或更多的序列，可以使用 zip() 组合：
# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q,a in zip(questions,answers):
#     print('What is your {0}?  It is {1}.'.format(q, a))

# format()方法的使用得注意下
# 参考：https://www.runoob.com/python/att-string-format.html
# 除了 上面 这种用得比较多外，保留多少位小数 也是很常见的

# print("{:.2f}".format(3.1415926))


# 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数：
# for i in reversed(range(1,10,2)):
#     print(i)


# 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值：
# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for f in basket:
#     print(f)



