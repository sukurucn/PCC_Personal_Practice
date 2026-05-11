# import p9_1to9_5
# from p9_1to9_5 import  Restaurant #区别引入整个文件和类吗如果引入整个文件整体的程序全部会被执行一遍
from p9_1to9_5 import user
# class IceCreamStand(Restaurant):
#     def __init__(self,restaurant_name,cuisine_type,flavors,num_served=0,):
#         # self.restaurant_name=restaurant_name
#         # self.cuisine_type='IceCream'
#         # self.num_served=num_served
#         super().__init__(restaurant_name,cuisine_type,num_served=0) #super().__innit__ 怎么调用父类初始化
#         self.flavors=[ "香草", "巧克力", "草莓", "抹茶", "芒果"] # 默认变量只能在定义框内定义 初始化再赋值时在刚开始就会因为参数不够报错
#     def icecream_falvors(self):
#         print('冰激凌的口味有',end='')
#         for flavor in self.flavors:
#             print(f'{flavor}')
# ice_shop = IceCreamStand("蜜雪冰城", "冰淇淋甜品",[]) #但是在程序里定义也确实是有用 怎么初始化非常的关键啊我看
#
# ice_shop.icecream_falvors()


# class Admin(user):
#     def __init__(self,first_name,last_name,age,gender,privilege,login_attempts=0,):
#         super().__init__(first_name,last_name,age,gender,login_attempts=0)
#         self.privilege=privilege
#     def show_privilege(self):
#         for prlg in self.privilege:
#             print(f"{prlg}")
# Admin_1=Admin('jixn','wei',26,'female',['add user','delete user','ban user'],3)
#
# Admin_1.describe_user()
# Admin_1.increment_login_attempts()
# Admin_1.reset_login_attempts()
# Admin_1.show_privilege()
class Privilege():
    def __init__(self,privilege):
        self.privilege=privilege
    def show_privilege(self):
        for prlg in self.privilege:
            print(f"{prlg}")

class Admin(user):
    def __init__(self,first_name,last_name,age,gender,privilege,login_attempts=0,):
        super().__init__(first_name,last_name,age,gender,login_attempts)
        self.privilege = Privilege(privilege) # 同过大类的参数来传递给小类参数 直接如此命名
Admin_1=Admin('jixn','wei',26,'female',["add user", "delete user", "ban user"],3,)

Admin_1.describe_user()
Admin_1.increment_login_attempts()
Admin_1.reset_login_attempts()
Admin_1.privilege.show_privilege()

"""A set of classes that can be used to represent electric cars."""

from car import Car  # 重点学习类的继承非常的关键啊


class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=60):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size  # 类的定义内应用使用.

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):  # 直接继承父类的所有方法和变量
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)  # bmw = car.Car('bmw' ,'a5',2010) 一样的内部有个类
        self.battery = Battery()


# 类外的引用使用bwm.name 为了区别变量和方法 变量后不加（） 方法后加入（） 方便引入参数 类很像一系列共用参数的函数的合计 部分需要传入参数 但是拥有基础的公共参数
# 问到点子上了！给你讲透**双下划线 `__` 开头**的规则👇
#
# # 1、`__init__` 也是 `__` 开头，为啥能继承？
# 关键点：
# - `__init__` 是 **Python 内置魔法方法**（系统预留的）
# - **不会被私有隐藏**，正常被子类继承、重写
#
# # 2、真正私有的是：**自己写的 `__xxx`**
# 只要**你自己定义**的、双下划线开头的属性/方法：
# ```python
# class Car:
#     def __secret(self):   # 自己写的 __开头 私有方法
#         print("秘密功能")
# ```
# 这种 **才会被隐藏，子类继承不到、直接调用不了**。
#
# # 3、区分两句话
# 1. **系统魔法方法**：`__init__`、`__str__`、`__del__`
#    自带双下划线，**正常继承、正常重写**。
#
# 2. **自定义私有成员**：自己写 `__name`、`__run`
#    双下划线开头，**自动私有化，子类访问不到**。
#
# # 4、极简总结
# - `__init__` 是**系统特殊方法**：虽有 `__`，但**能继承**
# - 你自己写的 `__xxx`：**才是私有，不能直接继承调用**
#
# 要不要我给你写一段小代码，演示「自定义__私有方法子类调用报错」，你一看就懂？
xiaopeng = ElectricCar('xiaopeng', 'p7', 2025)
xiaopeng.battery.get_range()
xiaopeng.battery.upgrade_battery()
xiaopeng.battery.get_range()