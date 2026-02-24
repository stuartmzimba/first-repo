"""
for_loops_basics.py

This file explains the basics of for loops in Python.
A for loop is used to repeat a block of code for each item in a sequence.
"""

# 1. Looping through a list

fruits = ["apple", "banana", "orange"]

print("Example 1: Looping through a list")
for fruit in fruits:
    print(fruit)

# The loop runs once for each item in the list.
# On eachfd iteration, 'fruit' holds the current item.


# ----------------------------------------
# 2. Using range()
# ----------------------------------------

print("\nExample 2: Using range()")

# range(5) generates numbers from 0 up to (but not including) 5
for number in range(5):
    print(number)

# Output: 0, 1, 2, 3, 4


# ----------------------------------------
# 3. range() with start and stop
# ----------------------------------------

print("\nExample 3: range(start, stop)")

for number in range(1, 6):
    print(number)

# This prints numbers from 1 to 5.


# ----------------------------------------
# 4. range() with step
# ----------------------------------------

print("\nExample 4: range(start, stop, step)")

for number in range(0, 10, 2):
    print(number)

# This prints even numbers from 0 to 8.


# ----------------------------------------
# 5. Looping through a string
# ----------------------------------------

print("\nExample 5: Looping through a string")

word = "Python"

for letter in word:
    print(letter)

# The loop runs once for each character in the string.


# ----------------------------------------
# 6. Using break and continue
# ----------------------------------------

print("\nExample 6: break and continue")

for number in range(1, 6):
    if number == 3:
        continue  # Skip number 3
    if number == 5:
        break     # Stop the loop completely
    print(number)

# continue: skips the current iteration
# break: exits the loop entirely


print("\nEnd of for loop examples.")