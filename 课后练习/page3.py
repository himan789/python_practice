#3-1姓名
names=['james','kobe','wade','curry']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
#3-2问候语
print(names[0].title()+' how are you old friend.')
print(names[1].title()+' how are you old friend.')
print(names[2].title()+' how are you old friend.')
print(names[3].title()+' how are you old friend.')
#3-3自己的列表
drivers=['car','bycycle','moto','walk']
print("I would like to own a "+drivers[0])
print("I would like to own a "+drivers[1])
print("I would like to own a "+drivers[2])
print("I would like to own a "+drivers[3])
#3-4嘉宾名单
friend_lists=['kobe','james','wade']
print('Hi '+friend_lists[0].title()+', would you like to my diner.')
print('Hi  '+friend_lists[1].title()+', would you like to my diner.')
print('Hi  '+friend_lists[2].title()+', would you like to my diner.')
#3-5修改嘉宾名单
print("Kobe doesn't come  the diner.")
friend_lists[0]='curry'
print(friend_lists)
print('Hi '+friend_lists[0].title()+', would you like to my diner.')
print('Hi  '+friend_lists[1].title()+', would you like to my diner.')
print('Hi  '+friend_lists[2].title()+', would you like to my diner.')
#3-6添加嘉宾
print("I find a big table,so we can ask three new friends.")
friend_lists.insert(0,'davis')
friend_lists.insert(2,'harden')
friend_lists.append('iverson')
print('Hi '+friend_lists[0].title()+', would you like to my diner.')
print('Hi  '+friend_lists[1].title()+', would you like to my diner.')
print('Hi  '+friend_lists[2].title()+', would you like to my diner.')
print('Hi '+friend_lists[3].title()+', would you like to my diner.')
print('Hi  '+friend_lists[4].title()+', would you like to my diner.')
print('Hi  '+friend_lists[5].title()+', would you like to my diner.')
#3-7缩减名单
#餐桌无法及时到达，只能邀请两位朋友
print("I'm so sorry friends,because the table don't come soon,so this time only two friends can visit the diner.")
#删除4位
print("Dear "+friend_lists.pop().title()+" so sorry this time don't have a nice time with you.")
print("Dear "+friend_lists.pop().title()+" so sorry this time don't have a nice time with you.")
print("Dear "+friend_lists.pop().title()+" so sorry this time don't have a nice time with you.")
print("Dear "+friend_lists.pop().title()+" so sorry this time don't have a nice time with you.")
#剩下2位发出邀请
print("Dear "+friend_lists[0].title()+" wlecome to my home,see you soon.")
print("Dear "+friend_lists[1].title()+" wlecome to my home,see you soon.")
#删除剩下2位
del friend_lists[0]
del friend_lists[0]
print(friend_lists)
#3-8放眼世界
places=["beijing","shanghai","guangzhou","kunming","chengdu"]
#原始旅游地
print(places)
#按照字母排序旅游地
print(sorted(places))
#核实排序是否改变
print(places)
#按照字母倒序排列
print(sorted(places,reverse=True))
#核实排序是否改变
print(places)
#用reverse倒序排列
places.reverse()
print(places)
#用reverse恢复
places.reverse()
print(places)
#用sort按字母排序
places.sort()
print(places)
#核实是否改变
print(places)
#用sort按字母倒序排列
places.sort(reverse=True)
print(places)
#核实
print(places)
#有几个想去的地方
print(len(places)) 
#有意引发错误,超出列表长度
print(places[4]) 


