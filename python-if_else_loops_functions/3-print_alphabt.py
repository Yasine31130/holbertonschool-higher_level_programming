#!/usr/bin/python3
letters_to_skip = ['e', 'q']
for alphabet in range(97, 123):
    if chr(alphabet) in letters_to_skip:
        continue
    #if chr(alphabet) == 'q' or chr(alphabet) == 'e':
     #   continue
    print("{}".format(chr(alphabet)), end="")
