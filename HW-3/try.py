import itertools
import nltk
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords

# def bigram_word_feats(words, score_fn=BigramAssocMeasures.chi_sq, n=200):
#     bigram_finder = BigramCollocationFinder.from_words(words)
#     print bigram_finder
#     bigrams = bigram_finder.nbest(score_fn, n)
#     print len(bigrams)
#     for each in bigrams:
#         print each[0] + " "+ each[1]
#         each2 = (SnowballStemmer('english').stem(each[0]),SnowballStemmer('english').stem(each[1]))
#
#         print each2[0] + " "+ each2[1]
#
#     number = "THISSSSS"
#     print number.isupper()


    #return dict([(ngram, 1) for ngram in itertools.chain(words, bigrams)])

#evaluate_classifier(bigram_word_feats)

#print bigram_word_feats(nltk.word_tokenize('This is going to be crazy but worth it'))



import string
stop_words = set(stopwords.words('english'))
text = "Feed'st thy light'st flame with self-substantial fuel,"
text = text.translate(None, string.punctuation)
print stop_words
print len(text), text
remove_stopword = text
for i in stop_words:
    remove_stopword = remove_stopword.replace(i,'')
print remove_stopword
# import nltk
#
# #nltk.download()
# def posAns(text):
#     #text2 = nltk.word_tokenize(text)
#     ans = nltk.pos_tag([text])
#     tup =ans
#     print ans[0][1]
#
#
# posAns('as')

        # tfidf = TfidfVectorizer(tokenizer=kTOKENIZER.tokenize(text), stop_words='english')
        # tfs = tfidf.fit_transform(d.values())
        # response = tfidf.transform([kTOKENIZER.tokenize(text)])
        # for col in response.nonzero()[1]:
			# d[col] = response[0, col]