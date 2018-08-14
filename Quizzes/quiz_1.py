# Written by *** and Eric Martin for COMP9021


'''
Generates a list L of random nonnegative integers at most equal to a given upper bound,
of a given length, all controlled by user input.

Outputs four lists:
- elements_to_keep, consisting of L's smallest element, L's third smallest element,
  L's fifth smallest element, ...
  Hint: use sorted(), list slices, and set()
- L_1, consisting of all members of L which are part of elements_to_keep, preserving
  the original order
- L_2, consisting of the leftmost occurrences of the members of L which are part of
  elements_to_keep, preserving the original order
- L_3, consisting of the LONGEST, and in case there are more than one candidate, the
  LEFTMOST LONGEST sequence of CONSECUTIVE members of L that reduced to a set,
  is a set of integers without gaps.
'''


import sys
from random import seed, randint 


try:
    arg_for_seed, upper_bound, length = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, upper_bound, length = int(arg_for_seed), int(upper_bound), int(length)
    if arg_for_seed < 0 or upper_bound < 0 or length < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, upper_bound) for _ in range(length)]
print('\nThe generated list L is:')
print('  ', L)

L_1 = []
L_2 = []
L_3 = []
elements_to_keep = []

# Replace this comment with your code
elements_to_keep = set(L)
elements_to_keep = list(elements_to_keep)
elements_to_keep.sort()
elements_to_keep = elements_to_keep[0:len(elements_to_keep):2]






for i in range(len(L)):
	if L[i] in elements_to_keep:
		L_1.append(L[i])

for j in range(len(L)):
	if L[j] in elements_to_keep and L[j] not in L_2:
		L_2.append(L[j])
		
L_4=[]
for i in range(len(L)):
	for j in range(len(L)):
		if L[j:i+1]:
			L_4.append(L[j:i+1])

print(L_4)
temp_l=0
count=0
count_len=0
for i in range(len(L_4)):
	temp=list(L_4[i])
	temp_l=len(temp)
	count=0
	if temp_l >= 2:		
		j=min(temp)
		count=0
		while(j<=max(temp)):
			if j in temp:
				count+=temp.count(j)
			else:
				count=0
				break
			j+=1
	else:
		count=0
		pass
	
	
	if count == len(temp) and count > count_len:
		count_len=count
		L_3 = list(temp)
		


		
print('\nThe elements to keep in L_1 and L_2 are:')
print('  ', elements_to_keep)
print('\nHere is L_1:')
print('  ', L_1)
print('\nHere is L_2:')
print('  ', L_2)
print('\nHere is L_3:')
print('  ', L_3)


