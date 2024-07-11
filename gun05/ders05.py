def myFunc1():
    x = "jane"
    def myFunc2():
        nonlocal x
        x = "hello"

    myFunc2()
    return x
print(myFunc1())
