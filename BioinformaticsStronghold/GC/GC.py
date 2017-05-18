print "Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each). Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.\n"

from Bio import SeqIO
from Bio.SeqUtils import GC

id_gc = {}
for f in SeqIO.parse('input.fasta', 'fasta'):
    id_gc[f.id] = GC(f.seq)

print(max(id_gc, key=id_gc.get))
print(id_gc[max(id_gc, key=id_gc.get)])
