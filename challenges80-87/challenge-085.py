name = str(input('Enter your name ? : '))
vowel = ['a', 'i', 'e' 'o', 'u']
count = 0
for i in name:
    if i.lower() in vowel:
        count = count + 1
print('the number of vowels in your name {0}'.format(count))
