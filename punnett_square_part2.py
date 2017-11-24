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

# Given two strings of two characters representing the gentics of a trait, returns a list of possible offsprings each represented as a two character string.

# "BB", "BB" -> ["BB", "BB", "BB", "BB"]
# "BB", "Bb" -> ["BB", "Bb", "BB", "Bb"]

def possible_offsprings_reps(father, mother):
    assert father in reps
    assert mother in reps
    offsprings = []
    for allele_father in father:
        for allele_mother in mother:
            offsprings += [allele_father+allele_mother]
    return offsprings



    
    
    



## Try it out:

## Tests

#TEST1: possible_offsprings_reps("BB", "BB") == ["BB", "BB", "BB", "BB"]
#OUTPUT: True


#TEST2: pors = possible_offsprings_reps("BB", "Bb")
#TEST2: len(pors) == 4
#OUTPUT: True

#TEST2: set(pors) == {"BB", "Bb"}
#OUTPUT: True


# can you come up with other good test cases?








## Try it out:

## Prove the tests are not sufficient !!!

## can you think of any possible test outputs that could screw up the second test?

## fill the output string, let it pass the two tests

## bad_pors = ["", "", "", ""] 

## len(bad_pors) == 4
#OUTPUT: True

## set(bad_pors) == {"BB", "Bb"}
#OUTPUT: True









## Note1: [] is an empty list, {} is an empty dictionary



## Note2: for loop:

## syntax for for loop

## for <condition>:
##     <statement>

## There can also be multiple statements

## for <condition>:
##     <statement1>
##     <statement2>
##     <statement3>
##     ...







#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# Challenge
# can you think of a robust test (tests) for pors
## Hint: you can use a list comprehension
#### len([rep for rep in pors if rep == STRING]) == INTEGER
