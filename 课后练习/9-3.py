class User():
    '''定义一个类'''
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def describe_user(self):
        print(f"The name is {self.first_name.title()} {self.last_name.title()}. ")
    def greet_user(self):
         print('Hi,nice to me to!')
my_name=User('robert','luo')
my_name.describe_user()
my_name.greet_user()

