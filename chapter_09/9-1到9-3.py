class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def descibe_restaurant(self):
        print(f"餐厅的名字是{self.restaurant_name}\n菜品的风格是{self.cuisine_type}")
    def open_restaurant(self):
        print('正在营业 欢迎就餐')
kfc= Restaurant ('kkffcc','快餐店')
kfc.descibe_restaurant()
kfc.open_restaurant()
mdd=Restaurant ('mmdddd','快餐店')
lxj=Restaurant ('老乡鸡','人民食堂')
mdd.descibe_restaurant()
lxj.descibe_restaurant()


class user():
    def __init__(self,first_name,last_name,age,gender):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.gender=gender
    def describe_user(self):
        if (self.gender=='male'):
            genderinfo='男士'     #所有内部的参数引用 需要self踏踏实实self
        else:
            genderinfo="女士"
        print(f'你好{genderinfo}，这边看到你的资料你的名字是{self.first_name.title()} {self.last_name.title()},年纪是{self.age}周岁')

limei=user('li','mei',27,'female')
limei.describe_user()
limei.first_name='cheng'
limei.describe_user()
