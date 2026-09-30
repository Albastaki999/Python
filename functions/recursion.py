stopRecursion = False

def sayHello():
    global stopRecursion
    # This condition below is responsible for stopping the recursion
    # Base case
    if stopRecursion == True:
        return
    
    # General Case
    print("hello")
    stopRecursion = True
    sayHello()

# def sayGoodMorning():
#     print("Good Morning")
    
sayHello()