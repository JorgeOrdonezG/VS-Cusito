largest_so_far = -1 #This is a variable
print('Before', largest_so_far)

for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print (largest_so_far, the_num)

print ('After', largest_so_far)

zork = 0
print ('\nBefore', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + 1 
    print (zork, thing)
print ('After', zork)

zork = 0 #Counting loop
print ('\nBefore', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing 
    print (zork, thing)
print ('After', zork)

count = 0 #Average loop
sum = 0 
print ('\nBefore', count, sum)
for value in [9, 41, 12, 3, 74, 15] :
    count = count + 1 
    sum = sum + value 
    print (count, sum, value)
print('After', count, sum, int(sum / count))

#Smallest value in a list
smallest_so_far = None #Flag Value 
print('\nBefore')
for value in [9, 41, 12, 3, 74, 15] :
    if smallest_so_far is None :
        smallest_so_far = value
    elif value < smallest_so_far :
        smallest_so_far = value
    print (smallest_so_far, value)
print ('After', smallest_so_far)


