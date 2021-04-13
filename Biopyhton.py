## pip install --upgrade pip  
# pip install cython
# pip install pysam (ubuntu)
# pip install bio

from Bio import Entrez
import time
import sys
from Bio import SeqIO
from statistics import median


Entrez.email ="francisco.ascue@unmsm.edu.pe"
handle = Entrez.efetch(db="nucleotide",id="NC_045512.2",rettype="fasta", retmode="text")
print(handle.read())

file = open('rosalind_ini.txt', 'r')
string = file.read()
freq = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for i in string:
    freq[i] = freq[i] + 1

print(freq['A'], freq['C'], freq['G'], freq['T'])

fatqfile = SeqIO.parse("rosalind_phre.txt", "fastq")
for i in fatqfile:
    print(median(i.letter_annotations["phred_quality"]))
