
age=int(input("请输入你家狗狗的年龄："))
# 这里
if age<=0:
    print("erro!")
elif age==1:
    print("相当于 14 岁的人。")
elif age==2:
    print("相当于 22 岁的人。")
elif age>2:
    human=22+(age-2)*5
    print("对应人类年龄: ",human)

#     判断 input 默认设置的数据类型
inp=input("输入一个数，判断 input 默认设置的数据类型：")
print(type(inp))
# 默认是 字符串
