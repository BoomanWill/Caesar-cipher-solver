import time

codedmessage = input('enter the coded message with no punctuation in all lower case, and numbers must be written out\n')
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
        time.sleep(0.005)
        if wordsolution in wordlist:
            successful.append(n)
            solution.append(wordsolution)
        
for i in successful:
    if i not in unique:
        unique.append(i)

for u in unique:
    if successful.count(u) >= len(words):
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
