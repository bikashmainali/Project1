import argparse
import sys
import os.path
import collections
import time

#  dictionary to hold data
hTable = {}

def file():
    """
    read word from console and return all the all value to calling method.
    :return: all argument passed from console
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("word", help="a word to display the total occurrences of")
    parser.add_argument("filename", help="a comma separated value unigram file")
    #  get all argument from console and return
    args = parser.parse_args()
    return args

def readfle(file):
    """
    read file and store tha data in hash table.
    :param file: name of the file to read from.
    :return: None
    """
    #  if the file exist in the system
    if (os.path.exists(file)):
        #  for every line in file
        for line in open(file):
            # split line in ','
            data = line.split(",")
            # create string with word and year
            #  if tup is already in htable
            if data[0] in hTable:
                # get previous count
                previouscount = hTable[data[0]]
                #  add new previous count to this word count
                newCount = int(previouscount) + int(data[2])
                # store in table
                hTable[data[0]] = newCount
            else:
                # store new word to table
                hTable[data[0]] = data[2]
    else:  # print("Error: " + file + " does not exist!\n")
        sys.stderr.write("Error: " + file + " does not exist!\n")
        # exit from program.
        sys.exit(1)

def printword(wor):
    """
    print word and and count of the word.
    :param wor: word to lookup
    :return: None
    """
    if wor in hTable:
        print(wor + " : " + str(hTable[wor]))
    else:
        print("Error: " + wor + " does not appear!")

def main():
    """
    this word_count program count number of time the word is used in text. pattern is word , year, count
    it look the word and see if the word is used before store total number of count.
    :return:
    """
    #  calls file method to read from console
    args = file()
    #  send to read from file by passing filename of the text
    readfle(args.filename)
    #  call print word method.
    printword(args.word)

# call main method
if __name__ == '__main__':
    main()
