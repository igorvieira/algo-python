list1 = [2, 4]
list2 = [1, 3]


for i in range(len(list1)):
  for j in range(len(list2)):
    if(i%2 == 0 and j%2 != 0):
      print(list1[i] + list2[j])



