"""Name: Stella Plahitko
   File name: M03_Lab.py
   Description: This app prompts the user to input attributes of a car. Those attributes will then be listed."""
#Defines the Vehicle class
class Vehicle:
    def __init__(self, vehicle_type):
    #Initializes a vehicle object with the attribute 'vehicle_type'
        self.vehicle_type = vehicle_type

#Defines Automobile as a subclass of the Vehicle class
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof, vehicle_type):
    #Initializes a vehicle object with the attributes 'self', 'year', 'make', 'model', 'doors',
    #and 'roof'. The vehicle type attribute is inherited from the parent class 'Vehicle'
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    def print_stats(self):
    #Prints a string listing each attribute of an Automobile Object
        print("Vehicle Stats:","\n","Vehicle Type:",self.vehicle_type,"\n","Vehicle Year:",self.year,"\n"
              ,"Vehicle Make:",self.make,"\n","Vehicle Model:",self.model
              ,"\n","Number of Doors:",self.doors,"\n","Roof Type:",self.roof)
    
#Prompts user for vehicle year, make, and model. Vehicle type is automatically set to 'car'
vehicle_type = "car"
year = str(input("Vehicle Year: "))
make = str(input("Vehicle Make: "))
model = str(input("Vehicle Model: "))

#Initalizes values for door_type and doors
door_type = ["2", "4"]
doors = 0
#Loop prompts users to input a value for doors until either a 2 or 4 in entered
while doors not in door_type:
    doors = str(input("Does the vehicle have 2 or 4 doors? Enter either '2' or '4': "))

#Initializes values for roof_type and roof
roof_type = ["sun", "solid"]
roof = "none"
#Loop prompts users to input a value for doors until either 'solid' or 'sun' is entered 
while roof not in roof_type:
    roof = str(input("Does the vehicle have a solid roof or sun roof? Enter either 'solid' or 'sun' in all lowercase: "))

#Uses input from prompts to create an object of the Automobile subclass and run the print_stats method
automobile = Automobile(year, make, model, doors, roof, vehicle_type)
Automobile.print_stats(automobile)