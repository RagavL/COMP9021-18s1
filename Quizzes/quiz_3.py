# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and finds out, for a given direction being
# one of N, E, S or W (for North, East, South or West) and for a given size greater than 1,
# the number of triangles pointing in that direction, and of that size.
#
# Triangles pointing North:
# - of size 2:
#   1
# 1 1 1
# - of size 3:
#     1
#   1 1 1
# 1 1 1 1 1
#
# Triangles pointing East:
# - of size 2:
# 1
# 1 1
# 1
# - of size 3:
# 1
# 1 1
# 1 1 1 
# 1 1
# 1
#
# Triangles pointing South:
# - of size 2:
# 1 1 1
#   1
# - of size 3:
# 1 1 1 1 1
#   1 1 1
#     1
#
# Triangles pointing West:
# - of size 2:
#   1
# 1 1
#   1
# - of size 3:
#     1
#   1 1
# 1 1 1 
#   1 1
#     1
#
# The output lists, for every direction and for every size, the number of triangles
# pointing in that direction and of that size, provided there is at least one such triangle.
# For a given direction, the possble sizes are listed from largest to smallest.
#
# We do not count triangles that are truncations of larger triangles, that is, obtained
# from the latter by ignoring at least one layer, starting from the base.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict
import itertools
from math import sqrt





def display_grid(grid):
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))


		

def turn_direction_of_triangles(grid):
    computed_grid = [[0] * len(grid) for _ in range(len(grid))]
    for row in range(len(grid)):
        for column in range(len(grid)):
            computed_grid[len(grid)-1-column][row] = grid[row][column]
    return computed_grid




def count_no_of_triangles(grid):
    size_and_num_of_triangles = defaultdict(int)
    for row in range(0,len(grid)):
        for column in range(1,len(grid)-1):
            if grid[row][column] == 1: 
                maximum_size = (len(grid)+1)//2

                while maximum_size >= 2:
                    if row+maximum_size <= len(grid) and column-maximum_size+1 >= 0 and column+maximum_size <= len(grid): 
                        num_of_count = num_in_a_line = 0
                        for row_element in range (1,maximum_size):
                            for column_element in range(column-row_element,column+row_element+1):
                                num_of_count += 1
                                num_in_a_line += grid[row+row_element][column_element]
                        if num_of_count == num_in_a_line:
                            size_and_num_of_triangles[maximum_size] += 1
                            break
                    maximum_size -= 1
    return size_and_num_of_triangles




def triangles_in_grid():
    grid_triangles = defaultdict(str)
    new_grid_N = grid.copy()
    for i in range(len(grid)):
        for j in range(len(grid)):
            new_grid_N[i][j] = int(grid[i][j] != 0)
        size_and_num_N = count_no_of_triangles(new_grid_N)
        if size_and_num_N:
            grid_triangles['N'] = []
            size_and_num_N = sorted(size_and_num_N.items(), key = lambda item: item[0], reverse = True)
            for key,value in size_and_num_N:
                grid_triangles['N'].append((key,value))
    
   
    new_grid_E = turn_direction_of_triangles(new_grid_N)
    size_and_num_E = count_no_of_triangles(new_grid_E)
    if size_and_num_E:
        grid_triangles['E'] = []
        size_and_num_E = sorted(size_and_num_E.items(), key = lambda item: item[0], reverse = True)
        for key,value in size_and_num_E:
            grid_triangles['E'].append((key,value))

    new_grid_S = turn_direction_of_triangles(new_grid_E)
    size_and_num_S = count_no_of_triangles(new_grid_S)
    if size_and_num_S:
        grid_triangles['S'] = []
        size_and_num_S = sorted(size_and_num_S.items(), key = lambda item: item[0], reverse = True)
        for key,value in size_and_num_S:
            grid_triangles['S'].append((key,value))

    new_grid_W = turn_direction_of_triangles(new_grid_S)
    size_and_num_W = count_no_of_triangles(new_grid_W)
    if size_and_num_W:
        grid_triangles['W'] = []
        size_and_num_W = sorted(size_and_num_W.items(), key = lambda item: item[0], reverse = True)
        for key,value in size_and_num_W:
            grid_triangles['W'].append((key,value))



    return grid_triangles
    
try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid(grid)
triangles = triangles_in_grid()
for direction in sorted(triangles, key = lambda x: 'NESW'.index(x)):
    print(f'\nFor triangles pointing {direction}, we have:')
    for size, nb_of_triangles in triangles[direction]:
        triangle_or_triangles = 'triangle' if nb_of_triangles == 1 else 'triangles'
        print(f'     {nb_of_triangles} {triangle_or_triangles} of size {size}')

