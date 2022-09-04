#人
from tkinter import N, Place


my_friend={'first_name':'james',
            'last_name':'lebron',
            'age':'40',
            'city':'loangles'}
print(my_friend)

#喜欢的数字
favorite_number={'alice':'1','james':'2','jam':'3','curry':'4','kobe':'8'}
print("Alice's favorite number is "+favorite_number['alice'])
print("James's favorite number is "+favorite_number['james'])
print("Jam's favorite number is "+favorite_number['jam'])
print("Curry's favorite number is "+favorite_number['curry'])
print("Kobe's favorite number is "+favorite_number['kobe'])
#用循环打出
for name,number in favorite_number.items():
    print(name.title()+"' favorite number is "+number)
#确认数字相符
if favorite_number['alice']=='2':
        print('Yes')
else:
    print("Wrong")
#词汇表
word_dicts={'print':'output','for':'loop','if':'judge','list':'liebiao','dict':'zidian'}
for word,dict in word_dicts.items():
    print('\n'+word+':'+dict )


#6.1
alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
print(alien_0)
new_points=alien_0['points']
print("You just earned "+str(new_points)+" points!")
#外星人
alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print("Original x_position: "+ str(alien_0['x_position']))
#向右移
#根据外星人当前速度决定将其移动多远
if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    x_increment=3
#新位置等于老位置加上增量
alien_0['x_position']=alien_0['x_position']+x_increment
print("New x_posintion: "+str(alien_0['x_position']))

favorite_languages = {'jen':'python',
                        'sarah':'c',
                        'edward':'ruby',
                         'phil':'python'}
#读取键值对D.items()
for name,language in favorite_languages.items():
    print(name.title()+"'s favorite language is "+language.title()+" .")
#读取字典中的键D.keys()
friends=['phil','sarah']
for name in favorite_languages.keys():
    print(name.title()) 
if name in friends:
    print("Hi "+name.title()+" ,I see your favorite language is "+favorite_languages[name].title()+" !")
#按字母顺序读取字典所有键sorted(D.keys())
for name in sorted(favorite_languages.keys()):
    print(name.title()+" ,thank you for talking the poll.")
#读取字典中的值D.values()
for language in favorite_languages.values():
    print(language.title())
#剔除重复项set()
for language in set(favorite_languages.values()):
    print(language.title())

#6-1人
myfriends={'first_name':'liao',
            'last_name':'yu',
            'age':'30',
            'city':'guangzhou'}
print(myfriends)
print("My old firend "+myfriends['first_name']+myfriends['last_name']+" is "+myfriends['age']+" in "+myfriends['city']+".")
#6-2喜欢的数字
nbastar={'james':'23','kobe':'24','oniel':'8','yaoming':'13','wade':'3'}
print("James likes "+nbastar['james']+' number.')
print("Kobe likes "+nbastar['kobe']+' number.')
print("Oniel likes "+nbastar['oniel']+' number.')
print("Yaoming likes "+nbastar['yaoming']+' number.')
print("Wade likes "+nbastar['wade']+' number.')
if nbastar['james']=='23':
    print('Hi,james,do you like number 23?')
    print('Yes,i do!')
#6-3词汇表
words={'print':'output','if':'condition','for':'loop','break':'stop','end':'over'}
print('print:'+words['print'])
print('if:'+words['if'])
print('for:'+words['for'])
print('break:'+words['break'])
print('end:'+words['end'])
print('\nprint:')
print(words['print'])
#6-4词汇表2
for key,value in words.items():
    print(key+":"+value)
    print(key+'\n'+value) 
#6-5河流
rivers={'changjiang':'china','huanghe':'china','nile':'egypt'}
for key,value in rivers.items():
    print("The "+ key+" runs through "+rivers[key])
    print(key)
    print(rivers[key])
#6-6调查
favorite_languages = {'jen':'python',
                        'sarah':'c',
                        'edward':'ruby',
                         'phil':'python'}
checkers = {'jen':'python',
            'sarah':'c',
            'james':'java',
            'kobe':'c++'}
for checker in checkers:
    if checker in favorite_languages.keys():
        print(f"Hi {checker.title()},thank you!")
    else:
        print(f"Hi {checker.title()},what's your favorite language?")
#6-7人（列表嵌套字典)
liaoyu={'first_name':'liao',
            'last_name':'yu',
            'age':'30',
            'city':'guangzhou'}
lebronjames={'first_name':'james',
            'lasr_name':'lebron',
            'age':'40',
            'city':'loanges'}
micheljordan={'first_name':'jordan',
            'last_name':'michel',
            'age':'50',
            'city':'newyork'}
my_friends=[liaoyu,lebronjames,micheljordan]
for my_friend in my_friends:
    print(my_friend)
#6-8宠物(列表嵌套字典)
pig={'type':'tuzhu',
    'zhuren':'james'}
cat={'type':'jafie',
    'zhuren':'kobe'}
dog={'type':'tugou',
    'zhuren':'wade'}
pets=[pig,cat,dog]
for pet in pets:
    print(pet)
#6-9喜欢的地方（字典嵌套列表）
favorite_places={'james':['beijing','shanghai'],
                'kobe':['guangzhou','qingdao'],
                'wade':['chongqing','chengdu']}
for name,palces in favorite_places.items():
    print(f"{name.title()}'s favorite places is:")
    for place in palces:
        print(place.title())
#6-10喜欢的数字
favorite_number={'alice':[1,2,3],
                'james':[3,4,5,],
                'jam':[7,8,9]}
for name,numbers in favorite_number.items():
    print(f"{name.title()}'s favorite numbers is:")
    for number in numbers:
        print(number)
#6-11城市
cities={'chongqing':{'country':'china','peple':'300millons','other_name':'montun_city'},
        'chengdu':{'country':'china','peple':'400millons','other_name':'panda_city'},
       'newyork':{'country':'america','peple':'500millons','other_name':'beautiful_city'} }
for city_name,message in cities.items():
    country=message['country']
    peple=message['peple']
    other_name=message['other_name']
    print(city_name.title()+" is a city of "+country.title()+" ,have "+peple+" peples ,called "+other_name)


