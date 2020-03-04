#!/usr/bin/env python3

import sys
import ete3
from ete3 import Tree

'''

script to get node ages from time-calibrated trees (i.e. sum of branch lengths from a node to one of the tips)


'''

# read input file from command line
with open(sys.argv[1], 'r') as f:
    infile = f.read()

# read tree
tree = Tree( infile, format = 5 ) # internal and leaf branches + leaf names

#print(tree)

# traverse tree to get information
for node in tree.traverse("postorder"):

	leaves = [] # create empty list of leaves for each node
	node_length = len(node) # returns the number of leaves under node

	# process only internal nodes
	if node_length > 1:
	
		# get all leaves for each node
		for leaf in node:
			if leaf.is_leaf():
				leaf.name
				leaves.append(leaf.name)
		#print(node_length, len(leaves))
		#print("node\n", leaves)
	
		# create strings of leaves to identify nodes
		nodename = '-'.join(sorted(leaves))
		#print(nodename)

		# calculate age as distance to the first leave in leaves
		age = node.get_distance(leaves[0])
		#print(age)

		# print out result
		print(nodename, '\t', age)
	
