#!/usr/bin/env python
import argparse
import sys
import codecs

if sys.version_info[0] == 2:
    from itertools import izip
else:
    izip = zip
from collections import defaultdict as dd
import re
import os.path
import gzip
import tempfile
import shutil
import atexit

# Use word_tokenize to split raw text into words
from string import punctuation

import nltk
from nltk.tokenize import word_tokenize, TweetTokenizer

scriptdir = os.path.dirname(os.path.abspath(__file__))

reader = codecs.getreader('utf8')
writer = codecs.getwriter('utf8')


def prepfile(fh, code):
    if type(fh) is str:
        fh = open(fh, code)
    ret = gzip.open(fh.name, code if code.endswith("t") else code + "t") if fh.name.endswith(".gz") else fh
    if sys.version_info[0] == 2:
        if code.startswith('r'):
            ret = reader(fh)
        elif code.startswith('w'):
            ret = writer(fh)
        else:
            sys.stderr.write("I didn't understand code " + code + "\n")
            sys.exit(1)
    return ret


def addonoffarg(parser, arg, dest=None, default=True, help="TODO"):
    ''' add the switches --arg and --no-arg that set parser.arg to true/false, respectively'''
    group = parser.add_mutually_exclusive_group()
    dest = arg if dest is None else dest
    group.add_argument('--%s' % arg, dest=dest, action='store_true', default=default, help=help)
    group.add_argument('--no-%s' % arg, dest=dest, action='store_false', default=default, help="See --%s" % arg)


class LimerickDetector:
    def __init__(self):
        """
        Initializes the object to have a pronunciation dictionary available
        """
        self._pronunciations = nltk.corpus.cmudict.dict()

    def apostrophe_tokenize(self, word):
        """
        Handles the tokenization of apostrophes correctly
        """
        aposToken = TweetTokenizer()
        return aposToken.tokenize(word)



    def num_syllables(self, word):
        """
        Returns the number of syllables in a word.  If there's more than one
        pronunciation, take the shorter one.  If there is no entry in the
        dictionary, return 1.
        """

        # TODO: provide an implementation!
        word = word.lower()
        min_syllable_count = sys.maxint
        if word in self._pronunciations:
            pronunciation_list = self._pronunciations[word]
            # print pronunciation_list
            for pronunciation in pronunciation_list:
                syllable_count = str(pronunciation).count('0') + str(pronunciation).count('1') + str(
                    pronunciation).count(
                    '2')
                # print syllable_count
                if syllable_count < min_syllable_count:
                    min_syllable_count = syllable_count

            # print "Minimum syllable is ", min_syllable_count
            return min_syllable_count

        else:
            # print "No entry found"
            return 1

    def rhymes(self, a, b):
        """
        Returns True if two words (represented as lower-case strings) rhyme,
        False otherwise.
        """
        a = a.lower()
        b = b.lower()
        a_cutlist = list()
        b_cutlist = list()
        if a in self._pronunciations:
            a_pronunciation_list = self._pronunciations[a]
            #print a_pronunciation_list
            for each_a_pronunciations in a_pronunciation_list:
                #print "Each pronunciation",each_a_pronunciations
                #print len(each_a_pronunciations)
                #print type(each_a_pronunciations)
                for element in each_a_pronunciations:
                    if '0' in element or '1' in element or '2' in element:
                        index = each_a_pronunciations.index(element)
                        a_cutlist.append(each_a_pronunciations[index:len(each_a_pronunciations)])
                        break
            #print "Cut off list A ",a_cutlist

        if b in self._pronunciations:
            b_pronunciation_list = self._pronunciations[b]
            #print b_pronunciation_list
            for each_b_pronunciations in b_pronunciation_list:
                #print "Each pronunciation",each_b_pronunciations
                #print len(each_b_pronunciations)
                #print type(each_b_pronunciations)
                for element in each_b_pronunciations:
                    if '0' in element or '1' in element or '2' in element:
                        index = each_b_pronunciations.index(element)
                        b_cutlist.append(each_b_pronunciations[index:len(each_b_pronunciations)])
                        break
            #print "Cut off list B ",b_cutlist
        #print "Length of List A",len(a_cutlist)," Length of List B",len(b_cutlist)


        for each_a in a_cutlist:
            for each_b in b_cutlist:
                #print "Each_a:",each_a," Each_b:",each_b," Length of each_a:",len(each_a)," Length of each_b:",len(each_b)
                if len(each_a) >= len(each_b):
                    if each_b[-len(each_b):] == each_a[-len(each_b):]:
                        #print "Rhymes!"
                        return True
                else:
                    if each_a[-len(each_a):] == each_b[-len(each_a):]:
                        #print "Rhymes!"
                        return True
                #print "--------------------------"
        # TODO: provide an implementation!
        #print "Does not Rhyme :(!"
        #print "--------------------------"
        return False

    def is_limerick(self, text):
        """
        Takes text where lines are separated by newline characters.  Returns
        True if the text is a limerick, False otherwise.

        A limerick is defined as a poem with the form AABBA, where the A lines
        rhyme with each other, the B lines rhyme with each other, and the A lines do not
        rhyme with the B lines.


        Additionally, the following syllable constraints should be observed:
          * No two A lines should differ in their number of syllables by more than two.
          * The B lines should differ in their number of syllables by no more than two.
          * Each of the B lines should have fewer syllables than each of the A lines.
          * No line should have fewer than 4 syllables

        (English professors may disagree with this definition, but that's what
        we're using here.)


        """
        t_lines =text.splitlines()

        last_word = []

        print "T-lines", t_lines

        number_array = []
        for each in t_lines:
            each = each.strip()
            if each == '' or each == None:
                continue
            tokenized_lines = word_tokenize(each)
            #tokenized_lines = self.apostrophe_tokenize(each)
            new_tokenized = []
            sum_line =0
            for each1 in tokenized_lines:
                x = re.sub('[^a-zA-Z0-9]', "", each1)
                if x != '' and x != None:
                    new_tokenized.append(x)
                    sum_line += self.num_syllables(x)
            number_array.append(sum_line)
            print "New-Tokenized", new_tokenized
            last_word.append(new_tokenized[-1])
        print "Number_array", number_array
        print "Last word", last_word

        # TODO: provide an implementation!

        if len(number_array) != 5:
            print "Size less than 5"
            return False
        if self.rhymes(last_word[0],last_word[1]) != True or self.rhymes(last_word[0],last_word[4])!= True or self.rhymes(last_word[1],last_word[4])!=True:
            print "All A's don't rhyme"
            return False
        if self.rhymes(last_word[2],last_word[3]) != True:
            print "All B's don't rhyme"
            return False
        if self.rhymes(last_word[0],last_word[2]):
            print "Line 1 and 3 rhyme! :o"
            return False
        if self.rhymes(last_word[0],last_word[3]):
            print "Line 1 and 4 rhyme! :o"
            return False
        if self.rhymes(last_word[1],last_word[2]):
            print "Line 2 and 3 rhyme! :o"
            return False
        if self.rhymes(last_word[1],last_word[3]):
            print "Line 2 and 4 rhyme! :o"
            return False
        if self.rhymes(last_word[4],last_word[2]):
            print "Line 5 and 3 rhyme! :o"
            return False
        if self.rhymes(last_word[4],last_word[3]):
            print "Line 5 and 4 rhyme! :o"
            return False
        if (2 < abs(number_array[0]-number_array[1])) or (2 < abs(number_array[0]-number_array[4])) or (2 < abs(number_array[1]-number_array[4])):
            print "A-A>2"
            return False
        if (2 < abs(number_array[3]-number_array[2])):
            print "B-B>2"
            return False
        if number_array[2]>=number_array[0] or number_array[2]>=number_array[1] or number_array[2]>=number_array[4]:
            print "B>A for line 3"
            return False
        if number_array[3]>=number_array[0] or number_array[3]>=number_array[1] or number_array[3]>=number_array[4]:
            print "B>A for line 4"
            return False
        for e in number_array:
            if e < 4:
                return False
        print "-------------------------"
        return True


# The code below should not need to be modified
def main():
    parser = argparse.ArgumentParser(
        description="limerick detector. Given a file containing a poem, indicate whether that poem is a limerick or not",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    addonoffarg(parser, 'debug', help="debug mode", default=False)
    parser.add_argument("--infile", "-i", nargs='?', type=argparse.FileType('r'), default=sys.stdin, help="input file")
    parser.add_argument("--outfile", "-o", nargs='?', type=argparse.FileType('w'), default=sys.stdout,
                        help="output file")

    try:
        args = parser.parse_args()
    except IOError as msg:
        parser.error(str(msg))

    infile = prepfile(args.infile, 'r')
    outfile = prepfile(args.outfile, 'w')

    ld = LimerickDetector()
    lines = ''.join(infile.readlines())
    outfile.write("{}\n-----------\n{}\n".format(lines.strip(), ld.is_limerick(lines)))


if __name__ == '__main__':
    main()
