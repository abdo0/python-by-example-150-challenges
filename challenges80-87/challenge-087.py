string = str(input('Enter a word : '))
length = len(string)
count = 1
for i in string:
    position = length - count
    letter = string[position]
    print(letter)
    count = count + 1
# easy way is type string[::-1]
