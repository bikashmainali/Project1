"""
This program compute the popularity of a word in terms of the number of occurrences of all words over all year.
"""
import argparse
import sys
import os
import operator
import matplotlib.pyplot as plt
#  to store data hash table
hTable = {}

# word class
class Word:
    """
    defines a word class that can store word, rank and count of the word used.
    """
    def __init__(self, word, rank, count):
        """
        initialize word , rank and count of the word
        :param word: word
        :param rank: rank of the word
        :param count: count of the word
        """
        self.word = word
        self.rank = rank
        self.count = count

    def __str__(self):
        """
        string representation of the string
        :return: string containing word, rank and count
        """
        txt = (str(self.word) + " " + str(self.rank) + " " + str(self.count))
        return txt


def file():
    """
    read user input from the console
    :return: return all the argument passed by the user.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("word", help="a word to display the overall ranking of")
    parser.add_argument("filename", help="a comma separated value unigram file")
    parser.add_argument("-o", "--output", help="display the top OUTPUT (#) ranked words by number of occurrences")
    parser.add_argument("-p", "--plot", help="plot the word rankings from top to bottom based on occurrences",
                        action="store_true")
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
        #  for each line in the file
        for line in open(file):
            # split data in ','
            data = line.split(",")
            #  if that word already exists in out dictionary
            if data[0] in hTable:
                previouscount = hTable[data[0]].count
                newCount = int(previouscount) + int(data[2])
                # create new word with updated count
                word = Word(data[0], count=newCount, rank=0)
                # store that word
                hTable[data[0]] = word
            else:
                # if read word is not found in out dictionary than create new word
                word = Word(data[0], count=int(data[2]), rank=0)
                # store that data in out dictionary
                hTable[data[0]] = word
        # arary to store data
        li = []
        # reverse sort dictionary value by count of that word
        for w in (sorted(hTable.values(), key=operator.attrgetter('count'), reverse=True)):
            li.append(w)
        #  loop to store position
        a = 1
        for x in li:
            if x.word in hTable.keys():
                cou = hTable[x.word].count
                wod = Word(word=x.word, count=cou, rank=a)
                hTable[x.word] = wod
                a += 1
    else:  # print("Error: " + file + " does not exist!\n")
        sys.stderr.write("Error: " + file + " does not exist!\n")
        sys.exit(1)


def printword(wor, filename):
    """
    print the word by ranking
    :param wor: word to print
    :param filename: file name to print if word is not found
    :return: return word count and word rank
    """
    if wor in hTable.keys():
        #  print rank
        print(str(wor) + " is ranked #" + str(hTable[wor].rank))
        # return hTable[wor].count, hTable[wor].rank
    else:
        print("Error: " + wor + " does not appear in " + str(filename))
        sys.exit(1)

def plot(word, file):
    """
    plot all data in file and plot specific word in that is given by the user
    :param word: word to print
    :param file: filename to print on top
    :return: NONE
    """
    #  array to store key and value
    x = []
    y = []
    #  reverse sort htable value by value attribute count.
    for w in (sorted(hTable.values(), key=operator.attrgetter('count'), reverse=True)):
        x.append(w.rank)
        y.append(w.count)
    #  convert array to tuple
    x1 = tuple(x)
    y1 = tuple(y)
    # plot
    plt.loglog(x1, y1, "-h")
    # specific plot for that word given
    plt.loglog(int(hTable[word].rank), int(hTable[word].count), "*", color="red", markersize=12, label=word)
    # print word in special place
    plt.text(int(hTable[word].rank) + 0.1 * int(hTable[word].rank),
             int(hTable[word].count) + 0.3 * int(hTable[word].count), word)
    t = file.split('/')
    plt.title("word frequency: " + t[1])
    plt.ylabel("Total number of occurrences")
    plt.xlabel("Rank of word (\"" + word + "\" is rank " + str(hTable[word].rank) + ")")
    #  code to adjust plot
    subplot = plt.subplot()
    subplot.autoscale_view(True, True, True)
    plt.show()

def printnumber(number):
    """
    if user want output than print output in rank
    :param number: number of word to print by rank
    :return:
    """
    count = 0
    # reverse sort htable by the value attribute count
    for w in (sorted(hTable.values(), key=operator.attrgetter('count'), reverse=True)):
        if count < number:
            print("#" + str(hTable[w.word].rank) + ": " + str(hTable[w.word].word) + " -> " + str(hTable[w.word].count))
            count += 1
        else:
            break

def main():
    """
    This program compute the popularity of a word in terms of the number of occurrences of all words over all years
    :return: NONE
    """
    #  get user input from file
    args = file()
    # call reafile method to read data from passed filename
    readfle(args.filename)
    # print word and it's ranking
    printword(args.word, args.filename)
    # if user want output in then print output in the console
    if args.output:
        printnumber(int(args.output))
    # if user want to plot data then plot that that
    if args.plot:
        plot(args.word, args.filename)

# call main method
if __name__ == '__main__':
    main()
