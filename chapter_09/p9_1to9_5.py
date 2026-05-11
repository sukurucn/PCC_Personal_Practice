class Restaurant():
    def __init__(self,restaurant_name,cuisine_type,num_served=0):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.num_served=num_served
    def descibe_restaurant(self):
        print(f"餐厅的名字是{self.restaurant_name}\n菜品的风格是{self.cuisine_type}")
    def open_restaurant(self):
        print('正在营业 欢迎就餐')
    def set_number_served(self,num_served):
        self.num_served=num_served
        print(f'用餐的人数是{num_served}')
    def increment_number_served(self,increase_num):
        self.num_served+=increase_num
        print(f'用餐的人数是{self.num_served}')

kfc= Restaurant ('kkffcc','快餐店')
kfc.descibe_restaurant()
kfc.open_restaurant()
mdd=Restaurant ('mmdddd','快餐店')
lxj=Restaurant ('老乡鸡','人民食堂')
mdd.descibe_restaurant()
lxj.descibe_restaurant()
lxj.set_number_served(100)
lxj.increment_number_served(20)

class user():
    def __init__(self,first_name,last_name,age,gender,login_attempts=0):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.gender=gender
        self.login_attempts=login_attempts
    def describe_user(self):
        if (self.gender=='male'):
            genderinfo='男士'     #所有内部的参数引用 需要self踏踏实实self
        else:
            genderinfo="女士"
        print(f'你好{genderinfo}，这边看到你的资料你的名字是{self.first_name.title()} {self.last_name.title()},年纪是{self.age}周岁')
    def increment_login_attempts(self):
        self.login_attempts+=1
        print(f'当前的尝试次数为{self.login_attempts}')
    def reset_login_attempts(self):
        self.login_attempts=0
        if(self.login_attempts==0):
            print('已归零')


limei=user('li','mei',27,'female')
limei.describe_user()
limei.first_name='cheng'
limei.describe_user()
i=0
while True:
    i+=1
    limei.increment_login_attempts()
    if i>=3:
        break
limei.reset_login_attempts()
