#!/usr/bin/perl

use strict;
use warnings;
use Bio::TreeIO;
use Data::Dumper;
use Statistics::Descriptive;

######################################

##   Iker Irisarri, MNCN Jun 2018  ##

######################################

# modification of mean_root_to_tip.pl because the rooting did not work properly
# Instead of calculating the distance with all outgroups, divide by two and get the mean
# this calculates the depth of all tips, including outgroups

# In principle, both approaches should produce the same results, 
# but for some reason there are small differences (judged by results on Jurgen's data)
 
######################################

my $usage = "mean_root_to_tip.pl tree > stdout\n";
my $in_tree = $ARGV[0] or die $usage;

# read in trees
my $treeio = new Bio::TreeIO(-file   => "$in_tree",
						     -format => "newick");

my $out = new Bio::TreeIO(#-file => '>outtree.tree',
                          -format => 'newick');

my $stat = Statistics::Descriptive::Full->new();
                          

while( my $tree = $treeio->next_tree ) {

	for my $node ( $tree->get_nodes ) {

		if ( $node->is_Leaf ) {
			
			my $id = $node->id;				
			my $depth = $node->depth;

			print "DEPTH $id: $depth\n";
			$stat->add_data($depth);
		}	
	}	
}


my $mean = $stat->mean();
my $stddev = $stat->standard_deviation();

print "information of branch lengths:\n";
print "mean: $mean\nSD: $stddev\n";

