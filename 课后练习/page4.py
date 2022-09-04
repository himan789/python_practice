#4-1披萨
pizzas=['tomato','potato','chiken']
for pizza in pizzas:
    print(pizza)
    print('I like '+pizza+' pizza.')
print('I really love pizza!')
#4-2动物
animals=['dog','cat','pig']
for animal in animals:
    print(animal)
    print('A '+animal+' would make a great pet.')
print('Any of these animals would make a great pet!')
#数字
digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))
#列表解析
squares=[value**2 for value in range(1,11)]
print(squares) 

#4-3用for循环打印数字1~20（含）
for i in range(1,21):
    print(i)

#4-4一百万
numbers=[]
for number in range(1,100):
    numbers.append(number)
print(numbers)
#列表解析一百万
numbers1=[number for number in range(1,100)]
print(numbers1)

#4-5计算1~1000000的总和
numbers2=[number for number in range(1,1000000)]
print(min(numbers2))
print(max(numbers2))
print(sum(numbers2))

#4-6奇数
numbers3=[number for number in range(1,20,2)]
for number in numbers3:
    print(number)

#4-7 3的倍数
numbers4=[value*3 for value in range(1,11)]
for number in numbers4:
    print(number)

#4-8立方
number6=[]
for value in range(1,11):
    number=value**3
    number6.append(number)
print(number6)
#立方解析
numbers5=[value**3 for value in range(1,11)]
for number in numbers5:
    print(number)
#python之禅
import this

#4-10切片
#列表前3
print("The first three in zhe list are:")
print(digits[:3])
#列表中间3
print("Three items from the middle of the list are:")
print(digits[5:8])
#列表最后3
print("The last three items in the list are:")
print(digits[-4:-1])
#4-11列表复制
my_foods=["a","b","c"]
friend_foods=my_foods[:]
my_foods.append("d")
friend_foods.append("e")
print(my_foods)
print(friend_foods)
print("My favorite pizza are:")
for my_food in my_foods:
    print(my_food)
print("My friends pizza are:")
for friend_food in friend_foods:
    print(friend_food)

#4-13元组
foods=("noodles","chikens","tomatoes","potatoes","ice cream")
for food in foods:
    print(food)
# foods[0]="acb"赋不了值
foods=("noodles","chikens","tomatoes","jiliu","feibing")
for food in foods:
    print(food)

