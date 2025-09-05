class Car: 
    def __init__(self, manufacturer, model, year, mileage, price):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price = price 

    def Paint(self, new_color):
        self.exterior_color = new_color 
        print(f"The {self.model} was painted {new_color}!")

    def Repair(self, part, replacement):
        if part.lower() in ["engine", "transmission", "drivetrain"]:
            setattr(self, part.lower(), replacement) 
            print(f"{self.model}'s {part} was replaced with {replacement}.") 
        else:
            print(f"Sorry, {part} cannot be repaired here.") 

    def Reupholster(self, new_color):
        self.interior_color = new_color 
        print(f"{self.model}'s interior was reupholstered to {new_color}!") 

    def Drive(self, miles):
        self.mileage += miles
        print(f"{self.model} was driven {miles} miles. Total mileage is now {self.mileage}.")

    def Modify_Price(self, amount):
        if amount < 1: 
            discount = self.price * amount
            new_price = self.price - discount 
            print(f"Discount applied. New price is ${new_price}.")
            confirm = input("Confirm new price? (yes/no): ")
            if confirm.lower() == "yes":
                self.price = new_price 
                print(f"Price updated to ${self.price}.")
            else: 
                print("Price update canceled.")
        else: 
            self.price = amount 
            print(f"Price set to ${self.price}.") 

class Seller:
    def __init__(self, name, rating): 
        self.name = name 
        self.rating = rating 
        self.inventory = [] 

    def Buy(self, car):
        if car not in self.inventory: 
            self.inventory.append(car)
            print(f"{self.name} bought {car.manufacturer} {car.model}.")
        else: 
            print(f"{car.model} is already in inventory.")

    def Sell(self, car):
        if car in self.inventory:
            self.inventory.remove(car)
            print(f"{self.name} sold {car.manufacturer} {car.model}.")
        else:
            print(f"{car.model} is not in inventory.")

import csv 

cars = []

with open("cars.csv", newline = "") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        mileage = float(row["mileage"]) if row["mileage"] else 0
        price = float(row["price"]) if row["price"] else 0
        car = Car(row["manufacturer"], row["model"], int(row["year"]), int(mileage), price)
        cars.append(car)

print("Cars loaded from CSV:", len(cars))
print("First car:", cars[0].manufacturer, cars[0].model, cars[0].year) 

if __name__ == "__main__":
    seller1 = Seller("Person A's used cars", 4.7)
    seller1.Buy(cars[0])
    seller1.Buy(cars[1])
    print(f"{seller1.name} has {len(seller1.inventory)} cars in inventory.")
    seller1.Sell(cars[0])
    print(f"{seller1.name} now has {len(seller1.inventory)} cars.")