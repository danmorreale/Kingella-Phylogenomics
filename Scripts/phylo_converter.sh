from Bio import Phylo
from Bio.Phylo import PhyloXMLIO
Phylo.convert("bkseqncbi_tree.nhx", "newick", "bkseqncbi_tree.xml", "phyloxml")
print "DONE"
