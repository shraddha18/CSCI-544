import sys
from fst import FST
from fsmutils import composewords,trace

kFRENCH_TRANS = {0: "zero", 1: "un", 2: "deux", 3: "trois", 4:
                 "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit",
                 9: "neuf", 10: "dix", 11: "onze", 12: "douze", 13:
                 "treize", 14: "quatorze", 15: "quinze", 16: "seize",
                 20: "vingt", 30: "trente", 40: "quarante", 50:
                 "cinquante", 60: "soixante", 100: "cent"}

kFRENCH_AND = 'et'

def prepare_input(integer):
    assert isinstance(integer, int) and integer < 1000 and integer >= 0, \
      "Integer out of bounds"
    return list("%03i" % integer)

def french_count():
    f = FST('french')

    f.add_state('start')
    f.add_state('ones')
    f.add_state('hundred')
    f.add_state('single')
    f.add_state('tens')
    f.add_state('twenties')
    f.add_state('thirties')
    f.add_state('forties')
    f.add_state('fifties')
    f.add_state('sixties')
    f.add_state('seventies')
    f.add_state('eighties')
    f.add_state('nineties')
    f.add_state('hundred1')
    f.add_state('hundred2')
    f.add_state('fin')

    f.initial_state = 'start'
    f.set_final('fin')

    for ii in xrange(10):

        f.add_arc('start', 'start', [str(ii)], [kFRENCH_TRANS[ii]])

        if ii==0:
            f.add_arc('start', 'hundred', [str(ii)], ())
            f.add_arc('hundred', 'ones', [str(ii)], ())
            f.add_arc('ones', 'fin', [str(ii)], [kFRENCH_TRANS[ii]])
            f.add_arc('tens', 'fin', [str(ii)], [kFRENCH_TRANS[10]])
            f.add_arc('twenties', 'fin', [str(ii)], ())
            f.add_arc('thirties', 'fin', [str(ii)], ())
            f.add_arc('forties', 'fin', [str(ii)], ())
            f.add_arc('fifties', 'fin', [str(ii)], ())
            f.add_arc('sixties', 'fin', [str(ii)], ())
            f.add_arc('seventies', 'fin', [str(ii)], [kFRENCH_TRANS[10]])
            f.add_arc('eighties', 'fin', [str(ii)], ())
            f.add_arc('nineties', 'fin', [str(ii)], [kFRENCH_TRANS[10]])
            f.add_arc('hundred1', 'hundred2', [str(ii)], ())
            f.add_arc('hundred2', 'fin', [str(ii)], ())


        if ii==1:
            f.add_arc('start', 'hundred1', [str(ii)], [kFRENCH_TRANS[100]])
            f.add_arc('hundred', 'tens', [str(ii)], ())
            f.add_arc('ones', 'fin', [str(ii)], [kFRENCH_TRANS[1]])
            f.add_arc('tens', 'fin', [str(ii)], [kFRENCH_TRANS[11]])
            f.add_arc('twenties', 'fin', [str(ii)], [kFRENCH_AND + " " + kFRENCH_TRANS[1]])
            f.add_arc('thirties', 'fin', [str(ii)], [kFRENCH_AND + " " + kFRENCH_TRANS[1]])
            f.add_arc('forties', 'fin', [str(ii)], [kFRENCH_AND + " " + kFRENCH_TRANS[1]])
            f.add_arc('fifties', 'fin', [str(ii)], [kFRENCH_AND + " " + kFRENCH_TRANS[1]])
            f.add_arc('sixties', 'fin', [str(ii)], [kFRENCH_AND + " " + kFRENCH_TRANS[1]])
            f.add_arc('seventies', 'fin', [str(ii)], [kFRENCH_AND + " " + kFRENCH_TRANS[11]])
            f.add_arc('eighties', 'fin', [str(ii)], [kFRENCH_TRANS[1]])
            f.add_arc('nineties', 'fin', [str(ii)], [kFRENCH_TRANS[11]])
            f.add_arc('hundred1', 'tens', [str(ii)],())
            f.add_arc('hundred2','fin', [str(ii)], [kFRENCH_TRANS[1]])



        if ii==2:
            f.add_arc('ones', 'fin', [str(ii)], [kFRENCH_TRANS[2]])
            f.add_arc('tens', 'fin', [str(ii)], [kFRENCH_TRANS[12]])
            f.add_arc('hundred', 'twenties', [str(ii)], [kFRENCH_TRANS[20]])
            f.add_arc('twenties', 'fin', [str(ii)], [kFRENCH_TRANS[2]])
            f.add_arc('thirties', 'fin', [str(ii)], [kFRENCH_TRANS[2]])
            f.add_arc('forties', 'fin', [str(ii)], [kFRENCH_TRANS[2]])
            f.add_arc('fifties', 'fin', [str(ii)], [kFRENCH_TRANS[2]])
            f.add_arc('sixties', 'fin', [str(ii)], [kFRENCH_TRANS[2]])
            f.add_arc('seventies', 'fin', [str(ii)], [kFRENCH_TRANS[12]])
            f.add_arc('eighties', 'fin', [str(ii)], [kFRENCH_TRANS[2]])
            f.add_arc('nineties', 'fin', [str(ii)], [kFRENCH_TRANS[12]])
            f.add_arc('start', 'hundred1', [str(ii)], [kFRENCH_TRANS[2] + " " + kFRENCH_TRANS[100]])
            f.add_arc('hundred1', 'twenties', [str(ii)],[kFRENCH_TRANS[20]])
            f.add_arc('hundred2','fin', [str(ii)], [kFRENCH_TRANS[2]])

        if ii==3:
            f.add_arc('ones', 'fin', [str(ii)], [kFRENCH_TRANS[3]])
            f.add_arc('tens', 'fin', '3', [kFRENCH_TRANS[13]])
            f.add_arc('hundred', 'thirties', [str(ii)], [kFRENCH_TRANS[30]])
            f.add_arc('twenties', 'fin', [str(ii)], [kFRENCH_TRANS[3]])
            f.add_arc('thirties', 'fin', [str(ii)], [kFRENCH_TRANS[3]])
            f.add_arc('forties', 'fin', [str(ii)], [kFRENCH_TRANS[3]])
            f.add_arc('fifties', 'fin', [str(ii)], [kFRENCH_TRANS[3]])
            f.add_arc('sixties', 'fin', [str(ii)], [kFRENCH_TRANS[3]])
            f.add_arc('seventies', 'fin', [str(ii)], [kFRENCH_TRANS[13]])
            f.add_arc('eighties', 'fin', [str(ii)], [kFRENCH_TRANS[3]])
            f.add_arc('nineties', 'fin', [str(ii)], [kFRENCH_TRANS[13]])
            f.add_arc('hundred2','fin', [str(ii)], [kFRENCH_TRANS[3]])
            f.add_arc('hundred1', 'thirties', [str(ii)],[kFRENCH_TRANS[30]])
            f.add_arc('start', 'hundred1', [str(ii)], [kFRENCH_TRANS[3] + " " + kFRENCH_TRANS[100]])

        if ii==4:
            f.add_arc('ones', 'fin', [str(ii)], [kFRENCH_TRANS[4]])
            f.add_arc('tens', 'fin', '4', [kFRENCH_TRANS[14]])
            f.add_arc('twenties', 'fin', [str(ii)], [kFRENCH_TRANS[4]])
            f.add_arc('thirties', 'fin', [str(ii)], [kFRENCH_TRANS[4]])
            f.add_arc('hundred', 'forties', [str(ii)], [kFRENCH_TRANS[40]])
            f.add_arc('forties', 'fin', [str(ii)], [kFRENCH_TRANS[4]])
            f.add_arc('fifties', 'fin', [str(ii)], [kFRENCH_TRANS[4]])
            f.add_arc('sixties', 'fin', [str(ii)], [kFRENCH_TRANS[4]])
            f.add_arc('seventies', 'fin', [str(ii)], [kFRENCH_TRANS[14]])
            f.add_arc('eighties', 'fin', [str(ii)], [kFRENCH_TRANS[4]])
            f.add_arc('nineties', 'fin', [str(ii)], [kFRENCH_TRANS[14]])
            f.add_arc('hundred2','fin', [str(ii)], [kFRENCH_TRANS[4]])
            f.add_arc('hundred1', 'forties', [str(ii)],[kFRENCH_TRANS[40]])
            f.add_arc('start', 'hundred1', [str(ii)], [kFRENCH_TRANS[4] + " " + kFRENCH_TRANS[100]])

        if ii==5:
            f.add_arc('ones', 'fin', [str(ii)], [kFRENCH_TRANS[5]])
            f.add_arc('tens', 'fin', '5', [kFRENCH_TRANS[15]])
            f.add_arc('twenties', 'fin', [str(ii)], [kFRENCH_TRANS[5]])
            f.add_arc('thirties', 'fin', [str(ii)], [kFRENCH_TRANS[5]])
            f.add_arc('forties', 'fin', [str(ii)], [kFRENCH_TRANS[5]])
            f.add_arc('hundred', 'fifties', [str(ii)], [kFRENCH_TRANS[50]])
            f.add_arc('fifties', 'fin', [str(ii)], [kFRENCH_TRANS[5]])
            f.add_arc('sixties', 'fin', [str(ii)], [kFRENCH_TRANS[5]])
            f.add_arc('seventies', 'fin', [str(ii)], [kFRENCH_TRANS[15]])
            f.add_arc('eighties', 'fin', [str(ii)], [kFRENCH_TRANS[5]])
            f.add_arc('nineties', 'fin', [str(ii)], [kFRENCH_TRANS[15]])
            f.add_arc('hundred2','fin', [str(ii)], [kFRENCH_TRANS[5]])
            f.add_arc('hundred1', 'fifties', [str(ii)],[kFRENCH_TRANS[50]])
            f.add_arc('start', 'hundred1', [str(ii)], [kFRENCH_TRANS[5] + " " + kFRENCH_TRANS[100]])

        if ii==6:
            f.add_arc('ones', 'fin', [str(ii)], [kFRENCH_TRANS[6]])
            f.add_arc('tens', 'fin', '6', [kFRENCH_TRANS[16]])
            f.add_arc('twenties', 'fin', [str(ii)], [kFRENCH_TRANS[6]])
            f.add_arc('thirties', 'fin', [str(ii)], [kFRENCH_TRANS[6]])
            f.add_arc('forties', 'fin', [str(ii)], [kFRENCH_TRANS[6]])
            f.add_arc('fifties', 'fin', [str(ii)], [kFRENCH_TRANS[6]])
            f.add_arc('hundred', 'sixties', [str(ii)], [kFRENCH_TRANS[60]])
            f.add_arc('sixties', 'fin', [str(ii)], [kFRENCH_TRANS[6]])
            f.add_arc('seventies', 'fin', [str(ii)], [kFRENCH_TRANS[16]])
            f.add_arc('eighties', 'fin', [str(ii)], [kFRENCH_TRANS[6]])
            f.add_arc('nineties', 'fin', [str(ii)], [kFRENCH_TRANS[16]])
            f.add_arc('hundred2','fin', [str(ii)], [kFRENCH_TRANS[6]])
            f.add_arc('hundred1', 'sixties', [str(ii)],[kFRENCH_TRANS[60]])
            f.add_arc('start', 'hundred1', [str(ii)], [kFRENCH_TRANS[6] + " " + kFRENCH_TRANS[100]])


        if ii==7:
            f.add_arc('ones', 'fin', [str(ii)], [kFRENCH_TRANS[7]])
            f.add_arc('tens', 'fin', '7', [kFRENCH_TRANS[10] + " " + kFRENCH_TRANS[7]])
            f.add_arc('twenties', 'fin', [str(ii)], [kFRENCH_TRANS[7]])
            f.add_arc('thirties', 'fin', [str(ii)], [kFRENCH_TRANS[7]])
            f.add_arc('forties', 'fin', [str(ii)], [kFRENCH_TRANS[7]])
            f.add_arc('fifties', 'fin', [str(ii)], [kFRENCH_TRANS[7]])
            f.add_arc('sixties', 'fin', [str(ii)], [kFRENCH_TRANS[7]])
            f.add_arc('hundred', 'seventies', [str(ii)], [kFRENCH_TRANS[60]])
            f.add_arc('seventies', 'fin', [str(ii)], [kFRENCH_TRANS[10] + " " + kFRENCH_TRANS[7]])
            f.add_arc('eighties', 'fin', [str(ii)], [kFRENCH_TRANS[7]])
            f.add_arc('nineties', 'fin', [str(ii)], [kFRENCH_TRANS[10] + " " + kFRENCH_TRANS[7]])
            f.add_arc('hundred2','fin', [str(ii)], [kFRENCH_TRANS[7]])
            f.add_arc('hundred1', 'seventies', [str(ii)],[kFRENCH_TRANS[60]])
            f.add_arc('start', 'hundred1', [str(ii)], [kFRENCH_TRANS[7] + " " + kFRENCH_TRANS[100]])

        if ii==8:
            f.add_arc('ones', 'fin', [str(ii)], [kFRENCH_TRANS[8]])
            f.add_arc('tens', 'fin', '8', [kFRENCH_TRANS[10] + " " + kFRENCH_TRANS[8]])
            f.add_arc('twenties', 'fin', [str(ii)], [kFRENCH_TRANS[8]])
            f.add_arc('thirties', 'fin', [str(ii)], [kFRENCH_TRANS[8]])
            f.add_arc('forties', 'fin', [str(ii)], [kFRENCH_TRANS[8]])
            f.add_arc('fifties', 'fin', [str(ii)], [kFRENCH_TRANS[8]])
            f.add_arc('sixties', 'fin', [str(ii)], [kFRENCH_TRANS[8]])
            f.add_arc('seventies', 'fin', [str(ii)], [kFRENCH_TRANS[10]+ " " + kFRENCH_TRANS[8]])
            f.add_arc('hundred', 'eighties', [str(ii)], [kFRENCH_TRANS[4] + " " + kFRENCH_TRANS[20]])
            f.add_arc('eighties', 'fin', [str(ii)], [kFRENCH_TRANS[8]])
            f.add_arc('nineties', 'fin', [str(ii)], [kFRENCH_TRANS[10]+ " " + kFRENCH_TRANS[8]])
            f.add_arc('hundred2','fin', [str(ii)], [kFRENCH_TRANS[8]])
            f.add_arc('hundred1', 'eighties', [str(ii)],[kFRENCH_TRANS[4] + " " + kFRENCH_TRANS[20]])
            f.add_arc('start', 'hundred1', [str(ii)], [kFRENCH_TRANS[8] + " " + kFRENCH_TRANS[100]])


        if ii==9:
            f.add_arc('ones', 'fin', [str(ii)], [kFRENCH_TRANS[9]])
            f.add_arc('tens', 'fin', '9', [kFRENCH_TRANS[10] + " " + kFRENCH_TRANS[9]])
            f.add_arc('twenties', 'fin', [str(ii)], [kFRENCH_TRANS[9]])
            f.add_arc('thirties', 'fin', [str(ii)], [kFRENCH_TRANS[9]])
            f.add_arc('forties', 'fin', [str(ii)], [kFRENCH_TRANS[9]])
            f.add_arc('fifties', 'fin', [str(ii)], [kFRENCH_TRANS[9]])
            f.add_arc('sixties', 'fin', [str(ii)], [kFRENCH_TRANS[9]])
            f.add_arc('seventies', 'fin', [str(ii)], [kFRENCH_TRANS[10]+ " " + kFRENCH_TRANS[9]])
            f.add_arc('eighties', 'fin', [str(ii)], [kFRENCH_TRANS[9]])
            f.add_arc('hundred', 'nineties', [str(ii)], [kFRENCH_TRANS[4] + " " + kFRENCH_TRANS[20]])
            f.add_arc('nineties', 'fin', [str(ii)], [kFRENCH_TRANS[10]+ " " + kFRENCH_TRANS[9]])
            f.add_arc('hundred2','fin', [str(ii)], [kFRENCH_TRANS[9]])
            f.add_arc('hundred1', 'nineties', [str(ii)],[kFRENCH_TRANS[4] + " " + kFRENCH_TRANS[20]])
            f.add_arc('start', 'hundred1', [str(ii)], [kFRENCH_TRANS[9] + " " + kFRENCH_TRANS[100]])

    return f

if __name__ == '__main__':
    string_input = raw_input()
    user_input = int(string_input)
    f = french_count()
    #print trace(f,user_input)
    if string_input:
        print user_input, '-->',
        print " ".join(f.transduce(prepare_input(user_input)))
