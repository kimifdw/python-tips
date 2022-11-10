# 冒泡排序
lastElementIndex = len(list)-1
print(0,list)
for idx in range(lastElementIndex):
    if list[idx]>list[idx+1]:
        list[idx],list[idx+1] = list[idx+1], list[idx]
    print(idx+1, list)