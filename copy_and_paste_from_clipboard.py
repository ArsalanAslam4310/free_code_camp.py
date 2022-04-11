#! python3
# bulletpointadder.py - adds wikipedia bullet point to the star
# of each line of text on the clipboard.
import pyperclip 

text = pyperclip.paste()
# step 2
# todo: separate lines and add stars.

printclip.copy(text)

# seperate line and stars.
lines =text.split('\n')
for i in range(len(lines)): # loop through all indexes in the 'lines' list  
    lines[i] ='*' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines)

pyperclip.copy(text)
 
