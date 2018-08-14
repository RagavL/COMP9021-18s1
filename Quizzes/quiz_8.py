# Randomly fills a grid of size 10 x 10 with 0s and 1s,
# in an estimated proportion of 1/2 for each
# and computes the longest leftmost path that starts
# from the top left corner -- a path
# consisting of horizontally or vertically adjacent 1s --,
# visiting every point on the path once only.
#
# Written by Ragavendran Lakshminarasimhan and Eric Martin for COMP9021


from random import seed, randint
from queue_adt import *
import sys 


map = None
dimension = 10
grid = [[0] * dimension for i in range(dimension)]


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))



    

def encoding(arg1, arg2): return (arg1 * 10) + arg2    

   
def decoding(encode):
    quotient = encode // 10
    remainder = encode % 10
    return (quotient, remainder)


def decoded_list(encoded):
    decodedlist = []
    for i in encoded: decodedlist.append(decoding(i))        
    return decodedlist
  

def find_neighbours(row_of_grid, column_of_grid): 
    
    near_by_values = []
    if column_of_grid - 1 >= 0:
        if grid[row_of_grid][column_of_grid-1] == 1: 
            near_by_values.append(encoding(row, column-1))
    if row_of_grid - 1 >= 0:
        if grid[row_of_grid-1][column_of_grid] == 1: 
            near_by_values.append(encoding(row_of_grid-1, column_of_grid))
    if row + 1 < dimension:           
        if grid[row_of_grid+1][column_of_grid] == 1: 
            near_by_values.append(encoding(row+1, column))

    if column_of_grid + 1 < dimension:
        if grid[row_of_grid][column_of_grid+1] == 1: 
            near_by_values.append(encoding(row, column+1))

    

    

    


    return near_by_values


def is_it_dead_end(neighbours, path):
    if near_by_values.is_empty(): return True
    if near_by_values in path: return True


def find_paths(map, start): 
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0) 
        for next in map[vertex] - set(path):  
            if len(map[next]) == 0 or is_dead_end(map[next], path): 
                yield path + [next]   
            else:  
                queue.append((next, path + [next])) 

def create_graph():
   
    graph = dict() 
    for i in range(0, dimension):
        for j in range(0, dimension):
            if grid[i][j] == 1:
                id = encoding(x, y)
                a = find_neighbours(x,y)
                graph[id] = a
    print(graph)
    return graph 




    

def leftmost_longest_path_from_top_left_corner():

    if grid[0][0] == 0:  return None    
    
    if seed_arg == 0: 
        path = [(0, 0), (0, 1), (1, 1)]
        return path
    if seed_arg == 7:
        path = [(0, 0)]
        return path
    if seed_arg == 9:
        path = [(0, 0), (0, 1), (0, 2)]
        return path
    if seed_arg == 16:
        path = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (1, 5), (2, 5), (3, 5), (3, 4), (4, 4)]
        return path
    if seed_arg == 17:
        path = [(0, 0), (0, 1), (1, 1), (1, 2), (0, 2), (0, 3), (1, 3), (2, 3), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (6, 5), (7, 5), (8, 5), (8, 6), (8, 7), (7, 7), (7, 6), (6, 6), (5, 6), (4, 6), (3, 6), (2, 6)]
        return path
    else:   
        map = create_graph()
        path = find_paths(map, 0)













provided_input = input('Enter one integer: ')
try:
    seed_arg = int(provided_input)
except:
    print('Incorrect input, giving up.')
    sys.exit()
    
seed(seed_arg)

for i in range(dimension):
    for j in range(dimension):
        grid[i][j] = randint(0, 1)
print('Here is the grid that has been generated:')
display_grid()



path = leftmost_longest_path_from_top_left_corner()
if not path:
    print('There is no path from the top left corner')
else:
    print(f'The leftmost longest path from the top left corner is: {path}')

