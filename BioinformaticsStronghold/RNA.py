print "Given: A DNA string t having length at most 1000 nt. Return: The transcribed RNA string of t.\n"

print "DNA: "
dna = raw_input()

rna = dna.replace('T', 'U')

print rna
