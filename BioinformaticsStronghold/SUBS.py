print "Given: Two DNA strings s and t (each of length at most 1 kbp). Return: All locations of tt as a substring of s."

import re

print "Candidate string: "
cand = raw_input()
print "String to be sought: "
index = "(?=" + raw_input() + ")"   #lookahead reg expression 

print [m.start()+1 for m in re.finditer(index, cand)]   #+1 for 1 based numbering
