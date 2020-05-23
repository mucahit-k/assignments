sentence = input('Enter a sentence ')
sent_list = list(sentence)
d = {}

for letter in set(sent_list):
    c = sent_list.count(letter)
    d[letter] = c
print(d)