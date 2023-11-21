#program to boot passenger on a flight
class Flight():     
    def __init__(self, capacity):   #takes an argument that represent the capacity
        self.capacity = capacity    #adds an attribute named capacity
        self.passengers = []        #adds an attribute nemed passengers

    def add_passenger(self, name):  #method that add a passenger to attribute passengers list  
        if not self.openSeats():    #if openSeats is 0
            return False
        self.passengers.append(name)    #append a passenger to list
        return True

    def openSeats(self):                                #the len method returns the length of a list
        return self.capacity - len(self.passengers)     #returns the capacity attribute minus the lenght of passengers list


flight = Flight(3)  #creates an object with capacity 3

people = ["Harry" , "Ron", "Hermione", "Ginny"]

for person in people:
    if flight.add_passenger(person):    #if the method add_passenger adds a passenger and returns true
        print(f"Added {person} to flight successfully.")
    else:   
        print(f"No available seats for {person}")
    