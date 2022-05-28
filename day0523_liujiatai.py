#1.pdf while练习
# 输出10个*
# i=0
# while i<11:
#     print('*')
#     i+=1

#2.while 练习2,求100以内累加和
# i=0
# n=0
# while i<=100:
#     n+=i
#     i+=1
# print(n)

#3.while练习，求100以内偶数累加和
# i=1
# add=0
# while i<=100:
#     if i%2 == 0:
#         add+=i
#     i+=1
# print(add)

#4.while条件下break和continue
#break
# i=0
# while i<=5:
#     if i == 4:
#         print('吃饱了')
#         break
#     i+=1
#     print(f'吃了{i}个苹果')
#continue
# i=0
# while i<=5:
#     if i == 3:
#         print('遇到虫子跳过')
#         i+=1
#         continue
#     print(f'吃了{i}个苹果')
#     i+=1

#5.while嵌套，用*打印方形
# i=0
# while i<=5:
#     n=0
#     while n<=5:
#         print('*',end="")
#         n+=1
#     print()
#     i+=1

#6.打印行数和*数相等的三角形
# i=0
# while i<=5:
#     n=0
#     while n<=i:
#        print('*',end='')
#        n+=1
#     print()
#     i+=1

#7.打印乘法表
# i=1
# while i<=9:
#     n=1
#     while n<=i:
#         print(f'{i}*{n}={i*n}',end="\t")
#         n+=1
#     print()
#     i+=1

#打印三角形
# for i in range(5):
#     for m in range(i-1):
#         print(end='-')
#     for n in range(i+1):
#         print('* ',end='')
#     print()

#面向对象1、打印小猫爱吃鱼，小猫要喝水
# class cat():
#     def __init__(self):
#         self.food='fish'
#         self.drink='water'
#     def __str__(self):
#         return f'小猫爱吃{self.food},小猫要喝{self.drink}'
# mimi= cat()
# print(mimi)

#面向对象2.小明爱跑步，爱吃东西。
#     1）小明体重75.0公斤
#     2）每次跑步会减肥0.5公斤
#     3）每次吃东西体重会增加1公斤
#     4）小美的体重是45.0公斤
# class human():
#     def __init__(self, name, weight):
#         #定义属性，名字，体重
#         self.name = name
#         self.weight = weight
#     #定义方法 run, eat
#     def run(self,n):
#         self.weight -= 0.5*n
#     def eat(self,m):
#         self.weight += m
#     def __str__(self):
#         return f'{self.name}的体重是{self.weight}kg'
#
#
# if __name__ == '__main__':
#     user1 = human('小明', 75)
#     user1.run(4)
#     user1.eat(1)
#     print(user1)
#
#     user2 = human('小美', 45)
#     user2.run(4)
#     user2.eat(1)
#     print(user2)









