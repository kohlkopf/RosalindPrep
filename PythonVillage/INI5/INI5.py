print "Given: A file containing at most 1000 lines. Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.\n"

f = open('input.txt', 'r')

list = f.readlines()
list = list[1::2]

list = ''.join(list)

print(list)

f = open('output.txt', 'w')
f.write(list)
f.close()

