# 2、小明爱跑步，爱吃东西。
#     1）小明体重75.0公斤
#     2）每次跑步会减肥0.5公斤
#     3）每次吃东西体重会增加1公斤
#     4）小美的体重是45.0公斤

#定义类
class human():
    #人的属性
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
    #定义方法：跑步
    def run(self,n):
        self.weight -= 0.5*n
    #定义方法:吃东西
    def eat(self,m):
        self.weight += 1*m
    #魔法方法返回
    def __str__(self):
        return f'姓名{self.name},体重{self.weight}kg'
if __name__=='__main__':
    ren1 = human('小明',75)
    ren1.run(5)
    ren1.eat(1)
    print(ren1)
    ren2 = human('小美',45)
    ren2.run(1)
    ren2.eat(2)
    print(ren2)
# 3、摆放家具
#     需求：
#     1）.房子有户型，总面积和家具名称列表
#        新房子没有任何的家具
#     2）.家具有名字和占地面积，其中
#        床：占4平米
#        衣柜：占2平面
#        餐桌：占1.5平米
#     3）.将以上三件家具添加到房子中
#     4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表


#家具类
class  jiaJ():
    #家具属性
    def __init__(self,name,mianji):
        self.name = name
        self.mianji = mianji
#房子类
class room():
    #房子属性
    def __init__(self,huxing,area,jiaju):
        self.huxing = huxing
        self.area = area
        self.jiaju = []
        self.free_area = area
    #方法：添加家具
    def add_jiaju(self,item):
        if self.free_area>= item.mianji:
            self.free_area -= item.mianji
            self.jiaju.append(item.name)
        else:
            print('放不下')
    #魔法方法返回房子现状
    def __str__(self):
        return f'房子户型是{self.huxing},房子总面积是{self.area}平方米,屋内家具有{self.jiaju},房子剩余面积是{self.free_area}平方米'
if __name__ == '__main__':
    house = room('卧室',30,[])
    bed = jiaJ('床',4)
    print(house)
    house.add_jiaju(bed)
    print(house)
    yigui = jiaJ('衣柜',2)
    house.add_jiaju(yigui)
    print(house)
    desk = jiaJ('餐桌',1.5)
    house.add_jiaju(desk)
    print(house)


