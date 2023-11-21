#decorator is a way that a function that takes a function as input and modify it

def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce   #adds announce decorator to this function (hello)
def hello():
    print("Hello, world!")

hello()