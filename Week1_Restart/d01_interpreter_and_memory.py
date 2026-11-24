# STEP 1
# Variables creation to verify id

# TEST TABLE (Expectation)
# a = 5, b = 5                   --> same id
# a = 65, b = 65                 --> id varies
# a = [1,5,7], b = [1,5,7]       --> different id
# a = [2,3,4], b = [3/3/4]       --> different id/ id varies
# print(f"  c is d  → {c is d}") --> expect: False
# print(f"  c == d  → {c == d}") --> expect: True
# print(f"  x is y? {x is y}")   --> expect: True
# print(f"  p is q? {p is q}")   --> expect: False
# print(f"  p = {p}")            --> p should stay [1, 2, 3]


a = 5
print(id(a))
b = 5
print(id(b))

a = 65
print(id(a))
b = 65
print(id(b))

a = [1,5,7]
print(id(a))
b = [1,5,7]
print(id(b))

a = [2,3,4]
print(id(a))
a = [3,2,4]
print(id(a))

a = 5
print(id(a))
a = [a]
print(id(a))



print("\nTest — is vs ==: ")
c = [1, 2, 3]
d = [1, 2, 3]
print(f"  c is d  → {c is d}")   
print(f"  c == d  → {c == d}")   


print("\nTest — mutability: ")
x = [1, 2, 3]
y = x                  
print(f"  before: x = {x}, y = {y}")
print(f"  x is y? {x is y}")  
y.append(99)
print(f"  after y.append(99):")
print(f"  x = {x}")          
print(f"  y = {y}")
print(f"  did x change too? {x == [1, 2, 3, 99]}")   # Yes because x is equivalent to y

print("\nTest — how to actually copy:")
p = [1, 2, 3]
q = p.copy()
print(f"  before: p = {p}, q = {q}")
print(f"  p is q? {p is q}")
q.append(99)
print(f"  after q.append(99):")
print(f"  p = {p}")         # It can't change because q is just a shadow of the list not the list different id
print(f"  q = {q}")