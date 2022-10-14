list1 = [10,-20,-30,-40,50,-60,-80,90,70,100,-120,-130,-140]
list2 = list(filter(lambda x: True if x>0 else False,map(lambda x: x*-1,list1)))
print(list2)