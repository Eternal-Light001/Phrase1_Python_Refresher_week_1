# Step 1:-
# Read number from 1 to 101
# if divisible by BOTH 3 and 5 --> FizzBuzz
# elif divisible by 5 --> Buzz
# elif divisible by 3 --> Fizz
# else --> number

# Step 2:-
for i in range(1, 101):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%5 == 0:
        print("Buzz")
    elif i%3 == 0:
        print("Fizz")
    else:
        print(i)

# TEST TABLE
# Code ran as expected, no errors, it shows:-
# The result:- divisible by 3 --> Fizz
# The result:- divisible by 5 --> Buzz
# The result:- divisilbe by neither 3 nor 5 --> number
# The result:- divisible by BOTH 3 and 5 --> FizzBuzz