list1 = [2,4]
list2 = [1,3]
list3 = []


for i in list1:
  for j in list2:
    list3 = [*list3, i*2-j]

print(list3)
