# codeAssessment2

### Instructions
Answer each question inside of the individual question files. Each file has the question paste inside of it.

### Problem 1
Ask the user to enter a number. 
Using the provided list of numbers, use a for loop to iterate the array and print out all the values that are smaller than the user input and print out all the values that are larger than the number entered by the user.

```
# Start with this List
list_of_many_numbers = [12, 24, 1, 34, 10, 2, 7]
```
Example Input/Output if the user enters the number 9:
```
The User entered 9
1  2  7 are smaller than 9
12  24  34  10 are larger than 9
```
### Problem 2
Prompt the user with the message, ‘Is it better to be rude or kind to People?’ 
Keeping prompting the user to enter an answer until they enter the word kind. 
Each time they enter something other than kind, print the message, ‘That’s not the answer I had hoped to hear. Try again.’ and prompt the user again.
Once the user enters kind, print, ’Now that’s what I wanted to hear!’ and exit the program.

### Problem 3
Given 2 lists of claim numbers, write the code to merge the 2 lists provided to produce a new list by alternating values between the 2 lists. Once the merge has been completed, print the new list of claim numbers (DO NOT just print the array variable!)
```
# Start with these lists
list_of_claim_nums_1 = [2, 4, 6, 8, 10]
list_of_claim_nums_2 = [1, 3, 5, 7, 9]
```
Example Output:
```
The newly created list contains:     2  1  4  3  6  5  8  7  10  9
```
### Problem 4
Write a program that allows users to compare words by their length. Implement a function called chk_strings that accepts 2 strings entered by the user and compares them by length
The function should return true if the first string parameter has more characters (i.e. longer) than the second string passed into the function, otherwise, the function should return false.
DO NOT print the result in the function, print the result using the return value provided by the function. 

Example Input/Output:
```
Enter the first string: BIRD
Enter the second string: COW

BIRD is longer than COW
```
### Problem 5
Create a SportsTeam Class for tracking sports teams. The class should have the properties team_name_p, team_city, and team_ranking_p.
The class should have a method to change a Team’s ranking. 
The class should implement the ```__str__``` method so that when an instance of the SportsTeam is printed it will output a string containing the team name, team city, and team rank (use f strings to format the output).
Your program should create a SportsTeam instance with an initial ranking of 2.
Print out the class.
Your program should change the ranking of the team to 8 using only the class method.
Print out the class (should use your ```__str__``` method).


Example Output:
```
The Grizzlies are from Memphis and are 2 in the standings.
# Update the rating from 2 to 8 from your code
The Grizzlies are from Memphis and are 8 in the standings.
```
### Problem 6
Create a class called ClubMember 
Each club member has a name and a role  
Create ClubMember instances for the following people:
```
Alfred - Club President
Troy - Club Vice President
Albert - Club Secretary
Bob - Club Treasurer
```
Add each member instance to a new club_members list that you create.
Write the code needed to loop through the club member list and print the current number of members in the list, then the member’s name and club role, one per line using f strings.

Example Output:
```
There are currently 4 club members in the list!

Club President: Alfred
Club Vice President: Troy
Club Secretary: Albert
Club Treasurer: Bob
```

