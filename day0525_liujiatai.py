"""烤地瓜
需求：1.地瓜烤的时间少于等于2分钟时是生的
     2.地瓜烤的时间大于2分钟小于等于4分钟时半生的
     3.地瓜烤的时间大于4分钟小于等于7分钟时是熟的
     4.地瓜烤的时间大于7分钟时烤糊了
"""
#定义地瓜类
class digua():
    #定义地瓜的属性
    def __init__(self):
        self.cook_time = 0
        self.status = '生的'
    #定义烤地瓜方法
    def cook(self,time):
        self.cook_time += time
        if 0<=self.cook_time<=2:
            self.status = '生的'
        elif 2<self.cook_time<=4:
            self.status = '半生的'
        elif 4<self.cook_time<=7:
            self.status = '熟的'
        elif self.cook_time>7:
            self.status = '糊的'
    #定义魔法方法输出结果
    def __str__(self):
        return f'地瓜烤了{self.cook_time}分钟,地瓜是{self.status}'

a = digua()
a.cook(4.5)
print(a)

