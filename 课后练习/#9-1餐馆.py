#9-1餐馆
class Restaurant():
    """创建了一个类"""
    def _init_(self,name,type):
        '''初始化name和type'''
        self.name=name
        self.type=type

    def describe_restaurant(self):
        '''描述餐馆'''
        print("The restaurant's name is {self.name.title()}." )
        print("The restaurant's type is {self.type.title()}.")

    def open_restaurant(self):
        '''正在营业'''
        print('The restaurant is opening!')
        
my_rest=Restaurant('little room','chinese food')
my_rest.describe_restaurant()