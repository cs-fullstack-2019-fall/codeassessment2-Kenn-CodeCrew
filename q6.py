# ### Problem 6
# Create a class called ClubMember
# Each club member has a name and a role
class ClubMember:
    def __init__(self, name, role):
        self.name = name
        self.role = role
# Create ClubMember instances for the following people:
# ```
# Alfred - Club President
# Troy - Club Vice President
# Albert - Club Secretary
# Bob - Club Treasurer
# ```

member1 = ClubMember("Alfred", "Club President")
member2 = ClubMember("Troy", "Club Vice President")
member3 = ClubMember("Albert", "Club Secretary")
member4 = ClubMember("Bob", "Club Treasurer")
# Add each member instance to a new club_members list that you create.
club_members = [member1, member2, member3, member4]
# Write the code needed to loop through the club member list and print the current number of members in the list, then the member’s name and club role, one per line using f strings.

print("There are currently " + str(len(club_members)) + " club members in the list!\n")

for eachElement in club_members:
    print(f"{eachElement.role}: {eachElement.name}")
# Example Output:
# ```
# There are currently 4 club members in the list!

# Club President: Alfred
# Club Vice President: Troy
# Club Secretary: Albert
# Club Treasurer: Bob
# ```

