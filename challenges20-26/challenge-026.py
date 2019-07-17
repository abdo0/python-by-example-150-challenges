word = str(input('Please enter a word : '))
first = word[0]
length = len(word)
rest = word[1:length]
if first != 'a' and first != 'e' and first != 'i' and first != 'o' and first != 'u':
    newword = rest + first + 'ay'
else:
    newword = word+'ay'
print(newword)
