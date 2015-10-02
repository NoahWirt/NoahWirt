"""Absolute crap right now. Sentences will be completely incoherent.
Always gives the same combinations of syllable i.e. 1, 2, 3 for a five syllable sentence.
"""

import random, sys

print "This is a program used to generate random haiku passages."

#Defines words with certain numbers of syllables.
one_syllable = ["A", "The", "Green", "Maul", "Caste", "Eat", "Mars"]
two_syllable = ["Lossless", "British", "Purple", "Current", "Orbit", "Rabbit", "Paper", "Pencil", "Pizza", "Music", "Summer", "Shampoo"]
three_syllable = ["Illegal", "Syllable", "Organic", "Absolute", "Substantial", "Icecream Cone"]
four_syllable = ["Arithmetic", "Irregular", "Identical", "American", "Arguable", "Vegetable", "Supermarket"]

#Defines function that generates the haiku.

def generate_haiku():
    print random.choice(one_syllable), random.choice(two_syllable), random.choice(two_syllable) 
    print random.choice(four_syllable), random.choice(two_syllable), random.choice(one_syllable) 
    print random.choice(one_syllable), random.choice(three_syllable), random.choice(one_syllable) 

#Asks if user wants to generate a haiku passage.

while True:
    x = raw_input("Do you want to generate a haiku (Y/N)")

    x = x.lower()

    if x == "y":
        generate_haiku()
    elif x == "n":
        print "Too bad."
        raw_input("")
        sys.exit()
    else:
        print "Not accepted value."
