total=0
j=1 #must initialized
while j<5:
    total += j
    j += 1
print(total)
#given list get the positives
given_list=[5, 4, 4, 3, 1, -2, -3, -5]
total2=0
i=0 #needs to be zero for the firt item in the list
while given_list[i] > 0:
    total2 += given_list[i]
    i += 1
print(total2)
#previous only works when including the negatives, because of the >0
#if you take out the negatives when the while loop gets given_list[5] it is an error
#
given_list2=[5, 4, 4, 3, 1]
total3=0
i=0
while i < len(given_list2) and given_list2[i] > 0:
    total3 += given_list2[i]
    i += 1
print(total3)
#now he same thing with for loop and break
given_list3=[5, 4, 4, 3, 1, -2, -3, -5]
total4=0
for element in given_list3:
    if element <= 0:
        break
    total4 += element
print(total4)
#
given_list4=[5, 4, 4, 3, 1, -2, -3, -5]
total5=0
i=0 #index
while True:
    total5 += given_list4[i]
    i += 1
    if given_list4[i] <= 0:
        break
print(total5)
#while sum of negatives
j=0
total_even=0
total_odd=0
given_list5=[5, 4, 4, 3, 1, -2, -3, -5]
while len(given_list5)>j:
    if given_list5[j]>0:
        total_even = total_even+given_list5[j]
    elif given_list5[j]<0:
        total_odd = total_odd+given_list5[j]
    j += 1
print(total_even)
print(total_odd)
#for sum of negatives
total_even2=0
total_odd2=0
given_list6=[5, 4, 4, 3, 1, -2, -3, -5]
for k in given_list6:
    if k>=0:
        total_even2 = total_even2+k
    elif k<0:
        total_odd2 = total_odd2+k
print(total_odd2)
print(total_even2)