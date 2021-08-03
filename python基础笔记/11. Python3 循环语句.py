# while 循环
# 同样需要注意冒号和缩进。另外，在 Python 中没有 do..while 循环

# a=1
# while a<10:
#     print(a,end=' ')
#     a+=2

# 用while 计算 1到100的总和

# a,sum=0,0
# while a<=100:
#     sum+=a
#     a+=1
# print(sum)

# while 循环使用 else 语句
# 如果 while 后面的条件语句为 false 时，则执行 else 的语句块。

# count = 0
# while count < 5:
#    print (count, " 小于 5")
#    count = count + 1
# else:
#    print (count, " 大于或等于 5")


# for 语句

# for循环用来遍历
# languages=["c","c++","perl","python"]
# for item in languages:
#     print(item)


# range()函数 也值得注意一下

# for i in range(5):
#     print(i)

# 还可以指定区间,左闭右开
# for i in range(1,5):
#     print(i)

# 还可以指定增量
# for i in range(1,10,2):
#     print(i)


# 还可以结合 range() 和 len() 来遍历一个序列的索引
# a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
# for i in range(len(a)):
#     print(i,a[i])
# 这里用print同时输出多个变量，中间用 逗号 分隔


# 然后 是 while 中使用 break 和 continue 和
# for 中使用 break 和 continue
# a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
# for i in a:
#     print(type(i))
#     print(i,len(i))
# 这个地方挺奇怪，len（i）这个函数用在这里就挺奇怪的，而且数还没有规律
# 哦哦，我知道了，傻了傻了，i 是循环项嘛，然后 len()就是计算每一个循环项的长度嘛，
# 这里每个循环项都是 字符串


# 然后 有一个 格式化 输出，这里也写一下
# a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
# for item in a:
#     print(f"hello,{item}")



