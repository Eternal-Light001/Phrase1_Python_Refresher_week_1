# STEP 1 (Summary Code)

# TEST TABLE (Behavior)
# Section 1 — Types (5 variables, 5 prints)
# int   --> 5              --> (class 'int')
# float --> 6.0            --> (class 'float')
# str   --> "Five", 'Five' --> (class 'str')
# bool  --> True or False  --> (class 'bool')
# None                     --> (class 'none')

# Section 2 — Type Casting (5 conversion demos)
# a = int("42")     --> 42                                          --> (class 'int')
# b = str(42)       --> 42 has been coated with quote in the memory --> (class 'str')
# c = float("3.14") --> 3.14                                        --> (class 'float')
# d = int(3.9)      --> 3                                           --> (class 'int')
# bool()            --> [], "" is False and the rests are True

# Section 3 — String Formatting
# f"{name}; {age}"
# Coach, this Test Table is fucking delaying my coding.
# 19.99

# Section 4 — Operators (one printed line per operator)
# Arithmetic — use 17 and 5 throughout:
# 9, 5, 14, 3,3333, 3, 1, 49

# Comparison — use 17 and 5:
# False, True, False, True, False, False

# Logical — with True/False values:
# True, True, True

# Bitwise — use 5 and 3:
# Coach, this Test Table is fucking delaying my coding.



# Section 1 — Types (5 variables, 5 prints)
number = 5
output_1 = f"This number is called an integer:- {number}, and the type is {type(number)}"
print(output_1)

decimal = 6.0
output_2 = f"This number is called a float:- {decimal}, and the type is {type(decimal)}"
print(output_2)

word = "Five"
output_3 = f"This word is called a string:- {word} either a double quote or a single quote (''), and the type is {type(word)}"
print(output_3)

condition = True
output_4 = f"This condition is called a boolean:- {condition}, either True or False, and the tpye is {type(condition)}"
print(output_4)

nothing = None
output_5 = f"This is called NoneType:- {nothing}, and the type is {type(nothing)}"
print(output_5)


# Section 2 — Type Casting (5 conversion demos)
a = int("42")
print(a, type(a))

b = str(42)
print(b, type(b))

c = float("3.14")
print(c, type(c))

d = int(3.9)
print(d, type(d))

print(bool(0), type(bool(0)))
print(bool(1), type(bool(1)))
print(bool(""), type(bool("")))
print(bool("hello"), type(bool("hello")))
print(bool([]), type(bool([])))
print(bool(None), type(bool(None)))


# Section 3 — String Formatting
name = "Emmanuel"
Age = 9

print(f"My name is {name}, and I am {Age} years old")

print("My name is {first}, and I am {second} years old".format(first=name, second=Age))

price = 19.9876
output_6 = f"{price:.2f}"
print(output_6)

print(f"[{name:>15}]")
print(f"[{name:<15}]")   


# Section 4 — Operators (one printed line per operator)
# Arithmetic — use 17 and 5 throughout:
print(17 + 5)  
print(17 - 5)    
print(17 * 5)    
print(17 / 5)    
print(17 // 5)   
print(17 % 5)    
print(17 ** 5)   

# Comparison — use 17 and 5:
print(17 == 5)
print(17 != 5)
print(17 < 5)
print(17 > 5)
print(17 <= 5)
print(17 >= 5)

# Logical — with True/False values:
a = True
b = False

print(a and a)
print(a or b)
print(not b)

# Bitwise — use 5 and 3:
c = 5
d = 1

print(c & d)
print(c | d)
print(c ^ d)
print(~ 5)
print(c << d)
print(c >> d)