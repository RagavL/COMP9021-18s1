# Written by Ragavendran Lakshminarasimhan for COMP9021
# Student Number: z5179974



import sys
import math
import statistics
import copy

file_name = input('Which data file do you want to use?')
try:
    file_object = open(file_name)
    L1=[]
    L2=[]
    Read=file_object.readlines()
    if (Read==[]):
        raise ValueError
        sys.exit()
    for line in Read:
        data = line.split()
        
        for i in range(len(data)):
            if i % 2 == 0:
                L1.append(int(data[i]))
                
            else:
                L2.append(int(data[i]))
                
except IOError:
    print('Incorrect input, giving up!')
    sys.exit()
except ValueError:
    print('Incorrect input, giving up!')
    sys.exit()
file_object.close()



max_mean_value = int(statistics.mean(L2))

min_value= int(min(L2))

ave = int((max_mean_value+min_value)/2)

def check(ave):
    outcome=[]
    M=L2[:]
    for j in range(len(M)-1):
        if(M[j]<ave):
            M[j+1] = M[j+1] - (ave-M[j]) - (L1[j+1]-L1[j])
            
        if(M[j]>ave):
          
            if( M[j]-ave > (L1[j+1]-L1[j])):
                M[j+1]=M[j+1] + (M[j]-ave) - ((L1[j+1]-L1[j]))
              
            if( M[j]-ave <= (L1[j+1]-L1[j])):
                pass
        if(M[j]==ave):
            pass
    if(M[-1]>ave):
       return 1
    if(M[-1]<ave):
        return 2
    if(M[-1]==ave):
        return 0
        

temp=0
while check(ave)!=0:
    if(check(ave)==2):
        max_mean_value=ave
        ave=(max_mean_value+min_value)/2
        if(abs(temp-ave)<0.01):
            break
    if(check(ave)==1):
        min_value=ave
        ave=(max_mean_value+min_value)/2
    temp=ave


print('The maximum quantity of fish that each town can have is {}.'.format(int(temp)))
