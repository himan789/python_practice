#2-1简单消息
message='Hello,my friend!'
print(message)
#2-2修改上一条消息
message='Hello,python world!'
print(message)
#2-3个性化消息
name='James'
print("Hello "+name+" ,would you like to learn some python today?")
#2-4调整大小写
name='kobe'
#全部大写
print(name.upper())
#全部小写
print(name.lower())
#只首字母大写
print(name.title())
#2-5名言
great_words="Albert Einstein once said,'A person who never made a mistake never tried anything new.'"
print(great_words)
#2-6名言2
famous_person='Albert Einstein'
message="'A person who never made a mistake never tried anything new.'"
print(famous_person+'once said, '+message)
#2-7剔除人名中的空白
a_man=' \twade '
print(a_man.lstrip())
print(a_man.rstrip())
print(a_man.strip())
#2-8数字8
print(2+6)
print(10-2)
print(2*4)
print(16/2)
#2-9最喜欢的数字
favorite_number='8'
message='My favorite number is '
print(message+favorite_number)