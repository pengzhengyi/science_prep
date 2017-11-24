######################################### PART ONE

reps = ["BB", "Bb", "bb"]

def rep2trait(rep):
    assert len(rep) == 2
    assert rep in reps
    if (rep == "bb"):
       return "Blue Eye"
    else:
       return "Brown Eye"


######################################### PART TWO

def possible_offsprings_reps(father, mother):
    assert father in reps
    assert mother in reps
    offsprings = []
    for allele_father in father:
        for allele_mother in mother:
            offsprings += [allele_father+allele_mother]
    return offsprings




######################################### PART FUN

# Pretty printing for a punnett square
## print as a 3*3 two dimensional array
def punnett_square(father, mother):
    ## play it around > _ <
    #    >>> punnett_square("BB", "BB")
    #    \   B   B
    #    B   BB  BB
    #    B   BB  BB
    #    >>> punnett_square("BB", "bb")
    #    \   b   b
    #    B   Bb  Bb
    #    B   Bb  Bb
    #    >>> punnett_square("Bb", "bb")
    #    \   b   b
    #    B   Bb  Bb
    #    b   bb  bb
    # why do we not need assertion checks here?
    pors = possible_offsprings_reps(father, mother)
    # is the order correct?
    square = [['\\', mother[0], mother[1]],
              [father[0], pors[0], pors[1]],
              [father[1], pors[2], pors[3]]]
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in square]))


######################################### PART EXTRA FUN

# Have you thought of how to print all punnett_squares?
## Let's use a nested loop
## why don't we use a list comprehension
## can you think of ways to use list comprehension
def all_punnett_squares():
    for father in reps:
        for mother in reps:
            punnett_square(father, mother)
            print() #Blank line after a square
