# Written by Ragavendran Lakshminarasimhan for COMP9021

import sys
import re
import copy

filename = input('Which data file do you want to use? ')
try:
    file = open(filename)
    do_L=[]
    L=[]
    Read=file.readlines()
    
    if (Read==[]):
        raise ValueError
        sys.exit()
    for line in Read:
        data = line.split()
        do_L.append(data)
    for i in do_L:
        temp=[]
        for j in i:
            temp.append(int(j))
            
        L.append(temp)
except IOError:
    print('Incorrect input!')
    sys.exit()
except ValueError:
    print('Incorrect input, giving up!')
    sys.exit()
file.close()

rec=[]
for i in range(len(L)-1,-1,-1):
    i_re=len(L)-i-1
    
    line=[]
    for j in range(0,len(L[i])):
        
        
        global m
        m=i+1
        global n
        n=j+1
        if(i+1==len(L)):
            line.append([L[i][j],1,[L[i][j]]])
            
                   
        if( i+1<len(L) and rec[i_re-1][j][0]==rec[i_re-1][j+1][0]):
            sum_v=L[i][j]+rec[i_re-1][j][0]
            line.append([sum_v,rec[i_re-1][j][1]+rec[i_re-1][j+1][1],copy.deepcopy(rec[i_re-1][j][2])])
            line[j][2].append(L[i][j])
         
            
        if( i+1<len(L) and rec[i_re-1][j][0]<rec[i_re-1][j+1][0]):
            sum_v=L[i][j]+rec[i_re-1][j+1][0]
            line.append([sum_v,rec[i_re-1][j+1][1],copy.deepcopy(rec[i_re-1][j+1][2])])
            line[j][2].append(L[i][j])
           
        if( i+1<len(L) and rec[i_re-1][j][0]>rec[i_re-1][j+1][0]):
            sum_v=L[i][j]+rec[i_re-1][j][0]
            line.append([sum_v,rec[i_re-1][j][1],copy.deepcopy(rec[i_re-1][j][2])])
            line[j][2].append(L[i][j])
    rec.append(copy.deepcopy(line))
    

final=rec[-1][-1][-1]

seq=[]
for i in range(len(final)-1,-1,-1):
    seq.append(final[i])

print('The largest sum is:',rec[-1][-1][0])
print('The number of paths yielding this sum is:',rec[-1][-1][1])
print('The leftmost path yielding this sum is:',seq)
