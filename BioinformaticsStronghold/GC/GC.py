print "Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each). Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.\n"

from Bio import SeqIO
from Bio.SeqUtils import GC

for seq_record in SeqIO.parse("input.fasta", "fasta"):
    calc = {seq_record.id : GC(seq_record.seq)}

print max(calc, key=calc.get)
print calc[max(calc, key=calc.get)]
