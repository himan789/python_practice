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


class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges=[]
    def show_privileges(self):
        print(f'The admin can: ')
        for privilege in self.privileges:
            print(privilege)
you_name=Admin('robert','xiao')
you_name.privileges=['add post','delet post','ban user']
you_name.show_privileges()

