# STEP 1 (What is about?)
# Create Mutability vs Immutability (with id() proof)
# Create Indexing & Slicing
# Create String Methods

# TEST TABLE (Expectation/Behavior)
# id changes after a = a + 1       -->True (id CHANGED)
# id changes after b.append(4)     --> False (id SAME)
# x after y=x; y.append(99)        --> [1,2,3,99] (shared object)
# x after y=x.copy(); y.append(99) --> [1,2,3] (independent copy)
# "PythonProgramming"[::-1]        --> "gnimmargorPnohtyP"
# "  hello  ".strip()              --> "hello"
# "a,b,c".split(",")               --> ["a","b","c"]


# Section 1 — Mutability vs Immutability (with id() proof)
# Immutability demo (int):
a = 5
print(id(a))

a = a + 1
print(id(a))   # id() changed not the same, int is immutable.

# Mutability demo (list):
b = [1, 2, 3]
print(id(b))

b.append(4)
print(id(b))   # id() not changed, it the say. List is mutable.

# The reference-sharing demo:
x = [1, 2, 3]
y = x
y.append(99)
print(x)   # x print the append of y because, x and y are mutated and the same not an independent list.

x = [1, 2, 3]
y = x.copy()
print(x)   # x print the exact value and because y is an independent list created by .copy()

# Immutability of strings:
try:
    s = "hello"
    s[0] = "H"
except TypeError:
    print("❌ Strings are immutable — can't reassign.")
s = "H" + s[1:]
print(s)

# Section 2 — Indexing & Slicing
s = "PythonProgramming"
print(s[0])   # it prints only the first letter P
print(s[1])   # it prints only the second letter y
print(s[-1])   # it prints only the first letter, I meant the end of the word, basically the last word.
print(s[-2])   # it prints only the second letter, I meant the second to the last of the word.
print(s[0:6])   # it's 6 characters (P-y-t-h-o-n)
print(s[:6])   # it's 6 characters (P-y-t-h-o-n)
print(s[6:])   # it prints only the character at the 6th characters still the end.
print(s[::2])     # every 2nd character, starting at index 0
print(s[::-1])   #  is the reversed string (gnimmargorPnohtyP)
print(len(s))   # it print the length of the word

# Section 3 — String Methods
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())

print(s.strip())
print(s.replace("P", "J"))
print(s.split())
print("-".join(["Python", "Programming"]))   # --> Python-Programming

print(s.find("5"))
print(s.count("m"))
print(s.startswith("P"))
print(s.endswith(".txt"))

# Suggested test strings (or make your own):
print(" hello world ".strip())

print("apple,banana,cherry".split(","))
print(",".join(["apple", "banana", "cherry"]))

print("banana".count("a"))
print("banana".find("n"))

print("file.txt".endswith(".txt"))
