# 1. 允许多个变量同时赋值
# a=b=c=1
# d,e,f=1,2,'shuaige'
# print(a,b,c,d,e,f)

# ----坑：注意是执行 现在 这个文件-------

# 2. 标准的数据类型
# Number（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Set（集合）
# Dictionary（字典）

# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

# 这里的 可变 和不可变 ，可以这样来看
# 字符串str 里面的元素 不能更改 ，同理 元组也是一样的道理，然后 可变 自然也就好理解了
# str="abcd"
# str[0]="2"
# print(str)

# 但是还有一个 就是 number 不可变 是什么意思
# 我们要知道在 Python 中，如果数据相同 是 不会 重复开辟空间的。
# 就是 说
# number1=111
# number2=111
# print("number1的地址：",id(number1))
# print("number2的地址：",id(number2))
# number1 和 number2 的地址 是相同的
# 只有 数据不同了 ，才会 再次开辟内存空间
# 所以 也就 没有覆盖 一说，所以 number 就是不可变的

# 3. number类型
# isinstance 和 type 都可用来判断类型
# isinstance 和 type 的区别在于：
#
# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。
# bool 是 int 的子类

# 然后 记住 两个特殊的 数值运算吧
# 乘方 **
# 除法，向下取整 //

# 4.string类型
# 涉及到的内容之前都有提到



# 5. list 列表

# 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。

# 列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
#
# 列表是写在方括号 [] 之间、用逗号分隔开的元素列表。

# 同样 列表 也能用 + 实现 列表连接 ，用  * 实现 列表重复


# 6. Tuple（元组）
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
# 元组也可以使用+操作符进行拼接

# 7. Set（集合）
# 集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
#
# 基本功能是进行成员关系测试和删除重复元素。
#
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

# sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu', 'Runoob'}
# print(sites)   # 输出集合，重复的元素被自动去掉

# # 成员测试
# if 'Runoob' in sites :
#     print('Runoob 在集合中')
# else :
#     print('Runoob 不在集合中')


# set可以进行集合运算
# a = set('abracadabra')
# b = set('alacazam')
#
# print(a)
#
# print(a - b)     # a 和 b 的差集
#
# print(a | b)     # a 和 b 的并集
#
# print(a & b)     # a 和 b 的交集
#
# print(a ^ b)     # a 和 b 中不同时存在的元素



# 8. Dictionary（字典）

# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
#
# 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
#
# 键(key)必须使用不可变类型。
#
# 在同一个字典中，键(key)必须是唯一的。

# tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
#
# print (tinydict)          # 输出完整的字典
# print(tinydict["site"])   # 输出键为 site 对应的值
# print (tinydict.keys())   # 输出所有键
# print (tinydict.values()) # 输出所有值

# 9. Python 数据类型转换

# 10. Python 注释
# 单行注释 是 #
# 多行注释 是 “””我是内容 “””
# 我们之前提到 多行字符串 也是 用 三引号。

# 注释：
"""
我是注释
"""

# 我是多行字符串
# sentence="""lalalalalallalal,
# jfdfkslfks,jsdls
# sjfks
# """


# 11. Python3的运算符
"""
算术运算符

比较运算符

赋值运算符

位运算符

逻辑运算符
and or not

成员运算符
in
not in

身份运算符
is
not is

运算符优先级
"""






