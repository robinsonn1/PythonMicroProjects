a = [3, 10, -1]
print(a)
#add item to the list
a.append(1)
print(a)
#add other types
a.append("hello")
print(a)
#to append another list to the original list
a.append([5,4])
print(a)
#delete the last item
#a.pop()
#print(a)
#first item in the list
#print(a[0])
#modify an item
#a[0]=100
#print(a[0])
#interchange item
a[0], a[2] = a[2], a[0]
print(a)