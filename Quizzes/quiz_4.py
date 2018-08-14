# Uses National Data on the relative frequency of given names in the population of U.S. births,
# stored in a directory "names", in files named "yobxxxx.txt with xxxx being the year of birth.
#
# Prompts the user for a first name, and finds out the first year
# when this name was most popular in terms of frequency of names being given,
# as a female name and as a male name.
# 
# Written by Ragavendran Lakshminarasimhan and Eric Martin for COMP9021


import os


first_name = input('Enter a first name: ')
directory = 'names'
min_male_frequency = 0
male_first_year = 0
min_female_frequency = 0
female_first_year = 0
temp_male=0
temp_female=0
male_count=0
female_count=0

for filename in os.listdir(directory):
  if  not (filename[7:11] == ".txt" and filename[0:3] =="yob" and filename[3:7].isnumeric()):
     continue
  elif filename[7:11] == ".txt" and filename[0:3] =="yob" and filename[3:7].isnumeric(): 
    with open(directory+'/'+ filename) as data_file:
      male_count=0
      female_count=0
      for line in data_file:
        name,sex,count = line.split(",")
        count=int(count)
        if sex == "M":
          male_count+=count
        elif sex =="F":
          female_count+=count
      with open(directory+'/'+ filename) as data_file:
        for line in data_file:
           name,sex,count = line.split(",")
           count=int(count)
           if name == first_name:
            if sex == "M" and ((count*100)/male_count > min_male_frequency):
              min_male_frequency = (count*100)/male_count
              male_first_year=int(filename[3:7])
            elif sex == "F" and ((count*100)/female_count > min_female_frequency):
              min_female_frequency = (count*100)/female_count
              female_first_year=int(filename[3:7])
         



if not female_first_year:
    print(f'In all years, {first_name} was never given as a female name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a female name first in the year {female_first_year}.\n'
          f'  It then accounted for {min_female_frequency:.2f}% of all female names.'
         )
if not male_first_year:
    print(f'In all years, {first_name} was never given as a male name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a male name first in the year {male_first_year}.\n'
          f'  It then accounted for {min_male_frequency:.2f}% of all male names.'
         )


