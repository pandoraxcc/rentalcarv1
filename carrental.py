import emoji
class shop:
    def __init__(self, rentalCars):
        self.carsForRent = rentalCars
    def giveCar(self,requestedCar):
        if requestedCar in self.carsForRent:
            self.carsForRent.remove(requestedCar)
            print(emoji.emojize(':white_check_mark: :red_car: :white_check_mark:'))
            print("Thank you for renting! You car will be prepared shortly.")
        else:
            print(emoji.emojize(':x: :red_car: :x:'))
            print("Sorry the car is unavailable")
    def takeCar(self,returnedCar):
        self.carsForRent.append(returnedCar)
        print("Thank you for returning the car!")
    def showCar(self):
        print("This is the list of the available cars:")
        for car in self.carsForRent:
            print(car)
class customer:
    def rentCar(self):
        self.car = input("You choosed to rent the car. Please enter the name of the car you would like to rent: ")
        return self.car
        print("Great! The car is booked.")
    def returnCar(self):
        self.car = input("You choosed to return the car. Enter the name of the car you would like to return: ")
        return self.car

#Initializing the objects
rentalShop = shop(["BMW", "Subaru", "Porsche"])
currentCustomer = customer()
while 1:
    print("\nThis is the list of available options:")
    print("Select 1 to see the list of the cars in stock")
    print("Select 2 to rent the car")
    print("Select 3 to return the car")
    print("Select 4 to close the app")
    userSelects = int(input())
    if userSelects == 1:
      rentalShop.showCar()
    elif userSelects == 2:
      requestedCar = currentCustomer.rentCar()
      rentalShop.giveCar(requestedCar)
    elif userSelects == 3:
      returnedCar = currentCustomer.returnCar()
      rentalShop.takeCar(returnedCar)
    elif userSelects == 4:
      quit()




