#7-1汽车租赁
cars=input("can I help you? please enter the car you want: ")
print('Let me see if I can find you a: '+cars.title())
#7-2餐馆定位
people=input("Hou many people this dinner,please enter: ")
peoples=int(people)
if peoples >8 :
    print('So sorry,there is not enough seats!')
else:
    print("Welcone!")
#7-3 10的整数倍
number=int(input("Please enter a number: "))
if number % 10==0:
    print('This number is 10 integer multiple.')
else:
    print('This number is not 10 integer multiple.')
#7-4比萨配料
pizza='Please enter the pizza toppings: '
pizza +="\nyou can enter the quit to finish."
a=''
while a !='quit':
    a=input(pizza)
    print('We can put '+a+' to the pizza! ')
#7-5电影票
ticket=3
active=True
while active:
    age=int(input('Pleasr enter you age:'))
    ticket-=1
 #   if ticket==0:
 #     active=False
    if ticket==0:
        break
    if age < 3:
        print('Free!')
    elif age>=3 and age<=12:
        print('Please pay 10$ !')
    else:
        print('Please pay 15$ !')
     
#7-6熟食店
sandwich_orders=['potato','tomato','chiken']
finished_sandwich=[]
for sandwich_order in sandwich_orders:
    print('I made your '+sandwich_order+' sandwich.')
    finished_sandwich.append(sandwich_order)
print(finished_sandwich)
#7-8五香烟熏牛肉卖完了
sandwich_orders=['pastrami','potato','tomato','pastrami','chiken','pastrami']
print('The pastrami sandwich was sell over.')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders) 
7-9#梦想的度假胜地
#设定一个字典，存放名字和地点
dream_places={}
#建一个标识
active=True
#开始调查
while active:
    name=input("What's your name?")
    place=input('Hi '+name+' ,If you could visit one place in the world,where would you go?')
    #将地点存放到字典
    dream_places[name]=place
    #是否继续调查
    repeat=input('Would you like to let another person respond?(yes/no')
    if repeat=='no':
        active=False
#输出调查结果
for name,place in dream_places.items():
    print('Hi '+name+' you want to visit '+place)






