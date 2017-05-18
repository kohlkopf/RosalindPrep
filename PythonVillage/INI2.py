print "Given: Two positive integers a and b, each less than 1000. Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b."

def answer(side_a, side_b):
	return side_a ** 2.0 + side_b ** 2.0        #** is exponent modifier

def hypotenuse(side_a, side_b):
	return answer(side_a, side_b) 

side_a = float(raw_input())

print "The length of side A is", side_a

side_b = float(raw_input())

print "The length of side B is", side_b

print "The square of the hypotenuse is", hypotenuse(side_a, side_b)
