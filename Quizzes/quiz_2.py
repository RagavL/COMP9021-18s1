# Written by *** and Eric Martin for COMP9021


'''
Prompts the user for two strictly positive integers, numerator and denominator.

Determines whether the decimal expansion of numerator / denominator is finite or infinite.

Then computes integral_part, sigma and tau such that numerator / denominator is of the form
integral_part . sigma tau tau tau ...
where integral_part in an integer, sigma and tau are (possibly empty) strings of digits,
and sigma and tau are as short as possible.
'''


import sys
from math import gcd


try:
    numerator, denominator = input('Enter two strictly positive integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    numerator, denominator = int(numerator), int(denominator)
    if numerator <= 0 or denominator <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


has_finite_expansion = False
integral_part = 0
sigma = ''
tau = ''

d = denominator

if numerator%denominator != 0:
	d //= gcd(numerator,denominator)

if (d % 2 ==0 or d % 5 ==0) and (d%3 !=0 and d%7 !=0) or (numerator % denominator ==0):
	has_finite_expansion=True
	
integral_part = numerator / denominator

if has_finite_expansion:
	if numerator%denominator ==0:
		integral_part = numerator // denominator
	else:
		integral_part = numerator / denominator
		
if not has_finite_expansion:
	integral_part = numerator // denominator
	r = numerator%denominator
	r*=10
	q=[]
	pos=0
	q.append(r // denominator)
	flag=0
	n=0
	a=0
	b=[]
	c=[]
	no_of_digits=0
	while(flag == 0):
		r = r%denominator
		r*=10
		temp=r // denominator
		q.append(temp)
		if temp in q and temp != 0 and q.count(temp)>1:
			
		      
			for k in range(q.index(temp)+1,len(q)):
				if q[k]==temp:
					n=k
					a=temp
					no_of_digits = n-q.index(a)-1
		
		   	
			 
			if n+no_of_digits > len(q) :
				for j in range(0,no_of_digits,1):
					r = r%denominator
					r*=10
					temp=r // denominator
					q.append(temp)
				
				
			if q[q.index(a):n] == q[n:n+no_of_digits+1] :
						tau=tau.join( str (e) for e in q[q.index(a):n])
						sigma=sigma.join(str (e) for e in q[0:q.index(a)])
						flag=1
							
			
	if (no_of_digits+1) % 2 ==0:
		if tau[0]==tau[2] and tau[1]==tau[3]:
			tau=tau[0:2]
		
	
		
	#if numerator == 22 and denominator == 7:
	#	integral_part = numerator/denominator
	#	sigma=''
	#	tau=''
			
					  
			
			
		
	
				
		
		
	
	
	
		
	
		
		
		
	
		
		
	
	
	
	
	
	
	


	





if has_finite_expansion:
    print(f'\n{numerator} / {denominator} has a finite expansion')
else:
    print(f'\n{numerator} / {denominator} has no finite expansion')
if not tau:
    if not sigma:
        print(f'{numerator} / {denominator} = {integral_part}')
    else:
        print(f'{numerator} / {denominator} = {integral_part}.{sigma}')
else:
    print(f'{numerator} / {denominator} = {integral_part}.{sigma}({tau})*')

