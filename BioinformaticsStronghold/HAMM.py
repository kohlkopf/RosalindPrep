print "Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).Return: The Hamming distance dH(s,t)dH(s,t)."

s1 = raw_input()
s2 = raw_input()

print sum ( s1[i] != s2[i] for i in range(len(s1)) )

