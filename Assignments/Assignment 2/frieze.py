#Written by Ragavendran Lakshminarasimhan for COMP9021 SEMESTER 1,2018

import os
import numpy as pd
from collections import defaultdict


def validnumbers(array):
    if (array >= 0).all() and (array <=15).all():
        return True 

def valid_lastcolumn(array):
    if (array[:,-1] >=0).all() and (array[:,-1] <=1).all():
        return True 
    else:
        return False

def valid_border_top(array):
     arr=pd.array(array,dtype=int)
     valid=True
     height,length=arr.shape
     for i in range(height):
         for j in range(length):
             if i==0:
                 if north(array[i][j]) or north_east(array[i][j]):
                     valid=False
                     break
     #print(False)
     return valid
 

# =============================================================================
# def valid_border_bottom(array):
#       arr=pd.array(array,dtype=int)
#       valid1=True
#       height,length=arr.shape
#       last_row=array[height-1,:]
#       for i in last_row:
#           if south_east(i):
#               valid1=False
#               break
#       
#       return valid1
# =============================================================================
# 

        
    
    
                    
binary_conversions_dict={'0':[0,0,0,0],'1':[0,0,0,1],'2':[0,0,1,0],'3':[0,0,1,1],'4':[0,1,0,0],'5':[0,1,0,1],'6':[0,1,1,0],'7':[0,1,1,1],'8':[1,0,0,0],'9':[1,0,0,1],'10':[1,0,1,0],'11':[1,0,1,1],'12':[1,1,0,0],'13':[1,1,0,1],'14':[1,1,1,0],'15':[1,1,1,1]}    
def north(point):
    number_in_binary=binary_conversions_dict[str(int(point))]
    if number_in_binary[-1] == 1:
        return True
    else:
        return False

def north_east(point):
    number_in_binary=binary_conversions_dict[str(int(point))]
    if number_in_binary[-2] == 1:
        return True
    else:
        return False

def east(point):
    number_in_binary=binary_conversions_dict[str(int(point))]
    if number_in_binary[-3] == 1:
        return True
    else:
        return False
    
def south_east(point):
    number_in_binary=binary_conversions_dict[str(int(point))]
    if number_in_binary[-4] == 1:
        return True
    else:
        return False

def check_reflection_glided(col_upper_part,col_lower_part):
    arg1=[]
    arg2=[]
    binary_conversions_dict={'0':[0,0,0,0],'1':[0,0,0,1],'2':[0,0,1,0],'3':[0,0,1,1],'4':[0,1,0,0],'5':[0,1,0,1],'6':[0,1,1,0],'7':[0,1,1,1],'8':[1,0,0,0],'9':[1,0,0,1],'10':[1,0,1,0],'11':[1,0,1,1],'12':[1,1,0,0],'13':[1,1,0,1],'14':[1,1,1,0],'15':[1,1,1,1]}
    for e in col_upper_part:
        arg1.append(binary_conversions_dict[str(int(e))])
    
    for e in col_lower_part:
        arg2.append(binary_conversions_dict[str(int(e))])
    arg1=pd.array(arg1)
    arg2=pd.array(arg2)
    col_lower_part=pd.array(col_lower_part,dtype=int)
    h1,l1=arg1.shape
    reflective_array = pd.zeros((h1,l1),dtype=int)
    if arg2[0,l1-1]==1:
        reflective_array[h1-1,l1-1]=1
    for i in range(h1):
        for j in range(l1):
            if (j==1 or j==3) and i==0:
                if arg1[i,j]==1:
                    if j==3:
                        reflective_array[i,j]=1
                    elif j==1:
                        reflective_array[i,j]=1
            elif (j==1 or j==3) and i!=0:
                if arg1[i,j]==1:
                    if j==3:
                        reflective_array[i-1,j]=1
                    elif j==1:
                        reflective_array[i,j]=1 
            elif (j==0 or j==2) and i==0:
                if arg1[i,j]==1:
                    if j==0:
                        reflective_array[i,j+2]=1
                    elif j==2:
                        reflective_array[i,j-2]=1
            elif (j==0 or j==2) and i!=0:
                if arg1[i,j]==1:
                    if j==0:
                        reflective_array[i,j+2]=1
                    elif j==2:
                        reflective_array[i,j-2]=1
    if pd.array_equal(pd.flipud(reflective_array),arg2):
        print(True)
    else:
        print(arg1)
        print(reflective_array)
        print(pd.flipud(arg2))
        print(arg2)
    
    

def check_reflection_horizontal(col_upper_part,col_lower_part):
    
    arg1=[]
    arg2=[]
    binary_conversions_dict={'0':[0,0,0,0],'1':[0,0,0,1],'2':[0,0,1,0],'3':[0,0,1,1],'4':[0,1,0,0],'5':[0,1,0,1],'6':[0,1,1,0],'7':[0,1,1,1],'8':[1,0,0,0],'9':[1,0,0,1],'10':[1,0,1,0],'11':[1,0,1,1],'12':[1,1,0,0],'13':[1,1,0,1],'14':[1,1,1,0],'15':[1,1,1,1]}
    
    for e in col_upper_part:
        arg1.append(binary_conversions_dict[str(int(e))])
    
    for e in col_lower_part:
        arg2.append(binary_conversions_dict[str(int(e))])
    arg1=pd.array(arg1)
    arg2=pd.array(arg2)
    col_lower_part=pd.array(col_lower_part,dtype=int)
    
    h1,l1=arg1.shape
    reflective_array = pd.zeros((h1,l1),dtype=int)
    if arg2[0,l1-1]==1:
        reflective_array[h1-1,l1-1]=1

    for i in range(h1):
        for j in range(l1):
            if (j==1 or j==3) and i==0:
                if arg1[i,j]==1:
                    if j==3:
                        reflective_array[i,j]=1
                    elif j==1:
                        reflective_array[i,j]=1
            elif (j==1 or j==3) and i!=0:
                if arg1[i,j]==1:
                    if j==3:
                        reflective_array[i-1,j]=1
                    elif j==1:
                        reflective_array[i,j]=1 
            elif (j==0 or j==2) and i==0:
                if arg1[i,j]==1:
                    if j==0:
                        reflective_array[i,j+2]=1
                    elif j==2:
                        reflective_array[i,j-2]=1
            elif (j==0 or j==2) and i!=0:
                if arg1[i,j]==1:
                    if j==0:
                        reflective_array[i,j+2]=1
                    elif j==2:
                        reflective_array[i,j-2]=1
                
    
    if pd.array_equal(pd.flipud(reflective_array),arg2):
        return True
    else:
        return False
      
    

    
def glided_horizonta(frieze_data,period):
    
    height,length=frieze_data.shape
    if period %2!=0:
        return False
    else:
        if height % 2 == 0:
            reflection_line=height // 2 +1
            upper_part=frieze_data[0:reflection_line-1,0:period]
            r1,c1=upper_part.shape
            lower_part=frieze_data[reflection_line-1:height,(period//2+1):(period+(period//2))]
            print(lower_part)
            for n in range(c1):
                check_reflection_horizontal(upper_part[0:4,n],lower_part[0:4,n])
            
        else:
            reflection_line=(height) // 2 
            upper_part=frieze_data[0:reflection_line,0:period]
            r1,c1=upper_part.shape
            lower_part=frieze_data[reflection_line+1:height,(period//2):(period+(period//2))]
            print(upper_part)
            print(lower_part)
            for n in range(c1):
                check_reflection_horizontal(upper_part[0:4,n],lower_part[0:4,n])
        
            
        
    

def horizontal_reflection(frieze_data,period):
    ch=0
    height,length=frieze_data.shape
    #print(height)
    
    if height % 2 == 0:
        reflection_line=height // 2 +1
        upper_part=frieze_data[0:reflection_line-1,0:period]
        r1,c1=upper_part.shape
        lower_part=frieze_data[reflection_line-1:height,0:period]
        for n in range(c1):
            if check_reflection_horizontal(upper_part[0:4,n],lower_part[0:4,n]):
                ch+=1
        
    else:
       reflection_line=(height+1) // 2 
       upper_part=frieze_data[0:reflection_line-1,0:period]
       r1,c1=upper_part.shape
       lower_part=frieze_data[reflection_line:height,0:period]
       for n in range(c1):
            if check_reflection_horizontal(upper_part[0:4,n],lower_part[0:4,n]):
                ch+=1
    
    
    if(ch==period):
            return True
    else:
            return False
        

        
        
    
    
    
    


class FileNotFoundError(Exception):
    def __init__(self, message):
        self.message = message

class FriezeError(Exception):
    def __init__(self,message):
        self.message=message

class Frieze:
    def __init__(self,filename,data=None):
        if filename is not None and os.path.isfile(filename):
            self.filename=filename
        else:
            raise FileNotFoundError('File Not Found')
       
        try:
            self.data=pd.loadtxt(self.filename)
        except:
            raise FriezeError('Incorrect input')

        
        try:
         self.height,self.length=self.data.shape
        except ValueError:
            raise FriezeError('Incorrect input')
        if self.height <=2 or self.height >17:
            raise FriezeError('Incorrect input')
        if self.length <5 or self.length >51:
            raise FriezeError('Incorrect input')
        
        if not validnumbers(self.data):
            raise FriezeError('Incorrect input')
            
        if not valid_lastcolumn(self.data):
            raise FriezeError('Input does not represent a frieze')
        
        if not valid_border_top(self.data):
             raise FriezeError('Input does not represent a frieze')
        #if valid_border_bottom(self.data):
             #raise FriezeError('Input does not represent a frieze')
            
            
        
        self.period=self.find_period()
        if self.period is None or self.period <2:
            raise FriezeError('Input does not represent a frieze')
            


    def find_period(self):
        transposed_matrix=self.data.transpose()
        max_possible_period=(self.length-1) //2
        for i in range(2,max_possible_period,1):
           if pd.array_equal(transposed_matrix[0:i],transposed_matrix[(i+1):(2*i)+1]):
                return i+1               
           else:
                pass
    def analyse(self):
        p=self.period
        h_r=horizontal_reflection(self.data,self.period)               
        #print(f'Pattern is a frieze of period {p} that is invariant under translation and vertical reflection only.')
        if h_r == True:
            print(f'Pattern is a frieze of period {p} that is invariant under translation\n        and horizontal reflection only.')
        elif h_r == False:
            print(f'Pattern is a frieze of period {p} that is invariant under translation only.')
            
            
        
    
    def display(self):
        binary_conversions_dict={'0':[0,0,0,0],'1':[0,0,0,1],'2':[0,0,1,0],'3':[0,0,1,1],'4':[0,1,0,0],'5':[0,1,0,1],'6':[0,1,1,0],'7':[0,1,1,1],'8':[1,0,0,0],'9':[1,0,0,1],'10':[1,0,1,0],'11':[1,0,1,1],'12':[1,1,0,0],'13':[1,1,0,1],'14':[1,1,1,0],'15':[1,1,1,1]}
        
        with open(self.filename[:-4] +'.tex', 'w') as latex_file:
            print('\\documentclass[10pt]{article}\n'
          '\\usepackage{tikz}\n'
          '\\usepackage[margin=0cm]{geometry}\n'
          '\\pagestyle{empty}\n'
          '\n'
          '\\begin{document}\n'
          '\n'
          '\\vspace*{\\fill}\n'
          '\\begin{center}\n'
          '\\begin{tikzpicture}[x=0.2cm, y=-0.2cm, thick, purple]', file = latex_file
          )
            #print('% North to South lines',file = latex_file)
            print(f'% North to South lines',file = latex_file)
            #print(self.height,self.length)
            #del L_duplicates[:]
            L_duplicates=[]         
            for i in range(self.length):
                flag=0
                for j in range(self.height):
                    if (j,i) not in L_duplicates:
                        a= binary_conversions_dict[str(int(self.data[j,i]))]
                        if j < self.height-1:
                            b= binary_conversions_dict[str(int(self.data[j+1,i]))]
                        if a[-1]!=0 and b[-1]==1 and flag==0:
                            start_x=i
                            start_y=j-1
                            flag=1
                            L_duplicates.append((j,i))
                            #finish_x=i
                            #finish_y=j
                            #print('\draw(',start_x,',',start_y,') -- (',finish_x,',',finish_y,');',file = latex_file)
                        elif a[-1]==1 and flag==0:
                            start_x=i
                            start_y=j-1
                            L_duplicates.append((j,i))
                            #print(j,start_x,start_y)
                            flag=1
                        elif a[-1]!=1 and flag==0:
                            pass
                        elif (a[-1]==1 and flag==1 and j <self.height):
                            pass
                        elif (a[-1]!=1 and flag==1 and j < self.height):
                            finish_x=i
                            finish_y=j-1
                            L_duplicates.append((j-1,i))
                            print(f'    \draw ({start_x},{start_y}) -- ({finish_x},{finish_y});',file = latex_file);
                            #print('\\draw(',start_x,',',start_y,') -- (',finish_x,',',finish_y,');',file = latex_file)
                            flag=0
                        if (a[-1]==1 and j==self.height-1 and flag==1):
                            finish_x=i
                            finish_y=j
                            L_duplicates.append((j,i))
                            print(f'    \draw ({start_x},{start_y}) -- ({finish_x},{finish_y});',file = latex_file);
                    else:
                        continue
                    
                    #print(self.data[j,i])
                    
                        #print(i,j)
                        
                     
            print('% North-West to South-East lines',file = latex_file)
            i=0
            j=0
            i_actual=0
            j_actual=0
            del L_duplicates[:]
            L_duplicates=[]
            for i in range(self.height):
                flag=0
                j=0
                while (j<self.length):
                    #print(i,j)
                    if (i,j) not in L_duplicates:
                        a= binary_conversions_dict[str(int(self.data[i][j]))]
                        if a[-4]==1 and flag==0:
                            start_x=j
                            start_y=i
                            L_duplicates.append((i,j))
                            i_actual=i
                            j_actual=j
                            i+=1
                            j+=1
                            flag=1
                        elif a[-4]!=1 and flag==1:
                            finish_x=j
                            finish_y=i
                            print(f'    \draw ({start_x},{start_y}) -- ({finish_x},{finish_y});',file = latex_file);
                            L_duplicates.append((i,j))
                            i=i_actual
                            j=j_actual+1
                            flag=0
                        elif a[-4]!=1 and flag==0:
                            j+=1
                        elif a[-4]==1 and flag==1:
                            L_duplicates.append((i,j))
                            j+=1
                            i+=1
                            flag=1
                        elif a[-4]==1 and flag==1 and j==self.length-1:
                            L_duplicates.append((i,j))
                            finish_x=j
                            finish_x=i
                            print(f'    \draw ({start_x},{start_y}) -- ({finish_x},{finish_y});',file = latex_file);
                            j=0
                            i=i_actual
                            flag=0
                        elif a[-4] and flag==1 and i==self.height:
                            L_duplicates.append((i,j))
                            finish_x=j
                            finish_y=i
                            print(f'    \draw ({start_x},{start_y}) -- ({finish_x},{finish_y});',file = latex_file);
                            i=i_actual
                            j=j_actual+1
                            flag=0
                        else:
                            j+=1
            #j+=1   
                    else:
                        j+=1
                    #j+=1
                    #i=i_actual
                    
                    
                    
                    
                        
                
            
            
                    
                  
            
                        
                    
            
            
            
            print('% West to East lines',file = latex_file)
            i=0
            j=0
            flag=0
            for i in range(self.height):
                flag=0
                for j in range(self.length):
                    a= binary_conversions_dict[str(int(self.data[i][j]))]
                    if a[-3]==1 and flag==0:
                        start_x=j
                        start_y=i
                        flag=1
                    elif a[-3]!=1 and flag==1:
                        finish_x=j
                        finish_y=i
                        print(f'    \draw ({start_x},{start_y}) -- ({finish_x},{finish_y});',file = latex_file);
                        flag=0
                    elif a[-3]!=1 and flag==0:
                        pass
                    elif a[-3]==1 and flag==1:
                        pass
                    if (a[-3]==1 and j==self.length-1 and flag==1):
                        finish_x=j
                        finish_y=j
                        print(f'    \draw ({start_x},{start_y}) -- ({finish_x},{finish_y});',file = latex_file);
            
                    
                        
            i=0
            j=0            
            reverse_data=[]
            duplicate_items=[]
            s=self.length
            print('% South-West to North-East lines',file = latex_file)
            for j in range(self.height-1,0,-1):
                i=self.length-1
                while i>=0:
                    if (j,i) not in duplicate_items:
                        if (self.data[j][i]==2 or self.data[j][i]==3 or self.data[j][i]==6 or self.data[j][i]==7 or \
                            self.data[j][i]==10 or self.data[j][i]==11 or self.data[j][i]==14 or self.data[j][i]==15):
                            m=i
                            n=j
                            duplicate_items.append((n,m))
                            while (self.data[n-1][m+1]==2 or self.data[n-1][m+1]==3 or self.data[n-1][m+1]==6 or \
                                   self.data[n-1][m+1]==7 or self.data[n-1][m+1]==10 or self.data[n-1][m+1]==11 or\
                                    self.data[n-1][m+1]==14 or self.data[n-1][m+1]==15) and n-1>0 and m+1<s :
                                n=n-1
                                m=m+1
                                duplicate_items.append((n,m))
                            reverse_data.append([(i,j),(m+1,n-1)])
                    i-=1
            reverse_data.reverse()
            for i in reverse_data:
                print(f'    \draw ({i[0][0]},{i[0][1]}) -- ({i[1][0]},{i[1][1]});',file = latex_file);
                #print('    \draw('+str(i[0][0])+','+str(i[0][1])+') -- ('+str(i[1][0])+','+str(i[1][1])+');',file=latex_file)
                       #print('\draw(',start_x,',',start_y,') -- (',finish_x,',',finish_y,');',file = latex_file)

            
                            
                            

                    
                        
                    
                        
            
            
            
            
            
            
            
            print('\\end{tikzpicture}\n'
          '\\end{center}\n'
          '\\vspace*{\\fill}\n'
          '\n'
          '\\end{document}', file = latex_file)
         


        





     
            






    

    
    



