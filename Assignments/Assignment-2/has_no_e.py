def has_no_e(word):
    for letter in word:
        if (letter =='e') or (letter == 'E'):
            return False
    return True    

reader = open('gadsby_stripped.txt')
for words in reader:
    word = words.strip()
    has_no_e(word)


