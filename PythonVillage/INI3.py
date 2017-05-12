print "Given: Two positive integers a and bb (a<b<10000a<b<10000). Return: The sum of all odd integers from a through b, inclusively.\n"

print "String: "
gabble = str(raw_input())

print "Indices: "
indices = map(int, raw_input().split())

splitOne = gabble[indices[0]:indices[1]+1]
splitTwo = gabble[indices[2]:indices[3]+1]

print splitOne + " " + splitTwo
