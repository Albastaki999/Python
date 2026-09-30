nums = [1, 2, 3, 4, 5, 6]
# sum1 = 0

# for i in nums:
#     sum1 = sum1 + i

# print(sum1)

nums2 = [192,1, 32, 32, 56]
# sum2 = 0

# for i in nums2:
#     sum2 = sum2 + i

# print(sum2)

# Message is a parameter
# def greet(message):
#     print(message)
#     return 10

# Calling the function
# "hello" is an argument
# greet("hello")
# greet("Hi")
# greet("Hey")
# greet(1234)

# returnedValue = greet("hello")
# print(returnedValue)
# printValue = print("hello", "hi", "how are you")
# print(printValue)

# print(sum([1, 2, 3, 4]))

def calculateSum(numbers):
    sum = 0
    
    for num in numbers:
        sum += num
    return sum

print(calculateSum(nums))
print(calculateSum(nums2))