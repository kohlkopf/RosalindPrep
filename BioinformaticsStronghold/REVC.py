print "Given: A DNA string s of length at most 1000 bp. Return: The reverse complement s^c of s.\n"

print "DNA: "
dna = raw_input()

complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}       #dictionary A:T etc
bases = list(dna)
bases = reversed([complement.get(base,base) for base in bases])
bases = ''.join(bases)

print bases

