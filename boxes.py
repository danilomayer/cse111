"""
A manufacturing company needs a program that will help its employees pack manufactured items into boxes for shipping. Write a Python program named boxes.py that asks the user for two integers:

1. The number of manufactured items
2. The number of items that the user will pack per box

Your program must compute and print the number of boxes necessary to hold the items. This must be a whole number. Note that the last box may be packed with fewer items than the other boxes.
"""
# Get the math library
import math

# Prompt user for the number of items
items = int(input("Enter the number of items: "))

# Prompt user for the number of items per box
iperbox = int(input("Enter the number of items per box: "))

# Calculate the number of boxes needed
nboxes = items / iperbox

# Store number of boxes as a whole number
boxes = math.ceil(nboxes)

# Return to the user the number of boxes according to the input
print(f"For {items} items, packing {iperbox} items in each box, you will need {boxes} boxes.")