import sys
import string
import re
import base64
#import png
#import Image
import pdb

def storewordsfromfile():
    """
    Open and read the lines in the file
    For every word in the line.split() remove whitespace and punctuations
    Create a dict with first character of the word as the key
    and its value to be a list containing the word along with its frequency
    """
    print storewordsfromfile.__doc__
    #pdb.set_trace()
    fp = open(sys.argv[1], 'rb')
    print fp
    #with open(sys.argv[1], 'rb') as fp:
    data = fp.readlines()
    #print type(data)
    #if '.png' in sys.argv[1]:
        #str = base64.b64encode(fp.read())
        #print str

    d = {}

    for line in data:
        #print line

        for word in line.split():
            #print 'word in file', word
            word = word.strip(string.whitespace + string.punctuation)
            word = word.lower()
            #print 'word after strip: ', word

            if word is "":
                #  If a word after strip operation becomes empty, break and continue with next word
                break

            if word[0] in d:
                flag  = 0 # If word is present in the list and only its freq is updated this flag is set to 1.

                for litem in d[word[0]]:

                    if word == litem[0]:
                        index = d[word[0]].index(litem)
                        d[word[0]][index][1] = d[word[0]][index][1]+1
                        flag = 1 # Freq updated
                        break

                # If flag is 1 this loop is not executed else the new word is apeended to the list with freq set to 1
                if flag != 1:
                   d[word[0]].append([word,1])

            # If key not present add the key
            else:
                d[word[0]] = [[word, 1]]

    print '\nStored Dict: ', d
    if d:
        return d
    else:
        print 'No valid data in file'
        return False

    #Sampledict = {'a': ['average', 'assume', 'average', 'assumes', 'are', 'at', 'all'], 'c': ['case', 'collisions', 'case'], 'd': ['dance', 'dict'], 'f': ['for', 'function', 'for', 'from'], 'i': ['is', 'in'], 'h': ['hi', 'hello', 'hash'], 'k': ['keys', 'keys'], 'm': ['make'], 'l': ['listed'], 'o': ['objects', 'objects', 'of'], 'n': ['ninad'], '1': ['123words'], 'p': ['prethi', 'parameters'], 's': ['sufficiently', 'selected', 'set'], 'r': ['robust', 'random'], 'u': ['uncommon', 'used', 'uniformly'], 't': ['the', 'times', 'that', 'the', 'the', 'to', 'the', 'the', 'the'], '7': ['78words'], 'z': ['zebra']}

    # After modifications:
    # Stored Dict:  {'a': [['average', 2], ['assume', 1], ['assumes', 1], ['are', 1], ['at', 1], ['all', 1]], 'c': [['case', 2], ['collisions', 1]], 'd': [['dance', 1], ['dict', 1]], 'f': [['for', 2], ['function', 1], ['from', 1]], 'i': [['is', 1], ['in', 1]], 'h': [['hi', 1], ['hello', 1], ['hash', 1]], 'k': [['keys', 2]], 'm': [['make', 1]], 'l': [['listed', 1]], 'o': [['objects', 2], ['of', 1]], 'n': [['ninad', 1]], '1': [['123words', 1]], 'p': [['prethi', 1], ['parameters', 1]], 's': [['sufficiently', 1], ['selected', 1], ['set', 1]], 'r': [['robust', 1], ['random', 1]], 'u': [['uncommon', 1], ['used', 1], ['uniformly', 1]], 't': [['the', 6], ['times', 1], ['that', 1], ['to', 1]], '7': [['78words', 1]], 'z': [['zebra', 1]]}

def findwordandfreq(d):
    """
    Prompt the user to enter a word to search in the file
    If no input is given, consider as invalid input
    If inputs first character is special character consider as invalid input
    """
    print findwordandfreq.__doc__
    #is_valid = 0
    findword = raw_input('Enter a word to search: ')

    """while not is_valid:

        try:
            findword = str(raw_input('Enter a word to search: '))
            is_valid = 1
        except ValueError, e:
            print ("'%s' is not a valid string." % e.args[0].split(": ")[1])"""

    while findword is "" or findword[0] in string.punctuation:
        print 'Provide a valid input and also special characters are not allowed'
        findword = raw_input('Enter a word to search: ')
        #return

    print 'Find: ', type(findword)

    findword = findword.strip(string.whitespace)
    findword = findword.lower()

    # regex
    """if findword[0] in d:
        print 'Dict Value for key %s is %s' % (findword[0], d[findword[0]])
        r=re.compile(findword)
        new = filter(r.match, d[findword[0]])
        print new
        print 'frequency of the %s is %d' % (findword, len(new))"""

    wordpresent = 0

    #print 'findword[0]: ', findword[0]
    if findword[0] in d:
        print 'Dict Value for key %s is %s' % (findword[0], d[findword[0]])

        for litem in d[findword[0]]:

            for item in litem:

                if item == findword:
                    wordpresent = 1
                    print 'Word %s is in the list with frequency %s ' % (item, litem[1])

        if wordpresent != 1:
            print '\nWord not in file'

    else:
        print '\nWord not in file'


def main():
    """ Main function - Open file, save to dict of lists; find a word and its frequency"""
    newdict = storewordsfromfile()
    if newdict is not False:
        findwordandfreq(newdict)

if __name__ == '__main__':
    main()
