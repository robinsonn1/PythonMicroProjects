a = ["banana", "apple", "microsoft"]
#using for loop
for element in a:
    print(element)
#for sum of the list
b =[20,10,5]
total =0
for e in b:
    total = total + e
print (total)
#creating a range of numbers
c = list(range(1,5))
print(c)
#using the range in a for
for i in range(1, 5):
    print("aqui", i)
# find the sum of the range
total2=0
for i in range(1,5):
    total2 += i
print(total2)
# compute the sum of multiples of 3 in the range(1,8)
print(list(range(1,8))) #not including 8
total3=0
for i in range(1,8):
    if i % 3 ==0:
        total3 += i
print(total3)
#compute all multiples of 3,5 that are less than 100
total4=0
for i in range(1,100):
    if i%3==0 or i%5==0:
        total4 += i
print(total4)