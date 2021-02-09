"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730337008"

# andint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("your fortune cookie says...")
fun: int=randint(1,4)
if fun == 1:
   print("Your future is bright.")
else: 
   if fun == 2:
    print("You have good things in your future.")
   else:
      if fun == 3:
       print("Maybe you will buy a dog in the near future")
      else:
         print("You will have a great dinner")
print("Now, go spread positive vibes!")