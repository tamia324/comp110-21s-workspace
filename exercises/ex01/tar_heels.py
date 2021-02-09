"""An exercise in remainders and boolean logic."""

__author__ = 730337008

# Begin your solution here...
integer: int = int(input("Pick an integer"))

if (integer % 7==0 and integer % 2==0):
    print("TAR HEELS") 
elif (integer % 2==0):
    print("TAR") 
elif (integer % 7==0):
    print("HEELS")

else: 
    print("CAROLINA")



