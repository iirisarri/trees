#!/usr/bin/env python3

import sys
import ete3
from ete3 import Tree

'''

script to collapse branches with low support (level provided as second argument)

(c) Iker Irisarri
University of Goettingen
Sep 2021

'''

# read input file from command line
with open(sys.argv[1], 'r') as f:
    infile = f.read()

# read support threshold (can be float)
threshold = float(sys.argv[2])

# read tree
tree = Tree( infile, format = 0 ) # internal and leaf branches + leaf names

#print(tree)

# traverse tree to get information
for node in tree.traverse("postorder"):

	node_length = len(node) # returns the number of leaves under node

	# process only internal nodes
	if node_length > 1:
	
		#print("support:", node.support)
		# if the support value is below the provided threshold, collapse
		if node.support < threshold:
	
			node.delete()

# print modified tree
print(tree.write())

