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