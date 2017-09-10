import unittest
from limerick import LimerickDetector

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.ld = LimerickDetector()

    def test_apos(self):
        s = []

        try: self.assertEqual(self.ld.apostrophe_tokenize("He can't do this"), True)
        except: s.append(1)
        try: self.assertEqual(self.ld.apostrophe_tokenize("She doesn't care this ain't her work"), True)
        except: s.append(2)

        print '\nNumber of failed rhyme tests:', str(len(s))
        if len(s)!=0: print 'Failed rhyme tests:', ','.join([str(x) for x in s])

    def test_rhyme(self):
        s = []

        try: self.assertEqual(self.ld.rhymes("dog", "bog"), True)
        except: s.append(1)
        try: self.assertEqual(self.ld.rhymes("eleven", "seven"), True)
        except: s.append(2)
        try: self.assertEqual(self.ld.rhymes("nine", "wine"), True)
        except: s.append(3)
        try: self.assertEqual(self.ld.rhymes("dine", "fine"), True)
        except: s.append(4)
        try: self.assertEqual(self.ld.rhymes("wine", "mine"), True)
        except: s.append(5)
        try: self.assertEqual(self.ld.rhymes("dock", "sock"), True)
        except: s.append(6)
        try: self.assertEqual(self.ld.rhymes("weigh", "fey"), True)
        except: s.append(7)
        try: self.assertEqual(self.ld.rhymes("tree", "debris"), True)
        except: s.append(8)
        try: self.assertEqual(self.ld.rhymes("niece", "peace"), True)
        except: s.append(9)
        try: self.assertEqual(self.ld.rhymes("read", "need"), True)
        except: s.append(10)
        try: self.assertEqual(self.ld.rhymes("dog", "cat"), False)
        except: s.append(11)
        try: self.assertEqual(self.ld.rhymes("bagel", "sail"), False)
        except: s.append(12)
        try: self.assertEqual(self.ld.rhymes("wine", "rind"), False)
        except: s.append(13)
        try: self.assertEqual(self.ld.rhymes("failure", "savior"), False)
        except: s.append(14)
        try: self.assertEqual(self.ld.rhymes("cup", "duck"), False)
        except: s.append(15)
        try: self.assertEqual(self.ld.rhymes("confession", "regression"), True)
        except: s.append(16)

        print '\nNumber of failed rhyme tests:', str(len(s))
        if len(s)!=0: print 'Failed rhyme tests:', ','.join([str(x) for x in s])

        """
        try: self.assertEqual(self.ld.rhymes("a", "ah"), False)
        except: s.append(1)
        try: self.assertEqual(self.ld.rhymes("eh", "meh"), False)
        except: s.append(2)
        try: self.assertEqual(self.ld.rhymes("play", "slay"), True)
        except: s.append(3)
        try: self.assertEqual(self.ld.rhymes("along", "prolong"), True)
        except: s.append(4)
        try: self.assertEqual(self.ld.rhymes("infinity", "affinity"), False)
        except: s.append(5)
        try: self.assertEqual(self.ld.rhymes("clarify", "verify"), True)
        except: s.append(6)
        try: self.assertEqual(self.ld.rhymes("anatomical", "Economical"), False)
        except: s.append(7)
        try: self.assertEqual(self.ld.rhymes("impair", "footwear"), False)
        except: s.append(8)
        try: self.assertEqual(self.ld.rhymes("along", "wrong"), True)
        except: s.append(9)

        print '\nNumber of failed rhyme tests:', str(len(s))
        if len(s)!=0: print 'Failed rhyme tests:', ','.join([str(x) for x in s])
        """

    def test_syllables(self):
        s = []
        try: self.assertEqual(self.ld.num_syllables("dog"), 1)
        except: s.append(1)
        try: self.assertEqual(self.ld.num_syllables("asdf"), 1)
        except: s.append(2)
        try: self.assertEqual(self.ld.num_syllables("letter"), 2)
        except: s.append(3)
        try: self.assertEqual(self.ld.num_syllables("washington"), 3)
        except: s.append(4)
        try: self.assertEqual(self.ld.num_syllables("dock"), 1)
        except: s.append(5)
        try: self.assertEqual(self.ld.num_syllables("dangle"), 2)
        except: s.append(6)
        try: self.assertEqual(self.ld.num_syllables("thrive"), 1)
        except: s.append(7)
        try: self.assertEqual(self.ld.num_syllables("fly"), 1)
        except: s.append(8)
        try: self.assertEqual(self.ld.num_syllables("placate"), 2)
        except: s.append(9)
        try: self.assertEqual(self.ld.num_syllables("renege"), 2)
        except: s.append(10)
        try: self.assertEqual(self.ld.num_syllables("reluctant"), 3)
        except: s.append(11)

        print '\nNumber of failed syllables tests:', str(len(s))
        if len(s)!=0: print 'Failed syllables tests:', ','.join([str(x) for x in s])

    def test_examples(self):

        a = """
a woman whose friends called a prude
on a lark when bathing all nude
saw a man come along
and unless we are wrong
you expected this line to be lewd
        """

        b = """while it's true all i've done is delay
in defense of myself i must say
today's payoff is great
while the workers all wait
"""

        c = """
this thing is supposed to rhyme
but I simply don't got the time
who cares if i miss,
nobody will read this
i'll end this here poem potato
"""

        d = """There was a young man named Wyatt
whose voice was exceedingly quiet
And then one day
it faded away"""

        e = """An exceedingly fat friend of mine,
When asked at what hour he'd dine,
Replied, "At eleven,     
At three, five, and seven,
And eight and a quarter past nine"""

        f = """A limerick fan from Australia
regarded his work as a failure:
his verses were fine
until the fourth line"""

        g = """There was a young lady one fall
Who wore a newspaper dress to a ball.
The dress caught fire
And burned her entire
Front page, sporting section and all."""

        h = "dog\ndog\ndog\ndog\ndog"

        i = """potato potato potato swine
potato potato mine
potato swig
potato rig
potato potato potato wine."""

        j = """potato potato swine swine
potato potato mine
potato swig
potato rig
potato potato wine wine."""

        k = """potato potato mice
potato potato ice
potato
potato
potato potato rice"""

        l = """potato potato mice
potato potato ice
potato
potato"""

        m = """potato potato mouse nick
potato potato tick
potato trick
potato pick
potato potato wick wick
        """

        n = """potato potato potato hand
potato potato demand
potato pride
potato snide

potato potato potato grand        """

        o = """rat rat rat rat pound
rat lives in the ground
rat is a big ass man
rat lives in a frying pan
rat pat mat bat cat     sat mound
        """

        s = []

        try: self.assertEqual(self.ld.is_limerick(a), True)
        except: s.append('a')
        try: self.assertEqual(self.ld.is_limerick(b), False)
        except: s.append('b')
        try: self.assertEqual(self.ld.is_limerick(c), False)
        except: s.append('c')
        try: self.assertEqual(self.ld.is_limerick(d), False)
        except: s.append('d')
        try: self.assertEqual(self.ld.is_limerick(f), False)
        except: s.append('f')
        try: self.assertEqual(self.ld.is_limerick(e), True)
        except: s.append('e')
        try: self.assertEqual(self.ld.is_limerick(g), True)
        except: s.append('g')
        try: self.assertEqual(self.ld.is_limerick(h), False)
        except: s.append('h')
        try: self.assertEqual(self.ld.is_limerick(i), False)
        except: s.append('i')
        try: self.assertEqual(self.ld.is_limerick(j), True)
        except: s.append('j')
        try: self.assertEqual(self.ld.is_limerick(k), False)
        except: s.append('k')
        try: self.assertEqual(self.ld.is_limerick(l), False)
        except: s.append('l')
        try: self.assertEqual(self.ld.is_limerick(m), False)
        except: s.append('m')
        try: self.assertEqual(self.ld.is_limerick(n), True)
        except: s.append('n')
        try: self.assertEqual(self.ld.is_limerick(o), False)
        except: s.append('o')

        print 'Number of failed limerick tests:', str(len(s))
        if len(s)!=0: print 'Failed limerick tests:', ','.join(s)

if __name__ == '__main__':
    unittest.main()
