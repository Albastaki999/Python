stopRecursion = False
def sayHello():
    global stopRecursion
    print("hello")
    if stopRecursion == True:
        return
    stopRecursion = True
    sayHello()

# def sayGoodMorning():
#     print("Good Morning")
    
sayHello()