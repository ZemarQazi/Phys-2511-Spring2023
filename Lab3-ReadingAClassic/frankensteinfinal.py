#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 22:00:19 2023

@author: nav
"""

# Open the book
with open("/Users/nav/Downloads/frank.txt", "r") as file:
    book = file.read()

# Split the book into chapters
chapters = book.split("Chapter")

chapters.pop(0)


# Loop through each chapter and count the number of times the word "creature" appears
for i, chapter in enumerate(chapters):
    count1= chapter.count("creature")
    print(f"creature was printed in Chapter {i + 1} {count1} times")
    
for i, chapter in enumerate(chapters):
    count2 = chapter.count("Frankenstein")
    print(f"Frankenstein was printed in Chapter {i + 1} {count2} times")
    
for i, chapter in enumerate(chapters):
    count3 = chapter.count("Agatha")
    print(f"Agatha was printed in Chapter {i + 1} {count3} times")
    
for i, chapter in enumerate(chapters):
    count4 = chapter.count("Caroline")
    print(f"Caroline was printed in Chapter {i + 1} {count4} times")
    
for i, chapter in enumerate(chapters):
    count5 = chapter.count("De Lacey")
    print(f"De Lacey was printed in Chapter {i + 1} {count5} times")
    
for i, chapter in enumerate(chapters):
    count6 = chapter.count("Elizabeth")
    print(f"Elizabeth was printed in Chapter {i + 1} {count6} times")

for i, chapter in enumerate(chapters):
    count7 = chapter.count("Ernest")
    print(f"Ernest was printed in Chapter {i + 1} {count7} times")
    
for i, chapter in enumerate(chapters):
    count8 = chapter.count("Felix")
    print(f"Felix was printed in Chapter {i + 1} {count8} times")
    
for i, chapter in enumerate(chapters):
    count9 = chapter.count("Henry")
    print(f"Henry was printed in Chapter {i + 1} {count9} times")
    
for i, chapter in enumerate(chapters):
    count10 = chapter.count("Justine")
    print(f"Justine was printed in Chapter {i + 1} {count10} times")

for i, chapter in enumerate(chapters):
    count11 = chapter.count("William")
    print(f"William was printed in Chapter {i + 1} {count11} times")
    
    
# graphing the data 

import numpy as np
import matplotlib.pyplot as plt

my_file = open("/Users/nav/Downloads/frank.txt", "r") 

data = my_file.read()

fran = data.count("Frankenstein")
creatur = data.count("creature")
agath = data.count("Agatha")
carolin = data.count("Caroline")
lace = data.count("De Lacey")
li = data.count("Elizabeth")
ernes = data.count("Ernest")
feli = data.count("Felix")
henr = data.count("Henry")
justin = data.count("Justine")
willia = data.count("William")

data = {'Frank': fran, 'Creature': creatur, 'Agatha': agath, 'Caroline': carolin, 'De Lacey': lace, 'Elizabeth': li, 'Ernest': ernes, 'Felix': feli, 'Henry': henr, 'Justine': justin, 'William': willia}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (10, 5))

plt.bar(courses, values, color = 'maroon', width = 0.4)

plt.xlabel("Characters in Frankestein")
plt.ylabel("Number of times characters are mentioned")
plt.title("Frank")
plt.show()

print("Number of total ocurrences of the character Frankenstein:", fran)
print("Number of total ocurrences of the character creature:", creatur)
print("Number of total ocurrences of the character Agatha:", agath)
print("Number of total ocurrences of the character Caroline:", carolin)
print("Number of total ocurrences of the character De Lacey:", lace)
print("Number of total ocurrences of the character Elizabeth:", li)
print("Number of total ocurrences of the character Ernest:", ernes)
print("Number of total ocurrences of the character Felix:", feli)
print("Number of total ocurrences of the character Henry:", henr)
print("Number of total occurrences of the character Justine:", justin)
print("Number of total occurrences of the character William:", willia)

# Answering the questions assigned, hypothesis
if fran > 0: 
    print("They meet Frankenstein.") 

if creatur > 0: 
    print("They meet the creature.")
    
if creatur >= fran:
    print("creature had a good relationship with Victor.")
else: 
    print("creature had a bad relationship with Victor.")
    
if agath >= fran:
    print("agatha had a good relationship with Victor.")
else: 
    print("agatha had a bad relationship with Victor.")

if carolin >= fran:
    print("caroline had a good relationship with Victor.")
else: 
    print("caroline had a bad relationship with Victor.")
    
if lace >= fran:
    print("de lacey had a good relationship with Victor.")
else: 
    print("de lacey had a bad relationship with Victor.")
    
if li >= fran:
    print("elizabeth had a good relationship with Victor.")
else: 
    print("elizabeth had a bad relationship with Victor.")
    
if ernes >= fran:
    print("ernest had a good relationship with Victor.")
else: 
    print("ernest had a bad relationship with Victor.")
    
if feli >= fran:
    print("felix had a good relationship with Victor.")
else: 
    print("felix had a bad relationship with Victor.")
    
if henr >= fran:
    print("henry had a good relationship with Victor.")
else: 
    print("henry had a bad relationship with Victor.")

if justin >= fran:
    print("justine had a good relationship with Victor.")
else: 
    print("justine had a bad relationship with Victor.")
    
if willia >= fran: 
    print("william had a good relationship with Victor.")
else: 
    print("william had a bad relationship with Victor.")