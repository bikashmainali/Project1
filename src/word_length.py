"""
This program can compute the average word length over a range of years.
"""
import argparse
import sys
import os
import matplotlib.pyplot as plt


class Word:
    """
    define word that class that can store numberOfWord and total wordlength
    """

    def __init__(self, numberOfWord, totalWordlength):
        """
        initialize numberOfWord and totalWordlength
        :param numberOfWord: number of word fount
        :param totalWordlength: total word length
        """
        self.numberOfWord = numberOfWord
        self.totalWordlength = totalWordlength

    def __str__(self):
        """
        string representation of word
        :return: text containg string representation of word
        """
        txt = "WordCount = " + str(self.numberOfWord) + " Len = " + str(self.totalWordlength)
        return txt


hTable = {}


def file():
    """
    read user input from the console
    :return: return all the argument passed by the user.
    """
    # create argument parser object
    parser = argparse.ArgumentParser()
    parser.add_argument("start", help="the starting year range", type=int)
    parser.add_argument("end", help="the ending year range", type=int)
    parser.add_argument("filename", help="a comma separated value unigram file")
    parser.add_argument("-o", "--output", help="display the average word lengths over years", action="store_true")
    parser.add_argument("-p", "--plot", help="plot the average word lengths over years", action="store_true")
    args = parser.parse_args()
    return args


def readfle(file):
    """
      read data from the file given.
      :param file: name of the file to read from
      :return: None
    """
    # if path exists in the file
    if (os.path.exists(file)):
        # for each line in file
        for line in open(file):
            #  split data in ','
            data = line.split(", ")
            # if year in table
            if data[1] in hTable.keys():
                # calculate new count by passing new word count and previous word count
                numOfWord = int(hTable[data[1]].numberOfWord) + int(data[2])
                totalWordlength = int(hTable[data[1]].totalWordlength)
                # calculate this word length by multiplying word length with repetition of word
                thisWordlength = int(int(len(data[0])) * int(data[2]))
                # store year
                hTable[data[1]] = Word(numOfWord, (thisWordlength + totalWordlength))
            else:
                #  count length
                length = int(len(data[0])) * int(data[2])
                #  store that year
                hTable[data[1]] = Word(data[2], length)
        # change word to represent in 1.0 value or in vercentage value
        for x in hTable.keys():
            hTable[x] = str(hTable[x].totalWordlength / hTable[x].numberOfWord)
    else:  # print("Error: " + file + " does not exist!\n")
        sys.stderr.write("Error: " + file + " does not exist!\n")
        sys.exit(1)


def plotgraph(args):
    """
    arrange all
    :param args: all argument passed by user
    :return: NONE
    """
    #  array to store x and y value
    x = []
    y = []
    #  get range of year from start year to end
    for a in range(args.start, args.end + 1):
        #  convert that year to sting
        a = str(a)
        if a in hTable.keys():
            #  if year in htable add year to x and value to y
            x.append(a)
            y.append(hTable[a])
        else:
            #  if year in not in htable add year to x and 0 to y
            x.append(a)
            y.append(0)
    # plot graph
    plt.plot(x, y)
    #  file name extraction
    t = args.filename.split('/')
    #  set tile
    plt.title("Average word lengths from " + str(args.start) + " to " + str(args.end) + ": " + t[1])
    plt.ylabel("Average word length")
    plt.xlabel("Year")
    #  show plot
    plt.show()


def main():
    """
    This program can compute the average word length over a range of years.
    :return: NONE
    """
    # get all argument passed by user
    args = file()
    # if given range is not valid
    if (args.start > args.end):
        print("Error: start year must be less than or equal to end year!")
        sys.exit(1)
    else:
        # read data from file name
        readfle(args.filename)
    # if user request output
    if args.output:
        # range from start year to end
        for x in range(args.start, args.end + 1):
            # convert calue to string
            x = str(x)
            if x in hTable.keys():
                print(str(x) + " : " + hTable[x])
            else:
                print(str(x) + " : 0")

    # if user request plot
    if args.plot:
        plotgraph(args)


# call main function
if __name__ == '__main__':
    main()
