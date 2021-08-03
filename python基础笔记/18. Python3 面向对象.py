

# 类对象创建
# class MyClass:
#     i=12345
#     def f(self):
#         print(self)
#         # self表示的是 类实例，而非 类
#         return "hello world!"

# x=MyClass()
# 访问 实例属性 及调用其方法
# print("MyClass 类的属性 i 为：", x.i)
# print("MyClass 类的方法 f 输出为：", x.f())



# 单继承初认识

# class people:
#     name=""
#     age=0
#     __weight=0
#     # 两根下划线 开头的 就是 私有
#     def __init__(self,n,a,w):
#         self.name=n
#         self.age=a
#         self.__weight=w
#     def speak(self):
#         print(f"{self.name}说：我{self.age}岁啦")
#
# # 单继承
# class student(people):
#     grade=''
#     def __init__(self,n,a,w,g):
#         people.__init__(self,n,a,w)
#         self.grade=g
#     # 覆写父类方法
#     def speak(self):
#         print(f"{self.name}说：我{self.age}岁,我读{self.grade}啦！")
#
# s1=student("tom",10,60,3)
# s1.speak()




# 多重继承
# 需要注意圆括号中父类的顺序，
# 若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索
# 即方法在子类中未找到时，从左到右查找父类中是否包含方法。

# 例子 就不举了哈哈哈



# 类 还有一些专有的方法
# 不过 还是 根据 需要吧

# 然后 作用域 这个 这里也先不说吧
# 标准库也不说




a = [1,2,3,None,(),[],]

print(len(a))