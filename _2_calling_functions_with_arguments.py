# == INSTRUCTIONS ==
#
# These challenges are a bit trickier and, in some cases, will require a few
# lines of code. If you start to get a little stuck, take a step back and make
# a plan by breaking the overall task down into small steps.

# == EXERCISES ==

# Purpose: checks if a string starts with the letter a
# Example:
#   Call:    starts_with_the_letter_a("apple")
#   Returns: True
#   Call:    starts_with_the_letter_a("Apple")
#   Returns: True
#   Call:    starts_with_the_letter_a("Rock")
#   Returns: False
def starts_with_the_letter_a(string):
    # your code goes here (delete the pass below)
    string1 = string[0].lower()
    if string1 == "a":
        return True
    else: 
        return False

print(starts_with_the_letter_a("apple"))


# Purpose: checks if a string ends with the letter a
# Example:
#   Call:    ends_with_the_letter_a("Java")
#   Returns: True
#   Call:    ends_with_the_letter_a("JAVA")
#   Returns: True
#   Call:    ends_with_the_letter_a("Python")
#   Returns: False
def ends_with_the_letter_a(string):
    # your code goes here (delete the pass below)
    string1 = string[-1].lower()
    if string1 == "a":
        return True
    else:
        return False

# Purpose: checks if a string contains the word hello
# Example:
#   Call:    contains_hello("hello world")
#   Returns: True
#   Call:    contains_hello("HELLO WORLD")
#   Returns: True
#   Call:    contains_hello("world")
#   Returns: False
def contains_hello(string):
    # your code goes here (delete the pass below)
    string1 = string.lower()
    if "hello" in string1:
        return True
    else:
        return False
        
print(contains_hello("hello world"))


# Purpose: replaces the word hello with the word goodbye
# Note: you don't need to worry about matching 'Hello' or 'HELLO' here
#       lowercase only is fine.
# Example:
#   Call:    substitute_hello_with_goodbye("hello folks")
#   Returns: "goodbye folks"
#   Call:    substitute_hello_with_goodbye("Hello folks")
#   Returns: "Hello folks"
def substitute_hello_with_goodbye(string):
    # your code goes here (delete the pass below)
    if "hello" in string:
        string1 = string.replace("hello", "goodbye")
        return string1
    else:
        return string

print(substitute_hello_with_goodbye("hello folks"))



# Purpose: removes the letter x from a string
# Example:
#   Call:    remove_x("xoxo")
#   Returns: "oo"
#   Call:    remove_x("OXO")
#   Returns: "OO"
def remove_x(string):
    # your code goes here (delete the pass below)
    string1 = string.replace("x" , "")
    string2 = string1.replace("X" , "")
    return string2

print(remove_x("xoxo"))


# Purpose: returns the first half of a string
# Example:
#   Call:    first_half("coding")
#   Returns: "cod"
# Note: you can assume the string will always have an even number of characters
def first_half(string):
    # your code goes here (delete the pass below)
    half_string = string[0:len(string)//2]
    return half_string

print(first_half("coding"))


# Purpose: returns the second half of a string
# Example:
#   Call:    second_half("coding")
#   Returns: "ing"
# Note: you can assume the string will always have an even number of characters
def second_half(string):
    # your code goes here (delete the pass below)
    end_half = string[len(string)//2:]
    return end_half

print(second_half("coding"))


# Congrats, you're done with this file. Move on to the next one.
