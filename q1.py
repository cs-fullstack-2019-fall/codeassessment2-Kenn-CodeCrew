# ### Problem 1
# Ask the user to enter a number. 

userInputInteger = int(input("Enter a number: "))
# Using the provided list of numbers, use a for loop to iterate the array and print out all the values that are smaller than the user input and print out all the values that are larger than the number entered by the user.

# ```
# # Start with this List
list_of_many_numbers = [12, 24, 1, 34, 10, 2, 7]

listOfSmallerNumbers = []
listOfLargerNumbers = []

for eachNumberInArray in list_of_many_numbers:
    if userInputInteger > eachNumberInArray:
        listOfSmallerNumbers.append(eachNumberInArray)
    elif userInputInteger < eachNumberInArray:
        listOfLargerNumbers.append(eachNumberInArray)

# print(listOfSmallerNumbers)
# print(listOfLargerNumbers)

print("The User entered " + str(userInputInteger))

stringOfSmallerNumbers = ""
for eachNumber in listOfSmallerNumbers:
    stringOfSmallerNumbers += str(eachNumber) + "  "
print(stringOfSmallerNumbers + "are smaller than " + str(userInputInteger))


stringOfLargerNumbers = ""
for eachNumber in listOfLargerNumbers:
    stringOfLargerNumbers += str(eachNumber) + "  "
print(stringOfLargerNumbers + "are larger than " + str(userInputInteger))

# ```
# Example Input/Output if the user enters the number 9:
# ```
# The User entered 9
# 1  2  7 are smaller than 9
# 12  24  34  10 are larger than 9
# ```

