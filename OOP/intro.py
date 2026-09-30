class Student:
    # Attributes, properties
    firstName = ""
    lastName = ""
    rollNo = 1
    course = "CSE"
    hasPaidFees = True
    
    # necessary
    # Constructor (used for building the object)
    def __init__(self, firstName, lastName, rollNo, course, hasPaidFees):
        self.firstName = firstName
        self.lastName = lastName
        self.rollNo = rollNo
        self.course = course
        self.hasPaidFees = hasPaidFees
    
    def getFullName(self):
        return self.firstName + " " + self.lastName

# Object
rashid = Student("Rashid", "Mahmood", 1, "CSE", True)
shahid = Student("Shahid", "Ali",2, "ECE", False)

print(rashid.firstName)
print(rashid.lastName)
print(rashid.rollNo)
print(rashid.course)
print(rashid.hasPaidFees)
print("\n")
print(shahid.firstName)
print(shahid.lastName)
print(shahid.rollNo)
print(shahid.course)
print(shahid.hasPaidFees)



# shahid.course = "IT"
# print(shahid.course)

# Printing FullName
# print(shahid.firstName + " " + shahid.lastName)
print(shahid.getFullName())
print(rashid.getFullName())

nums = [1, 2, 3, 4]
# Function written inside a class is called a method
nums.append()
