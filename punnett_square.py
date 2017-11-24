######################################### PART ONE

# Given a string of two characters representing the gentics of a trait, returns a string describing the trait.

# "BB" -> "Brown Eye"
# "Bb" -> "Brown Eye"
# "bb" -> "Blue Eye"

reps = ["BB", "Bb", "bb"]

def rep2trait(rep):
    # it is always good practice to write some test cases even before actually writing code
    """
        >>> rep2trait("BB") == "Brown Eye"
        True
        >>> rep2trait("Bb") == "Brown Eye"
        True
        >>> rep2trait("bb") == "Blue Eye"
        True
    """
    # consider the function of these two assertions
    # try modify these assertions to see how these two assertions restrict the input
    ## ex: what will happen when we change reps to ["BB", "bb"]
    # in practice, it is often helpful to restrict the range of allowed input > _ <
    assert len(rep) == 2
    assert rep in reps
    # Is there any other way to rewrite this if-else statement?
    # Why are we justified in only performing one equality check?
    if (rep == "bb"):
       return "Blue Eye"
    else:
       return "Brown Eye"




######################################### PART TWO

# Given two strings of two characters representing the gentics of a trait, returns a list of possible offsprings each represented as a two character string.

# "BB", "BB" -> ["BB", "BB", "BB", "BB"]
# "BB", "Bb" -> ["BB", "Bb", "BB", "Bb"]

def possible_offsprings_reps(father, mother):
    assert father in reps
    assert mother in reps
    # can you come up with other good test cases?
    # how are we justified in the second test (the tests for pors)?
    # can you think of any possible test outputs that could screw up the second test?
    # can you think of a robust test (tests) for pors
    ## Hint: you can use a list comprehension
    #### len([rep for rep in pors if rep == STRING]) == INTEGER
    """
        >>> possible_offsprings_reps("BB", "BB") == ["BB", "BB", "BB", "BB"]
        True
        >>> pors = possible_offsprings_reps("BB", "Bb")
        >>> len(pors) == 4
        True
        >>> set(pors) == {"BB", "Bb"}
        True
    """
    ## can you guess what the values of allele_father and allele_mother are in each iteration based on the output list for the second test?
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
