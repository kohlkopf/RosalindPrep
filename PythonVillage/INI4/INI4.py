print "Sum of odd integers betwixt a and b.\n"


print "Integers: "
a = int(raw_input())
b = int(raw_input())

odds = filter(lambda x: x % 2, range(a, b))

answer = sum(odds)

print answer

