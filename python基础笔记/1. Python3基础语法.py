# 1.终端 python -V 显示 安装Python版本
    # 或者也可以 搜索 idle ，打开交互界面，也可以看到版本信息

# 2.需要先去 官网 下载Python(解释器)，pycharm 只是一个编辑器吧好像

# 3.打印 python 保留字
#     import keyword
#     keyword.kwlist
#     一个很奇怪的东西，为什么上面的命令 在 idle 里面能运行，在 pycharm里面就跑不了了。
#     查到了 得用 下面这个才行
#     print(keyword.kwlist)


# 4.Python 注释

# 5.行与缩进
#     缩进相同的行就是 表示 是一个代码块
#     如缩进不一致，则会报错


# 6.多行语句
#     6.1 如果语句很长，我们可以 用 \ 来实现多行语句
# total=1+2+3+4\
#     +5+6\
#     +2
# print(total)

#     6.2 但是 如果是 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \
# total_again=[1,2,3
#              ,4,5,
#              6]
# print(total_again)

# 7.数字类型
# int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
# bool (布尔), 如 True。
# float (浮点数), 如 1.23、3E-2
# complex (复数), 如 1 + 2j、 1.1 + 2.2j

# 8.字符串

# 8.0 单行字符串

# 8.1 多行字符串--用 三引号，(''' 或 """)
# word = '字符串'
# sentence = "这是一个句子。"
# paragraph = """这是一个段落，
# 可以由多行组成"""
# print(word)
# print(paragraph)
# 注意 print(paragraph) 打印出来 有换行的效果

# 8.2 转义字符
# \ 表示转义，
# 前面加 r 则不会转义，这里的 r 指 raw，即 raw string，原始字符串
# sentence="this is a line with \n 哈哈哈哈"
# sentence=r"this is a line with \n 哈哈哈哈"
# print(sentence)

# -----pycharm 执行 快捷键 是 shift + f10

# 8.3 连接字符串，重复字符串
# str='123456789'
# print(str + '你好',end=' ')
# print("123456789"*2)

# 8.4 python字符串 里面的字符 不能改变
# str="adfd"
# str[1]="s"
# print(str)

# 8.5 字符串截取
# 8.5.1 正着截
# str='123456789'
# 左闭右开，右边界 不会被 截到
# print(str[0:2])
# 8.5.2 反着截
# 注意默认 步长 是 1，这里反着截 需要 设置步长为 -1
# 终点 可以省略不写，就是一直到末尾
# print(str[-1::-1])

# 9. 空行也是 程序的一部分

# 10.等待用户输入
# input("按下 enter 键后退出")

# 11.一条语句结尾
# 如一条语句占一行，则不需要在末尾加上任何东西
# 如多条语句占一行，需要在 每一条 语句后面 都加上 分号 ；

# 12.import 与 from...import
# 在 python 用 import 或者 from...import 来导入相应的模块。
#
# 将整个模块(somemodule)导入，格式为： import somemodule
#
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
#
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
#
# 将某个模块中的全部函数导入，格式为： from somemodule import *

# import sys
# print('================Python import mode==========================')
# print ('命令行参数为:')
# for i in sys.argv:
#     print (i)
# print ('\n python 路径为',sys.path)

# from sys import argv, path  # 导入特定的成员
#
# print('================python from import===================================')
# print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path



