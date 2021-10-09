import time
import string

codedmessage = input('enter the coded message\n')
codedmessage = codedmessage.translate(codedmessage.maketrans('', '', string.punctuation))
codedmessage = codedmessage.lower()
wordtext = open('path to your words.txt file')
line = wordtext.readline()
wordlist = []
for line in wordtext:
    word = line.strip()
    wordlist.append(word)
words = codedmessage.split()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
solution = []
successful = []
unique = []
thedict = {}

for n in range(1, 52):
    for w in words:
        wordsolution = ''
        for i in w:
            index = alphabet.index(i)
            index = index + n
            letter = alphabet[index]
            wordsolution += letter
        print(wordsolution)
        if wordsolution in wordlist:
            successful.append(n)
            solution.append(wordsolution)
        
for i in successful:
    if i not in unique:
        unique.append(i)

for u in unique:
    if successful.count(u) >= 0.85 * len(words):
        theshift = u

solution = []


for w in words:
    wordsolution = ''
    for i in w:
        index = alphabet.index(i)
        index += theshift
        letter = alphabet[index]
        wordsolution += letter
    solution.append(wordsolution)

print(solution)

#made by https://github.com/BoomanWill
