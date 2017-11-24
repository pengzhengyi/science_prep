######################################### PART ONE

# Given a string of two characters representing the gentics of a trait, returns a string describing the trait.

# "BB" -> "Brown Eye"
# "Bb" -> "Brown Eye"
# "bb" -> "Blue Eye"

reps = ["BB", "Bb", "bb"]

def rep2trait(rep):
    assert len(rep) == 2
    assert rep in reps
    if (rep == "bb"):
       return "Blue Eye"
    else:
       return "Brown Eye"


# Try It Out
## READ Note2, Note4

## Tests:

## Process the code above . (Copy them to repl_it and hit run)

## Copy or type the first line (THE PART AFTER "#TEST1 ") into repl_it (the right section), hit Enter
#### see if the output matches exactly the second line (THE PART AFTER "#OUTPUT: ")

#TEST1: rep2trait("BB") == "Brown Eye"
#OUTPUT: True

## Try the same for the other two tests

#TEST2: rep2trait("Bb") == "Brown Eye"
#OUTPUT: True

#TEST3: rep2trait("bb") == "Blue Eye"
#OUTPUT: True





# Try it out
## READ Note3

## Copy or type "rep2trait("BBB")" into repl_it (the right section), press enter.
## What did you get?

## remove the line "assert len(rep) == 2" in left section of repl_it. Process the code(hit Enter), 
## do the previous step again, what did you get?




# Try it out
## READ Note5

# Why are we justified in only performing one equality check?

# Can you rewrite the if else statement to be a if else if statement
# fill the strings (eg: "" -> "BB")

# def rep2trait(rep):
#     assert len(rep) == 2
#     assert rep in reps
#     if (rep == ""):
#        return ""
#     elif (rep == ""):
#         return ""
#     else:
#        return ""

# Try the previous tests. Do your function still pass the tests?

















# Note1: the line starting with # is a comment. The computer will ignore them. Comments can improve
## the readability of program.



# Note2: tests are designed to check whether a function works (produce the desired output when provided
## a given input). It is always good practice to write some test cases even before actually writing code



# Note3: Assertion is a statement reflecting our expectation in a certain state of program. For example,
## we assume the length of rep is 2 at the first line of function since we expect the input to be a string
## of length two.
## The syntax for assert is: 
## assert <condition>
## the statement could either evaluates to true or to false. In the first case, assert succeeds and in the
## second case, the assert fails and an assertion error occurs. 



# Note4: Equality check is "==". It will determine whether the right hand side equals the left hand side
## for example, "1 == 1" would evaluates to True.  "1 == 2" would evaluates to False. 




# Note5: If statement
## Syntax for If Else statement:

## if (<condition>):
##    <statement>
## else:
##    <statement>

## Syntax for If Else-If statement:
## if (<condition>):
##    <statement>
## elif (<condition>):
##    <statement>
## else:
##    <statement>





