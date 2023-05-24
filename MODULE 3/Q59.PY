# Write a Python program to read a random line from a file.
import random
def random_line(a):
    lines = open(a).read().splitlines()          # USING SPLITLINES FUNCTION SPLIT THE LINE
    return random.choice(lines)            # FOR RANDOM LINE READ
print(random_line('pratik.txt'))                   
