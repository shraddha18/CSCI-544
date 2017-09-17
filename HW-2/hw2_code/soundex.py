from fst import FST
import string, sys
from fsmutils import composechars, trace

def letters_to_numbers():
    """
    Returns an FST that converts letters to numbers as specified by
    the soundex algorithm
    """
    #print type(user_input)
    # Let's define our first FST
    f1 = FST('soundex-generate')

    # Indicate that '1' is the initial state
    f1.add_state('start')
    f1.add_state('next')
    f1.add_state('s1')
    f1.add_state('1')
    f1.add_state('2')
    f1.add_state('3')
    f1.add_state('4')
    f1.add_state('5')
    f1.add_state('6')
    f1.add_state('7')
    f1.initial_state = 'start'

    # Set all the final states
    f1.set_final('next')

    group1 = ['b','f','p','v']
    group2 = ['c','g','j','k','q','s','x','z']
    group3 = ['d','t']
    group4 = ['l']
    group5 = ['m','n']
    group6 = ['r']
    vowels = ['a','e','i','o','u','h','w','y']


    # Add the rest of the arcs
    for letter in string.ascii_lowercase + string.ascii_uppercase :
        f1.add_arc('start', 's1', (letter), (letter))

        if letter in group1:
            #_ = f1.add_arc('start','s1',(letter),(letter))
            _ = f1.add_arc('s1','1',(letter),'1')
            _ = f1.add_arc('1','1',(letter),())
            _ = f1.add_arc('7','1',(letter),'1')
            _ = f1.add_arc('2','1',(letter),'1')
            _ = f1.add_arc('3','1',(letter),'1')
            _ = f1.add_arc('4','1',(letter),'1')
            _ = f1.add_arc('5','1',(letter),'1')
            _ = f1.add_arc('6','1',(letter),'1')
        if letter in group2:
            #_ = f1.add_arc('start','s1',(letter),(letter))
            _ = f1.add_arc('s1','2',(letter),'2')
            _ = f1.add_arc('2','2',(letter),())
            _ = f1.add_arc('7','2',(letter),'2')
            _ = f1.add_arc('1','2',(letter),'2')
            _ = f1.add_arc('3','2',(letter),'2')
            _ = f1.add_arc('4','2',(letter),'2')
            _ = f1.add_arc('5','2',(letter),'2')
            _ = f1.add_arc('6','2',(letter),'2')
        if letter in group3:
            #_ = f1.add_arc('start','s1',(letter),(letter))
            _ = f1.add_arc('s1','3',(letter),'3')
            _ = f1.add_arc('3','3',(letter),())
            _ = f1.add_arc('7','3',(letter),'3')
            _ = f1.add_arc('1','3',(letter),'3')
            _ = f1.add_arc('2','3',(letter),'3')
            _ = f1.add_arc('4','3',(letter),'3')
            _ = f1.add_arc('5','3',(letter),'3')
            _ =f1.add_arc('6','3',(letter),'3')
        if letter in group4:
            #_ = f1.add_arc('start','s1',(letter),(letter))
            _ = f1.add_arc('s1','4',(letter),'4')
            _ = f1.add_arc('4','4',(letter),())
            _ = f1.add_arc('7','4',(letter),'4')
            _ = f1.add_arc('1','4',(letter),'4')
            _ = f1.add_arc('2','4',(letter),'4')
            _ = f1.add_arc('3','4',(letter),'4')
            _ = f1.add_arc('5','4',(letter),'4')
            _ =f1.add_arc('6','4',(letter),'4')
        if letter in group5:
            #_ = f1.add_arc('start','s1',(letter),(letter))
            _ = f1.add_arc('s1','5',(letter),'5')
            _ = f1.add_arc('5','5',(letter),())
            _ = f1.add_arc('7','5',(letter),'5')
            _ = f1.add_arc('1','5',(letter),'5')
            _ = f1.add_arc('2','5',(letter),'5')
            _ = f1.add_arc('3','5',(letter),'5')
            _ = f1.add_arc('4','5',(letter),'5')
            _ = f1.add_arc('6','5',(letter),'5')
        if letter in group6:
            #_ = f1.add_arc('start','s1',(letter),(letter))
            _ = f1.add_arc('s1','6',(letter),'6')
            _ = f1.add_arc('6','6',(letter),())
            _ = f1.add_arc('7','6',(letter),'6')
            _ = f1.add_arc('1','6',(letter),'6')
            _ = f1.add_arc('2','6',(letter),'6')
            _ = f1.add_arc('3','6',(letter),'6')
            _ = f1.add_arc('4','6',(letter),'6')
            _ = f1.add_arc('5','6',(letter),'6')
        if letter in vowels:
           # _ = f1.add_arc('start','s1',(letter),(letter))
            _ = f1.add_arc('s1','7',(letter),())
            _ = f1.add_arc('1','7',(letter),())
            _ = f1.add_arc('2','7',(letter),())
            _ = f1.add_arc('3','7',(letter),())
            _ = f1.add_arc('4','7',(letter),())
            _ = f1.add_arc('5','7',(letter),())
            _ = f1.add_arc('6','7',(letter),())
            _ = f1.add_arc('7','7',(letter),())

    f1.add_arc('1', 'next', (), ())
    f1.add_arc('2', 'next', (), ())
    f1.add_arc('3', 'next', (), ())
    f1.add_arc('4', 'next', (), ())
    f1.add_arc('5', 'next', (), ())
    f1.add_arc('6', 'next', (), ())
    f1.add_arc('7', 'next', (), ())
    return f1

    # The stub code above converts all letters except the first into '0'.
    # How can you change it to do the right conversion?

def truncate_to_three_digits():
    """
    Create an FST that will truncate a soundex string to three digits
    """

    # Ok so now let's do the second FST, the one that will truncate
    # the number of digits to 3
    f2 = FST('soundex-truncate')

    # Indicate initial and final states
    f2.add_state('1')
    f2.add_state('2')
    f2.add_state('3')
    f2.add_state('4')
    f2.add_state('5')
    f2.initial_state = '1'
    f2.set_final('2')
    f2.set_final('3')
    f2.set_final('4')
    f2.set_final('5')

    # Add the arcs
    for letter in string.letters:
        _ = f2.add_arc('1', '2', (letter), (letter))

    for n in range(10):
        _ = f2.add_arc('1', '3', (str(n)), (str(n)))#if string doesnt start with a letter
        _ = f2.add_arc('2', '3', (str(n)), (str(n)))
        _ = f2.add_arc('3', '4', (str(n)), (str(n)))
        _ = f2.add_arc('4', '5', (str(n)), (str(n)))
        _ = f2.add_arc('5', '5', (str(n)), ())


    return f2

    # The above stub code doesn't do any truncating at all -- it passes letter and number input through
    # what changes would make it truncate digits to 3?

def add_zero_padding():
    # Now, the third fst - the zero-padding fst
    f3 = FST('soundex-padzero')

    f3.add_state('1')
    f3.add_state('1a')
    f3.add_state('1b')
    f3.add_state('2a')
    f3.add_state('2b')
    f3.initial_state = '1'
    f3.set_final('2b')

    for letter in string.letters:
        f3.add_arc('1', '1a', (letter), (letter))

    f3.add_arc('1', '1b', (), ('0'))
    f3.add_arc('1a', '1b', (), ('0'))
    f3.add_arc('1b', '2a', (), ('0'))
    f3.add_arc('2a', '2b', (), ('0'))

    for number in xrange(10):
        f3.add_arc('1', '1b', (str(number)), (str(number)))
        f3.add_arc('1a', '1b', (str(number)), (str(number)))
        f3.add_arc('1b', '2a', (str(number)), (str(number)))
        f3.add_arc('2a', '2b', (str(number)), (str(number)))
    


    return f3

    # The above code adds zeroes but doesn't have any padding logic. Add some!

if __name__ == '__main__':
    user_input = raw_input().strip()
    f1 = letters_to_numbers()
    #print trace(f1,user_input)
    f2 = truncate_to_three_digits()
    #print trace(f2,user_input)
    f3 = add_zero_padding()
    #print trace(f3,user_input)

    if user_input:
        print("%s -> %s" % (user_input, composechars(tuple(user_input), f1, f2, f3)))
