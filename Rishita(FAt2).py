from pprint import pprint
string = input()
for i in range(0, len(string)-1):
    if not string[i].isalpha() and string[i] != " " and string[i+2].islower():
        print("Invalid input")
        exit(0)
words = []

for i in string.split(" "):
    if not i[-1].isalpha():
        words.append(i[:len(i)-1].lower())
    else:
        words.append(i.lower())

unique_words = set(words)
dictionary = dict()

for word in unique_words:
    count = 1
    dictionary[word] = words.count(word)
    while word in words:
        words.remove(word)
pprint(dictionary)