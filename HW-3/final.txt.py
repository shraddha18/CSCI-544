#!/usr/bin/env python
from collections import defaultdict
from csv import DictReader, DictWriter
import string
import nltk
import codecs
import sys
import enchant
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.tokenize import TreebankWordTokenizer
from nltk.stem.snowball import SnowballStemmer
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
import  collections
from nltk import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

kTOKENIZER = TreebankWordTokenizer()
stop_words = set(stopwords.words('english'))
enc = enchant.Dict('en_GB')
#lemma = nltk.wordnet.WordNetLemmatizer()

def morphy_stem(word):
    """
    Simple stemmer
    """
    #stem = wn.morphy(word)
    stem = SnowballStemmer('english').stem(word)
    #stem = lemma.lemmatize(stem2)
    if stem:
        return stem.lower()
    else:
        return word.lower()


class FeatureExtractor:
    def __init__(self):
        """
        You may want to add code here
        """

        None

    def features(self, text):
        d = defaultdict(int)
        for i in string.punctuation:
            d[i] = text.count(i)
        for i in ["'s","'d","'st"]:
            d[i] = text.count(i)
        for i in ["1","4"]:
         	d[i] = text.count(i)


        d["len_text"] = len(text)
        text = text.translate(None, string.punctuation)
        d["len_text_after_removing_punc"] = len(text)
        #bigram_finder = BigramCollocationFinder.from_words(kTOKENIZER.tokenize(text))
        #bigrams = bigram_finder.nbest(BigramAssocMeasures.chi_sq, 200)
		#d["length_of_bigrams"] = len(bigrams)
        #for each in bigrams:
        #    each2 = (SnowballStemmer('english').stem(each[0]),SnowballStemmer('english').stem(each[1]))
        #    d[each2] += 1

        for ii in kTOKENIZER.tokenize(text):
            #d["no_of_words_line"] = len(kTOKENIZER.tokenize(text))

            if ii not in stop_words:
                d[morphy_stem(ii)] += 1
            else:
                d["no_of_stop_words"] = d.get("no_of_stop_words",0)+1



            #if enc.check(morphy_stem(ii)) == "True":
            #    d["correct spelling"] = d.get("correct spelling",0)+1
            #else:
            #    d["incorrect spelling"] = d.get("incorrect spelling",0)+1


        return d
reader = codecs.getreader('utf8')
writer = codecs.getwriter('utf8')


def prepfile(fh, code):
  if type(fh) is str:
    fh = open(fh, code)
  ret = gzip.open(fh.name, code if code.endswith("t") else code+"t") if fh.name.endswith(".gz") else fh
  if sys.version_info[0] == 2:
    if code.startswith('r'):
      ret = reader(fh)
    elif code.startswith('w'):
      ret = writer(fh)
    else:
      sys.stderr.write("I didn't understand code "+code+"\n")
      sys.exit(1)
  return ret

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("--trainfile", "-i", nargs='?', type=argparse.FileType('r'), default=sys.stdin, help="input train file")
    parser.add_argument("--testfile", "-t", nargs='?', type=argparse.FileType('r'), default=None, help="input test file")
    parser.add_argument("--outfile", "-o", nargs='?', type=argparse.FileType('w'), default=sys.stdout, help="output file")
    parser.add_argument('--subsample', type=float, default=1.0,
                        help='subsample this fraction of total')
    args = parser.parse_args()
    trainfile = prepfile(args.trainfile, 'r')
    if args.testfile is not None:
        testfile = prepfile(args.testfile, 'r')
    else:
        testfile = None
    outfile = prepfile(args.outfile, 'w')

    # Create feature extractor (you may want to modify this)
    fe = FeatureExtractor()

    # Read in training data
    train = DictReader(trainfile, delimiter='\t')

    # Split off dev section
    dev_train = []
    dev_test = []
    full_train = []

    for ii in train:
        if args.subsample < 1.0 and int(ii['id']) % 100 > 100 * args.subsample:
            continue
        feat = fe.features(ii['text'])
        #print feat
        if int(ii['id']) % 5 == 0:
            dev_test.append((feat, ii['cat']))
        else:
            dev_train.append((feat, ii['cat']))
        full_train.append((feat, ii['cat']))
    #print dev_test[:50]

    #print collections.Counter(dev_test[0][0].values()).most_common()[-1][0]
    #print collections.Counter(dev_test[0][0].values())


    # Train a classifier
    sys.stderr.write("Training classifier ...\n")
    classifier = nltk.classify.NaiveBayesClassifier.train(dev_train)
    #classifier.show_most_informative_features(15)
    #print dev_train[:10]



    right = 0
    total = len(dev_test)
    for ii in dev_test:
        prediction = classifier.classify(ii[0])
        if prediction == ii[1]:
            right += 1
    sys.stderr.write("Accuracy on dev: %f\n" % (float(right) / float(total)))

    if testfile is None:
        sys.stderr.write("No test file passed; stopping.\n")
    else:
        # Retrain on all data
        classifier = nltk.classify.NaiveBayesClassifier.train(dev_train + dev_test)

        # Read in test section
        test = {}
        for ii in DictReader(testfile, delimiter='\t'):
            test[ii['id']] = classifier.classify(fe.features(ii['text']))

        # Write predictions
        o = DictWriter(outfile, ['id', 'pred'])
        o.writeheader()
        for ii in sorted(test):
            o.writerow({'id': ii, 'pred': test[ii]})
