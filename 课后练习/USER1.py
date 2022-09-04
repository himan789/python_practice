class User():
    '''定义一个类'''
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def describe_user(self):
        print(f"The name is {self.first_name.title()} {self.last_name.title()}. ")
    def greet_user(self):
         print('Hi,nice to meet you!')
#my_name=User('robert','luo')
#my_name.describe_user()
#my_name.greet_user()

"""class Privileges():
    def __init__(self,privileges=[]):
        self.privileges=privileges
    def show_privileges(self):
        print(f'The admin can: ')
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges=Privileges()
"""
#you_name=Admin('robert','xiao')
#you_name.privileges.privileges=['add post','delet post','ban user']
#you_name.privileges.show_privileges()

