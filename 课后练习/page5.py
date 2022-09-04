#条件测试
car="subaru"
print("Is car=='subaru'? I predict True.")
print(car=="subaru")

print("\nIs car =='audi'? I predict Flase.")
print(car=="audi")
#字符串是否相等
a="abc"
b="abc"
if a==b:
    print(True)
c="bcd"
if a!=c:
    print(False)
#首字母大
b="Abc"
if a==b:
    print(True)
if a==b.lower():
    print(True)
#两数比较
d=25
e=24
if d==e:
    print(True)
if d>=20 and e>=25:
    print(True)
if d>=20 or e>=25:
    print(True)
#包含
qwe=[1,2,3,34,46]
if 1 in qwe:
    print("T")
if 4 not in qwe:
    print("f")

#外星人的颜色1
alien_color='green'
if alien_color=='green':
    print('The player can get 5 points' )
if alien_color=='red':
    print('The player can get 0 points')
#外星人的颜色2
alien_color='red'
if alien_color=='yellow':
    print('The player can get 5 points')
else:
    print('The player can get 10 points')
#外星人的颜色3
alien_color='green'
if alien_color=='yellow':
    print('The player can get 10 points')
elif alien_color=='green':
    print('The player can get 5 points')
else:
    print('The player can get 15 points')

#人生的不同阶段
age=66
if age<2:
    print('He is a baby.')
elif age>=2 and age<4 :
    print('He is studying walk.')
elif age>=4 and age<13 :
    print('He is a children.')
elif age>=13 and age<20 :
    print('He is a teeniger.')
elif age>=20 and age<65 :
    print('He is a man.')
else:
    print('He is an old man.')

#喜欢的水果
favorite_fruits=['apple','banana','water malen']
if 'banana' in favorite_fruits:
    print('You really like bananas!')
if 'apple' in favorite_fruits:
    print('You really like apples!')
if 'water malen' in favorite_fruits:
    print('You really like water malens!')
if 'tomato' in favorite_fruits:
    print('You really like tomates!')
if 'potato' in favorite_fruits:
    print('You really like potatoes!')

#特殊方式打招呼
user_lists=['admin','eric','robert','alice','davide']
for user_list in user_lists:
    if user_list=='admin':
        print('Hello admin,would you like to see a status report?')
else:
        print('Hello Eric,thanking you for logging in again.')
#检查列表是否为空
user_lists=[]
if user_lists==[]:
    print('We need to find some users!')

#检查用户名
current_users=['admin','eric','robert','alice','davide']
new_users=['Admin','eric','antoni','james','paul']
current_users_lower=[]
for current_user in current_users:
    current_users_lower.append(current_user.lower())
new_users_lower=[]
for new_user in new_users:
    new_users_lower.append(new_user.lower())
for new_users_lower in new_users_lower:
    if new_users_lower in current_users_lower:
        print(new_users_lower +' you need input other name!')
    else:
        print(new_users_lower +' the name is not used!')

#序数
numbers_list=[1,2,3,4,5,6,7,8,9]
for nuber in numbers_list:
    if nuber==1:
        print('1st')
    elif nuber==2:
        print('2nd')
    elif nuber==3:
        print('3rd')
    elif nuber==4:
        print('4th')
    elif nuber==5:
        print('5th')
    elif nuber==6:
        print('6th')
    elif nuber==7:
        print('7th')
    elif nuber==8:
        print('8th')
    else:
        print('9th')  








