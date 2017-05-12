print "Sum of odd integers betwixt a and b, recursively \n"

def integers(a, b):
    return list(range(a, b+1))
def find_odds(numbers):
  if not numbers:
    return []
  if numbers[0] % 2 == 1:
    return [numbers[0]] + find_odds(numbers[1:])
  return find_odds(numbers[1:])

print "Integers: "
a = int(raw_input())
b = int(raw_input())

numbers = integers(a,b)

odds = find_odds(numbers)

answer = sum(odds)

print answer


