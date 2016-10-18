"""
this program calculate the frequency of character used in text. if looks at each word and get number of word used.
"""
import sys
import argparse
import os.path
import string
import matplotlib.pyplot as plt


htable = dict()
# character from a to z.
chr = list(string.ascii_lowercase)


def file():
    """
    read word from console and return all the all value to calling method.
    :return: all argument passed from console
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="a comma separated value unigram file")
    parser.add_argument("-o", "--output", help="display letter frequencies to standard output", action="store_true")
    parser.add_argument("-p", "--plot", help="plot letter frequencies using matplotlib", action="store_true")
    args = parser.parse_args()
    return args


def readfile(file):
    """
    read file and store tha data in hash table.
    :param file: name of the file to read from.
    :return: None
    """
    #  if the file exist in the system
    if (os.path.exists(file)):
        for line in open(file):

            line = line.lower()
            arr = line.split(",")
            #  looping through all character in word
            for ch in arr[0]:
                #  if word exist
                if ch in htable.keys():
                    # get the count
                    count = htable[ch]
                    #  add count and store updated value
                    htable[ch] = count + int(arr[2])
                else:
                    # store character to count
                    htable[ch] = int(arr[2])
    else:  # print("Error: " + file + " does not exist!\n")
        sys.stderr.write("Error: " + file + " does not exist!\n")
        sys.exit(1)


def showPlot(xlabel, ylabel,title, table):
    """
    show polt to the user
    :param xlabel: xlabel to print
    :param ylabel: ylabel to print
    :param title: title
    :param table: table to get data from
    :return: None
    """
    #  array to hold x and y values
    val = []
    key = []
    #  sort table by keys and iterate over it.
    for x in sorted(table.keys()):
        #  add value to the val array
        val.append(table[x])
        #  add value to the key array
        key.append(x)
    #  convert that array to tuple
    v = tuple(val)
    #  convert that array to tuple
    k = tuple(key)
    # make x with range of table
    plt.xticks(range(len(table)), k)
    # call bar function
    plt.bar(range(len(table)),v,width=0.9, bottom= None, hold=None, data=None,align='center')
    # ylable value added
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(title)
    # show plot
    plt.show()


def main():
    """
    program to calculate the letter frequency of each letter. it uses letter used in different perioud and graph the
    frequency of the character.
    :return:
    """
    #  get argument from user
    args = file()
    # read file from filename given by user.
    readfile(args.filename)

    total = 0
    # count total word used
    for x in htable.keys():
        total += htable[x]
    # calculate the value in number of word / total word to get in 1.0 form
    for x in chr:
        if x in htable.keys():
            count = htable[x]
            htable[x] = (count / total)
        else:
            # if word is not found it assign to 0.0
            htable[x] = 0.0
    # if user request output than print output in console
    if args.output:
        # sort dictionary by key
        for c in sorted(htable.keys()):
            print(c + ": " + str(htable[c]) )
    # if user request to plot, plot the graph
    if args.plot:
        showPlot("Letter", "Frequency", 'Letter Frequencies: '+ args.filename,htable)

# call main function
if __name__ == '__main__':
    main()
