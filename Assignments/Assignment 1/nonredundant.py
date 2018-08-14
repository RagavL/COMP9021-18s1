# Written by Ragavendran Lakshminarasimhan(z5179974) for COMP9021


import sys
import re

filename = input('Which data file do you want to use? ')
try:
    redundancy = open(filename, 'r').readlines()
except FileNotFoundError:
        print("File doesn't exist. Quitting")
        sys.exit()
        
coordinates = dict()
redundant_path = []

'''
Function to remove duplicate paths from the input
'''
def remove_duplicates_path():
    length = len(redundancy)
    temporary = []
    for line in redundancy:
        line = re.sub("\D", "", line)
        temporary.append((f'R({line[0]},{line[1]})'))
    for i in range(length):
        one = temporary[i]
       
        for j in range(i+1,length):
            
            two = temporary[j]
            if one == two:
                redundancy.remove(redundancy[j])
                length -= 1


'''
Find out if the current source node has already been seen and updated into the dictionary
'''        
def key_path_exists(coordinates, source):
    if source in coordinates:
        return True
    else:
        coordinates[source] = []
        return False


'''
Find out if a path already exists from the given source node to destination node
'''                
def path_exists(coordinates, source, destination):
    
    if not key_path_exists(coordinates, source):
        return False
    else:
        if destination in coordinates[source]:
            
            return True
        else: return False



'''
Add the current destination node to the source node
'''
def add_to_paths(coordinates, source, destination):
    if not key_path_exists(coordinates, source):
            coordinates[source].append(destination)
    for key, value in coordinates.items():
        if key == source:
            coordinates[key].append(destination)


'''
Function to handle certain cases of redundant nodes where a redundant node 
is found after it has already been marked as non-redundant
'''
def remove_duplicate_paths(coordinates, source, destination):
    nodes = list(coordinates.keys())
    index_of_source = []
    for index, node in enumerate(nodes):
        if destination in coordinates[node]:
            if source in coordinates[node]:                 
                index_of_source.append(node)
    return index_of_source   


'''
Add the current destionation node to all paths that lead to the current source node
'''     
def update_all_paths(coordinates):
    sources = list(coordinates.keys())
    for key, value in coordinates.items():         
        for source in sources:
            if source in value:
                temp = coordinates[source]
                for items in temp:
                    if items in value:
                        red = (f'R({key},{items})')
                        redundant_path.append(red)
                    if items not in value:
                        value.append(items)

             


'''
Populate the dictionary to find out paths from a node to another node
'''
def populate_paths(coordinates, redundancy, redundant_path):
    
    remove_duplicates_path()
    
    for line in redundancy:

        og_line = line
        line = re.sub("\D", "", line)
  
        if path_exists(coordinates, line[0], line[1]):
            check = (f'R({line[0]},{line[1]})') 
            redundant_path.append((og_line.lstrip()).rstrip())
        
        else:      
            add_to_paths(coordinates, line[0], line[1])
            source = remove_duplicate_paths(coordinates, line[0], line[1])
          
            if source:
               
                for key in source:
    
                    redundant_thing = key+line[1]
                    for path in redundancy:
                        
                        original_line = path
                        path = re.sub("\D", "", path)
                        if redundant_thing == path:
                            
                            redundant_path.append((original_line.lstrip()).rstrip())
                            
            update_all_paths(coordinates)
       

populate_paths(coordinates, redundancy, redundant_path)  

print("The nonredundant facts are:")


for element in redundancy:
    element = (element.lstrip()).rstrip()
    if element not in redundant_path:
      print(element, end = "\n")
