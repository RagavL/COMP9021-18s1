# Randomly generates a binary search tree whose number of nodes
# is determined by user input, with labels ranging between 0 and 999,999,
# displays it, and outputs the maximum difference between consecutive leaves.
#
# Written by *** and Eric Martin for COMP9021

import sys
from random import seed, randrange
from binary_tree_adt import *

values_of_the_leaves = []

def traverse_the_given_tree(tree):
    
    if tree is not None:
        if tree.left_node is not None and tree.right_node is not None:
            if tree.left_node.value is None and tree.right_node.value is None:
                values_of_the_leaves.append(tree.value)
    else:
        return
    traverse_the_given_tree(tree.left_node)
    traverse_the_given_tree(tree.right_node)




def max_diff_in_consecutive_leaves(tree):
    traverse_the_given_tree(tree)
    
    maximum_difference = 0
    for i in range(0, len(values_of_the_leaves)-1):
        temp = abs(values_of_the_leaves[i] - values_of_the_leaves[i+1])
        if temp > maximum_difference:
            maximum_difference = temp

    return maximum_difference


provided_input = input('Enter two integers, the second one being positive: ')
try:
    arg_for_seed, nb_of_nodes = provided_input.split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, nb_of_nodes = int(arg_for_seed), int(nb_of_nodes)
    if nb_of_nodes < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
tree = BinaryTree()
for _ in range(nb_of_nodes):
    datum = randrange(1000000)
    tree.insert_in_bst(datum)
print('Here is the tree that has been generated:')
tree.print_binary_tree()
print('The maximum difference between consecutive leaves is: ', end = '')
print(max_diff_in_consecutive_leaves(tree))
           
