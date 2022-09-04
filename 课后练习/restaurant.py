class Restaurant():
    '''创建了一个类'''
    '''特别注意__init__分别是两个下划线'''
    def __init__(self,name,type):
        '''初始化name和type'''
        self.name=name
        self.type=type
        self.number_served=0

    def describe_restaurant(self):
        '''描述餐馆'''
        print(f"The restaurant's name is {self.name.title()}." )
        print(f"The restaurant's type is {self.type.title()}.")

    def open_restaurant(self):
        '''正在营业'''
        print('The restaurant is opening!')

    def set_number_served(self):
        '''就餐人数'''
        print(f'The restaurant was {self.number_served}.')
    def increment_number_served(self,number):
        '''就餐人数递增'''
        self.number_served += number