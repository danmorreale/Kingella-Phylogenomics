'''
This is a quick program using BioPython and SeqIO to take a folder of ffn files
read then in, build a dictionary, and return the sequence of a gene of interest.
This was written to work with the ffn files output by prokka, and will print
sequences and locus tags in fasta format to the terminal where they can be sorted
further
'''
import os
import sys
import Bio
from Bio import SeqIO

###List of key words that you want to search for in the genomes
#gene_of_interest = ["RTX", "rtx", "lkt", "apxIC", "tolC"]
###path to ffn file directory
file = os.listdir("/Users/danielmorreale/Desktop/ffn")

##read in each ffn file in the directory one at a time
for item in file:
    with open(item, "rU") as handle:
        ###parse into a dictionary that has all data saved
        dict = SeqIO.index(item ,"fasta")
        for record in SeqIO.parse(handle, "fasta"):
            #for each keyword listed above, see if that is in any descriptions lines from the fasta
            for name in gene_of_interest:
                if name in record.description:
                    ##collect fasta descriptions, append with the strain name
                    gene = record.description
                    gene = gene + "_" + item
                    ##collect fasta seq and print all to terminal
                    seq = record.seq
                    print (">", gene, "\n", seq)
