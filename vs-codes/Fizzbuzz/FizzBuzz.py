# A py program that iterates the integers from 1 to 50.
# For multiples of 3, print "Fizz", for multiples of 5, print "Buzz."
# For numbers that are multiples of both 3 $ 5, print "FizzBuzz."

for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("FizzBuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("Fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("Buzz")
        continue
    print(fizzbuzz)
