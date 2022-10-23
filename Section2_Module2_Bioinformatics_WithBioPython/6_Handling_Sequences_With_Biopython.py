# -*- coding: utf-8 -*-


# All of this was done in JuypterLab when Jesse E. Agbe the instructor did it

# I am using Spyder and Python

import Bio

print(Bio.__version__)

from Bio.Seq import Seq

print(dir(Bio))

############################

# Working with sequences


from Bio.Seq import Seq

# Methods Of Seq 

print( dir(Seq) )


# Create a simple seqence

seq1 = Seq('ATGATCTCGTAA')


#############################################################


#Checking For The Type Of Sequence

#seq1.alphabet()


#from Bio.Alphabet import generic_dna,generic_rna,generic_protein

#Bio Alphabet has been removed


###############################################################

#Lets find the length

print("This is the length")
print(len(seq1) )


#Lets use another sequence

seq2 = Seq ('ARGATCTCGTGG')

# Lets join it to another sequence

print (seq1[0:6] + seq2)

dna_seq = seq1[0:6] + seq2

#######

# Lets find the number of nucleotides/bases within our seq


print ("This is the number of Gs")


print( dna_seq.count('G') )

print ("This is the number of As")


print( dna_seq.count('A') )

# Let's count the number of codons

print (f"This is the number of codons with ATG {dna_seq.count('ATG')}")

#Let's find the position/location of a nucleotide

print( f"This is the position of G - {dna_seq.find('G')}")

print ( f"Manually check 0, 1. 2 if it is in the second position {dna_seq}")

#Let's find the position/location of a nucleotide from the right

print( f"This is the position of G from the right - {dna_seq.rfind('G')}")

# To find a location you can do index

print( f"This is the position of G using index {dna_seq.index('G')}")


print( f"This is the position of G using index from the right {dna_seq.rindex('G')}")


############################

#Plot of Frequency Of Nucleotides/Base

import matplotlib.pyplot as plt

from collections import Counter

dna_freq = Counter(dna_seq)


plt.bar(dna_freq.keys(), dna_freq.values())

