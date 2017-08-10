#defaultdict is imported so that the count of a word in the dictionary is 0 by default and does not have to be looked up
from collections import defaultdict



#this is test code using the files provided (commented out)

##textList = []
##textFiles = ['all-topics-strings.lc.txt', 'all-places-strings.lc.txt', 'all-people-strings.lc.txt']
##for textFile in textFiles:
##    textView = open(textFile, 'rb')
##    for word in textView:
##        textList.append(word.strip())
##    textView.close()
##
##
book = open('plot.txt', 'rb')
print book.readlines()


#returns a dictionary that maps from each word in the text files to a count of each word in the book
#textList is a consolidated list of all the words from the text files
#book is a list of lines from the large text file; assume each line is a list of words
def numOccurrences(textList, book):
    dataDict = defaultdict(int)
    for line in book:
        for word in textList:
            dataDict[word] += line.count(word)
    return dataDict
    
##book.close()

#Notes: the one-line-at-a-time reading is efficient in terms of memory usage; reading in the whole book file causes a memory 
