# English to pig latin
from email import message


print("Enter the English message to translate into pig latin:")
message=input()

vowel =('a', 'e','i', 'o', 'u', 'y')
pig_latin =[] # a list of the words in pig latin


for word in message.split():
    # seperate the non-letters at the start of this word:
    prefix_non_letters =''
    while len(word) > 0 and not word[0].isalpha():
        prefix_non_letters += word[0]
        word=word[1:]
    if len(word)==0:
        pig_latin.append(prefix_non_letters)
        continue
    #seperate the non_letters at the end of this word:
    suffix_non_letter=''
    while not word[-1].isalpha():
        suffix_non_letter += word[-1]
        word = word[:-1]
    # remember if the word was in uppercase or title case.
    was_upper=word.isupper()
    was_title=word.istitle()
    word=word.lower() # make the word lower case for translation.
    #seperate the consonants at the start of this word:
    prefix_consonants=''
    while len(word)>0 and not word[0] in vowel:
        prefix_consonants += word[0]
        word = word[1:]

    # add the pig latin ending to the word:
    if prefix_consonants != '':
        word += prefix_consonants + 'ay'
    else:
        word += 'yay'

        # set the word back to uppercase or titlecase

    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()

    # add the non_letter back to the start or end of the word.
    pig_latin.append(prefix_non_letters + word + suffix_non_letter)
    # join all the words back togethor into a single string:

print(' '.join(pig_latin))




pig_latin = []
for word in message.split():
    prefix_non_letters=''
    while len(word)> 0 and not word[0].isalpha():
        prefix_non_letters +=word[0]
        word = word[1:]
    if len(word)==0:
        pig_latin.append(prefix_non_letters)
        continue
    # seperate the non-letters at the end of this word:
    suffix_non_letter=''
    while not word[-1].isalpha():
        suffix_non_letter += word[-1]
        word = word[:-1]

    # remember if the word was in uppercase or title case.
    was_upper=word.isupper()
    was_title=word.istitle()

    word = word.lower() # make the word lowercase for translation.

    # seperate the consonants at the start of this word:
    prefix_consonants = ''
    while len(word)> 0 and not word[0] in vowel:
        prefix_consonants += word[0]
        word=word[1:]

    # add the pig latin ending to the word:
    if prefix_consonants != '':
        word += prefix_consonants + 'ay'
    else:
        word +='yay'

    #set the word back to uppercase or title case:
    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()

    # add the non-letters back to the start or end of the word.
    pig_latin.append(prefix_non_letters + word + suffix_non_letter)

    # join all the word back together into a single string:
print(' '.join(pig_latin))