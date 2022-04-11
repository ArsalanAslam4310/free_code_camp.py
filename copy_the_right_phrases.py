#! python3
# mclip.py - A multi-clipboard program. 

text={'agree': """yes,I agree.That sound fine to me.""","busy":"""sorry, can we do this later this week or next week?""","upsell":"""Would you consider making this a monthly donation"""}

import sys
if len(sys.argv) < 2:
    print("usage: python mclip.py[keyphrase] - copy phrase text")
    sys.exit()

key_phrase=sys.arg[1] #fist command line arg is the key_phrase

if key_phrase in text:
    pyperclip.copy(text[key_phrase])
    print("test for " + key_phrase + "copied to clipboard.")
else:
    print("there is no text for " + key_phrase)
