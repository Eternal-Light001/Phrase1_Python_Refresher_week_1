# STEP (Procedure)
# Section 1 — Big O intuition (no timing needed)
# 1. Just demonstrate the difference with a comment:
# 2. No timing required. Just show both work, and comment why the set version is faster on big data.

# Section 2 — Set basics + operations
# 1. Print a, b — show the sets
# 2. Print a | b (union), a & b (intersection), a - b (difference)
# 3. Also: build a set from a list with duplicates and show dedupe:

# Section 3 — List comprehensions
# 1. Given nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
# 2. [n * 2 for n in nums] — double each
# 3. [n for n in nums if n % 2 == 0] — only evens
# 4. [n * n for n in nums if n > 5] — squares, but only > 5
# 5. [len(word) for word in ["hello", "world", "python"]] — length of each word

# Section 4 — Set comprehensions
# 1. Given nums = [1, 2, 2, 3, 3, 4, 5, 5]:
# 2. {n for n in nums} — dedupe as a set
# 3. {n % 3 for n in range(10)} — remainder mod 3, deduped

# Section 5 — Dict comprehensions (the important one)
# 1. {name: score + 5 for name, score in scores.items()} — bump all by 5
# 2. {name: score for name, score in scores.items() if score >= 80} — only passing
# 3. {name.upper(): score for name, score in scores.items()} — uppercase names
# 4. {score: name for name, score in scores.items()} — invert dict (score as key, name as value)
# 5. Add a comment on the invert one — why is it risky? (Hint: what if two students had the same score?)

# Section 6 — Combined (bridge to the Student Grade Tracker)
# 1. [s["name"] for s in students] — all names as a list
# 2. [s["name"] for s in students if s["score"] >= 80] — names of passing students
# 3. {s["name"]: s["score"] for s in students} — convert list-of-dicts to dict
# 4. sum(s["score"] for s in students) / len(students) — average (note: no brackets = generator expression, works the same as comprehension inside sum())
# 5. That last pattern is the bridge to your Week 1 capstone. You'll use it in the Student Grade Tracker.



# TEST TABLE (Expectation)
# {1,2,3,4} & {3,4,5,6}                                                     --> {3, 4}
# [n*2 for n in [1,2,3]]                                                    --> [2, 4, 6]
# [n for n in [1,2,3,4,5] if n % 2 == 0]                                    --> [2, 4]
# {name: score for name, score in {"Ada":85,"Bob":72}.items() if score>=80} --> {"Ada": 85}
# sum(s["score"] for s in [{"score":85},{"score":72}]) / 2                  --> 78.5

# Section 1 — Big O intuition (no timing needed)
nums = list(range(100000))          # big list
nums_set = set(nums)                # same data as a set

# Then one line each:
print(99999 in nums)                # --> True (O(n) — checks each)   # list recheck from 0 - 99999 to verify if 99999 is in the range, because it can't verify it with going the ranges
print(99999 in nums_set)            # --> True (O(1) — instant)       # set don't need recheck, It needs to just match 99999 and verify if it the same with the one in i memory.
print()

# Section 2 — Set basics + operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a, b)          # {1, 2, 3, 4} {3, 4, 5, 6}
print(a | b)         # {1, 2, 3, 4, 5, 6}
print(a & b)         # {3, 4}
print(a - b)         # {1, 2}

print(set([1, 2, 2, 3, 3, 3]))     # --> {1, 2, 3}   # The list is created with dedupe
print()

# Section 3 — List comprehensions
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print([n * 2 for n in nums])

print([i for i in nums if i % 2 == 0])

print([x * x for x in nums if x > 5])

print([len(word) for word in ["hello","world", "python"]])
print()

# Section 4 — Set comprehensions
nums = [1, 2, 2, 3, 3, 4, 5, 5]

print({n for n in nums})         # --> {1, 2, 3, 4, 5}

print({n % 3 for n in range(10)})     # --> {0, 1, 2}
print()

# Section 5 — Dict comprehensions (the important one)
scores = {"Ada": 85, "Bob": 72, "Cleo": 91, "Dee": 65}

print({name: score + 5 for name, score in scores.items()})                   # +5      

print({name: score for name, score in scores.items() if score >= 80})        # Pass

print({name.upper(): score for name, score in scores.items()})               # Uppercase

print({score: name for name, score in scores.items()})                       # Invert   # It is risk because two students, can share the same score. But we can use the value to search for the key
print()

# Section 6 — Combined (bridge to the Student Grade Tracker)
students = [
    {"name": "Ada", "score": 85},
    {"name": "Bob", "score": 72},
    {"name": "Cleo", "score": 91},
    {"name": "Dee", "score": 65},
]

print([s["name"] for s in students])

print([s["name"] for s in students if s["score"] >= 80])

print({s["name"]: s["score"] for s in students})

print(sum(s["score"] for s in students) / len(students))


