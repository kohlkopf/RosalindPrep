print "Given: A DNA string s of length at most 1000 nt. Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.\n"

import collections

print "String: "
seq = str(raw_input())

d = collections.defaultdict(int)
for c in seq:
    d[c] += 1


for key, value in d.items():
    print key, value,        #, importantly replaces \n with space


