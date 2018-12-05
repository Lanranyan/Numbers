'''
Assignment 2
 1)Generate a list of 20 random numbers
    - generate a random num selection
          - from -100, 100
    append the number to your list
 2)Get the min and max of your list
    - using sort
    -
'''

import random # import a library to create random numbers
lost = []

for i in range (20):
    num = random.randint(-100,100)
    lost.append(num)
print(lost)
lost.sort()

print(lost)
print("Minimum is ", lost[0])
print()
print("Maximum is ", lost[-1])



# lost = []
# len(lost) = lost.index()
# if len(lost) == 19:
#     print(len(lost)
# else :
#     num = random.randint(-100,100)
#      mylist.append
# num = random.randint(-100,100)
# print(num)
#
# mylist = []
# mylist.append(num)
# num = random.randint(-100,100)