
# 简单函数应用，输入两个数，返回最大的那个数

# def max(a,b):
#     if b>=a:
#         return b
#     else:
#         return a

# a=input("请输入第一个数：")
# b=input("请输入第二个数：")
# input()同时接收多个数
# a,b=map(int,input("输入a,b空格隔开").split())

# a,b=map(int,input("输入a,b逗号隔开").split(','))
# print(max(a,b))



# 然后 还有一个 参数传递 值得注意一下

# 当传过去的 是 不可变类型 即：数字，字符串，元组 的时候 ，相当于 是传值调用

# 当传过去的 是 可变类型，即：列表，集合，字典的时候，相当于 是 传引用



# 不定长参数
# 参考：https://www.cnblogs.com/liangshian/p/11208899.html

# 第一种 是 以 元组的形式存在，形参是 *name
# 第二种 是 以 字典的形式存在，形参是 **name

# def funA(a,b,*args):
#     print(a)
#     print(b)
#     print(args)
#
# funA(1,2,3,4,45,5)

# def funB(a,b,**args):
#     print(a)
#     print(b)
#     print(args)
# funB(1,2,c=1,d=3,w=4)



# 匿名函数
# 两个数相加
# sum=lambda arg1,arg2:arg1+arg2
# print("相加之后的值为：",sum(10,20))