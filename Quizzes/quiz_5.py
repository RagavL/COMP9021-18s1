# Randomly fills a grid of size 10 x 10 with 0s and 1s and computes:
# - the size of the largest homogenous region starting from the top left corner,
#   so the largest region consisting of connected cells all filled with 1s or
#   all filled with 0s, depending on the value stored in the top left corner;
# - the size of the largest area with a checkers pattern.
#
# Written by Ragavendran Lakshminarasimhan and Eric Martin for COMP9021

import sys
from random import seed, randint
from copy import deepcopy

dim = 10
grid = [[None] * dim for _ in range(dim)]
def display_grid(gird):
    for i in range(dim):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(dim)))

# Possibly define other functions
try:
    arg_for_seed, density = input('Enter two nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density = int(arg_for_seed), int(density)
    if arg_for_seed < 0 or density < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
# We fill the grid with randomly generated 0s and 1s,
# with for every cell, a probability of 1/(density + 1) to generate a 0.
for i in range(dim):
    for j in range(dim):
        grid[i][j] = int(randint(0, density) != 0)
print('Here is the grid that has been generated:')
display_grid(grid)
grid_2 = deepcopy(grid)


def replace_1_by_star_1(i,j):
    global grid
    if grid[i][j] == 1:
        grid[i][j] = '*'
        if i:
            replace_1_by_star_1(i - 1, j)
        if i < dim - 1:
            replace_1_by_star_1(i + 1, j)
        if j:
            replace_1_by_star_1(i, j - 1)
        if j < dim - 1:
            replace_1_by_star_1(i, j + 1)
def replace_1_by_star_0(i,j):
    global grid
    if grid[i][j] == 0:
        grid[i][j] = '*'
        if i:
            replace_1_by_star_0(i - 1, j)
        if i < dim - 1:
            replace_1_by_star_0(i + 1, j)
        if j:
            replace_1_by_star_0(i, j - 1)
        if j < dim - 1:
            replace_1_by_star_0(i, j + 1)
if grid[0][0] == 1:
    replace_1_by_star_1(0,0)
if grid[0][0] == 0:
    replace_1_by_star_0(0,0)

def homogenous_region_to_star(grid):
    for i in range(dim):
        '   ', ' '.join(str(grid[i][j]) for j in range(dim))

homogenous_region_to_star(grid)

def if_zero_or_one(element):
    if element:
        return 0
    else:
        return 1

def function_for_checkers(i,j,grid, checked, start):
    if grid[i][j] == start:
        grid[i][j] = '*'
        checked +=1
        if i:
            checked = function_for_checkers(i-1, j, grid, checked, if_zero_or_one(start))
        if i < dim -1:
            checked = function_for_checkers(i+1, j, grid, checked, if_zero_or_one(start))
        if j:
            checked = function_for_checkers(i, j-1, grid, checked, if_zero_or_one(start))
        if j < dim - 1:
            checked = function_for_checkers(i, j+1, grid, checked, if_zero_or_one(start))
    return checked

grid_3 = deepcopy(grid_2)

def check_checks(grid):
    max_checked = 0
    checked = 0
    for i in range(0, dim-1):
        for j in range(0, dim-1):
            current = function_for_checkers(i, j, grid, checked, grid[i][j])
            if current > max_checked:
                max_checked = current
            grid_2 = deepcopy(grid_3)
            checked = 0

    return max_checked


def finding_homo_region(grid):
    size_of_largest_homogenous_region_from_top_left_corner  = 0
    for i in range(dim):
        for j in range(dim):
            if grid[i][j] == '*':
                size_of_largest_homogenous_region_from_top_left_corner += 1
    print('The size_of the largest homogenous region from the top left corner is '
          f'{size_of_largest_homogenous_region_from_top_left_corner}.'
         )
finding_homo_region(grid)


max_size_of_region_with_checkers_structure = check_checks(grid_2)

print('The size of the largest area with a checkers structure is '
      f'{max_size_of_region_with_checkers_structure}.'
     )

