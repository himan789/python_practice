#9-1餐馆
class Restaurant():
    '''创建了一个类'''
    '''特别注意__init__分别是两个下划线'''
    def __init__(self,name,type):
        '''初始化name和type'''
        self.name=name
        self.type=type

    def describe_restaurant(self):
        '''描述餐馆'''
        print(f"The restaurant's name is {self.name.title()}." )
        print(f"The restaurant's type is {self.type.title()}.")

    def open_restaurant(self):
        '''正在营业'''
        print('The restaurant is opening!')
        
my_rest=Restaurant('little room','chinese food')
print(my_rest.name)
print(my_rest.type)
my_rest.describe_restaurant()
my_rest.open_restaurant()
 