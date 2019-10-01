# ### Problem 4
# Write a program that allows users to compare words by their length. Implement a function called chk_strings that accepts 2 strings entered by the user and compares them by length
# The function should return true if the first string parameter has more characters (i.e. longer) than the second string passed into the function, otherwise, the function should return false.
# DO NOT print the result in the function, print the result using the return value provided by the function. 

def chk_strings(string1, string2):
    if len(string1) > len(string2):
        return True
    else:
        return False

userInput1 = input("Enter the first string: ")
userInput2 = input("Enter the second string: ")

answerFromFunction = chk_strings(userInput1, userInput2)

if(answerFromFunction):
    print("\n" + userInput1 + " is longer than " + userInput2)
else:
    print("\n" + userInput2 + " is longer than " + userInput1)

# Example Input/Output:
# ```
# Enter the first string: BIRD
# Enter the second string: COW

# BIRD is longer than COW
# ```
