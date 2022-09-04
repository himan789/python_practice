class User():
    '''定义一个类'''
    def __init__(self,first_name,last_name,login_attempts):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=0
        
    def describe_user(self):
        '''描述姓名'''
        print(f"The name is {self.first_name.title()} {self.last_name.title()}. ")

    def greet_user(self):
        '''打招呼'''
        print('Hi,nice to me to!')

    def increment_login_attempts(self):
        '''登录次数'''
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        '''登录次数重置为0'''
        self.login_attempts = 0

my_name=User('robert','luo',0)
my_name.describe_user()
my_name.greet_user()
#查看login_attempts
print(my_name.login_attempts)
#调用3次
my_name.increment_login_attempts()
my_name.increment_login_attempts()
my_name.increment_login_attempts()
#看是否递增
print(my_name.login_attempts)
#重置login_attempts
my_name.reset_login_attempts()
print(my_name.login_attempts)

