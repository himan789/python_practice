from user import User
class Privileges():
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