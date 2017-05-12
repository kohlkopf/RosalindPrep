print "Given: A string s of length at most 10000 letters. Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.\n"

from collections import Counter
import pickle   #for dictionary output

f = open('input.txt', 'r')
f = f.read()    #string

result = dict(Counter(f.split()))

for key, value in result.items():
    print key, value

a = result

with open('output.pickle', 'wb') as handle:
    pickle.dump(a, handle, protocol = pickle.HIGHEST_PROTOCOL)

with open('output.pickle', 'rb') as handle:
    b = pickle.load(handle)

print "Pickle file write success: " , a == b

