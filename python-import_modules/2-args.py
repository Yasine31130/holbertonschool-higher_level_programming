#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

    argument == len(argv)
    if argument == 1:
        print("0 arguments.")
    elif argument == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(argument - 1))
    
    for i in range (1, argument):
        print("{}: {}".format(i, argv[i]))
