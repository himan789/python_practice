#8-1消息
from pydoc import describe
from statistics import quantiles
from this import d


def display_message():
    """显示这章学的什么"""
    print('This page tell us function.')
display_message()
#8-2喜欢的图书
"""title为形参"""
def favorite_book(title):
    print('One of my favorite books is '+title.title()+' .')
"""hackers with painters为实参"""
favorite_book('hackers with painters')
#8-3T恤
def make_shirt(size,typeface):
    print('The t-shirt size is '+size)
    print('The t-shirt typeface is '+typeface)
'关键字实参'
make_shirt(size='small',typeface='Life is short,I use Python!')
#8-4大号T恤
'默认值'
def make_shirt(size='Large',typeface='I love Python!'):
    print('The t-shirt size is '+size)
    print('The t-shirt typeface is '+typeface)
make_shirt()
'默认中号'
def make_shirt1(size='middle',typeface='I love Python!'):
    print('The t-shirt size is '+size)
    print('The t-shirt typeface is '+typeface)
make_shirt1()
'默认字样'
def make_shirt2(size,typeface='I love Java!'):
    print('The t-shirt size is '+size)
    print('The t-shirt typeface is '+typeface)
make_shirt2(size='small')
#8-5城市
def describe_city(city,country='China'):
    print(city+' in '+country)
describe_city(city='Chongqing')
describe_city(city='Chengdu')
describe_city(city='Tokyo')
#8-6城市名
def city_country(city,country):
    city_countrys=[city,country]
    return city_countrys
print(city_country(city='Chongqing',country='China'))
print(city_country(city='Chengdu',country='China'))
print(city_country(city='Newyork',country='China'))
#8-7专辑
def make_ablam(name,ablam):
    ablamlist={'name':name.title(),'ablam':ablam.title()}
    return ablamlist
print(make_ablam(name='jay',ablam='the greant artist'))
print(make_ablam(name='michale',ablam='bit'))
print(make_ablam(name='aiver',ablam='love'))
#歌曲数
def make_ablam1(name,ablam,quantity):
    ablamlist1={'name':name.title(),
                'ablam':ablam.title(),
                }
    if quantity:
        ablamlist1['quantity']=quantity
    return ablamlist1
print(make_ablam1(name='aiver',ablam='love',quantity=0))
print(make_ablam1(name='aiver',ablam='hate',quantity=6))
#8-8用户的专辑
def make_ablam2(name,ablam,quantity):
    ablamlist2={'name':name.title(),
                'ablam':ablam.title(),
                }
    if quantity:
        ablamlist2['quantity']=quantity
    return ablamlist2
while True:
    singer=input("singer'name: ")
    if singer=='quit':
        break
    ablam_name=input('the ablam name:' )
    if ablam_name=='quit':
        break
    quantities=input('quantity: ')
    if quantities=='quit':
        break
    print(make_ablam2(singer,ablam_name,quantities))

#8-9魔术师
magicians=['jay','liuqian','kobe']
def show_mahicians(names):
    for name in names:
        print(name)
show_mahicians(magicians)
#8-9了不起的魔术师
the_great_magicians=[]
def make_great():
    while magicians:
        the_great_magicians=magicians.pop()
        print('The Great:'+the_great_magicians)
make_great()
'''原列表没有了'''
show_mahicians(magicians)
#8-10不变的魔术师
def make_great1():
    '''复制'''
    magicians1=magicians[:]
    while magicians1:
        the_great_magicians=magicians1.pop()
        print('The Great:'+the_great_magicians)
make_great1()
'''原列表不变'''
show_mahicians(magicians)
#8-11三明治
def sandwich_tops(*tops):
    '''创建一个元组tops'''
    print('Your sandwich would add :')
    for top in tops:
        print(top)
    print('Your sandwich is ok!')
sandwich_tops('tomato','potato','beef','cheese')
sandwich_tops('red pepper','eggplant','durian','ham')
sandwich_tops('egg','chicken')
#8-12用户简介
def build_profile(first, last, **user_info):
    '''创建一个字典，包含用户的信息'''
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('robert', 'luo',location='chongqing',field='artist',age='30')
print(user_profile)
#8-13汽车
def make_car(maker,size,**tops):
    '''创建一个字典，存放汽车的信息'''
    car_mesg={}
    car_mesg['maker']=maker
    car_mesg['size']=size
    for key,value in tops.items():
        car_mesg[key]=value
    return car_mesg
car=make_car('toyota','suv',color='white',tow_package='True')
print(car)
