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

#定义家具类
class jiaju():
    #家具的属性
    def __init__(self,name,area):
        self.name = name
        self.area = area
#定义房子类
class house():
    #房子的属性
    def __init__(self,huxing,area):
        self.huxing = huxing
        self.area = area
        self.free_area = area
        self.jiaju = []
    #定义返回魔法方法
    def __str__(self):
        return f'房子的户型是{self.huxing},房子的面积是{self.area},屋里有家具{self.jiaju},剩余面积还有{self.free_area}'
    #定义方法：添加家具
    def add_jiaju(self,item):
        if self.free_area >= item.area:
            self.jiaju.append(item.name)
            self.free_area -= item.area
        else:
            print('放不下')
if __name__=='__main__':
    bed = jiaju('床',4)
    yigui = jiaju('衣柜',2)
    canzhuo = jiaju('餐桌',1.5)
    room = house('开间',40)
    print(room)
    room.add_jiaju(bed)
    print(room)
    room.add_jiaju(yigui)
    print(room)
    room.add_jiaju(canzhuo)
    print(room)

# 4.士兵开枪
#     需求：
#     1）.士兵瑞恩有一把AK47
#     2）.士兵可以开火(士兵开火扣动的是扳机)
#     3）.枪 能够 发射子弹(把子弹发射出去)
#     4）.枪 能够 装填子弹 --增加子弹的数量

#定义枪类
class gun():
    #枪的属性
    def __init__(self, name, bullet_count):
        self.name = name
        self.bullet_count = bullet_count
        self.max_bullet_count = 20
    #枪的方法：发射子弹
    def shoot(self):
        if self.bullet_count > 0:
            self.bullet_count -= 1
        else:
            print('没有子弹了')
    #枪的方法：装填子弹
    def add_bullet(self):
        if self.bullet_count < self.max_bullet_count:
            self.bullet_count += (self.max_bullet_count-self.bullet_count)
    #定义返回魔法类
    def __str__(self):
        return f'枪名是{self.name},枪里还有子弹{self.bullet_count}发'
#定义士兵类
class soldier():
    #士兵属性
    def __init__(self,xingming,gun_name):
        self.xingming = xingming
        self.gun_name = gun_name
    #士兵的方法：开火,调用枪的发射子弹方法
    def fire(self):
        self.gun_name.shoot()
    #士兵的方法：装子弹，调用枪的装填子弹方法
    def add_bullets(self):
        self.gun_name.add_bullet()

if __name__=='__main__':
    qiang = gun('AK47',15)
    ren = soldier('瑞恩',qiang)
    ren.fire()
    print(qiang)
    ren.fire()
    print(qiang)
    ren.add_bullets()
    print(qiang)






















