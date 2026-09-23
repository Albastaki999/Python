# a = 30
# b = 20

# # Indentation
# if a < b:
#     print("a is less than b")
# else:
#     print("a is not less than b")
    
# print("If condition completed")


# age = int(input("Please enter your age:"))

# if age >= 18:
#     print("You are eligible to vote")
# else:
#     print("Not eligible")
    
# print("Eligibility check completed")

# Nested

age = int(input("Enter your age:"))
hasVoterIdCard = input("Do you have a Voter ID Card (Y/N):")

if age >= 18:
    if hasVoterIdCard == 'Y':
        print("Eligible to Vote")
    else:
        print("No Voter ID Card")
else:
    print("Below 18")
