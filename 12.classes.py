class Point():
    #its a method that called every time that I create a point
    def __init__(self, input1, input2 ): #the self argument represent the object name, the arguments inpu1 and input2 represent the values of the object
        self.x = input1 #add the property x that stores the input1 argument
        self.y = input2 #add the property y that stores the input2 argument

p = Point(8, 10) #create an object 

print(p.x)
print(p.y)

