# **Car Inventory System**

## **Purpose**

This project creates a simple car inventory management system for used car dealers. It allows car dealers to track their cars and perform common dealership tasks like painting cars, fixing parts, and managing their inventory. 

## **How It Works**

The program reads car data from a CSV file and creates a virtual car lot where dealers can buy and sell cars.   
---

## **Car Class**

### **What Information Each Car Stores:**

* manufacturer \- Who made the car   
* model \- the type of car   
* year \- When the car was made  
* mileage \- How many miles the car has been driven  
* price \- How much the car costs

### **What Cars Can Do:**

Paint(new\_color) \- Changes the car's exterior color

* Takes a color name and changes the car's paint  
* Prints a message saying the car was painted

Repair(part, replacement) \- Fixes car parts

* Can replace engine, transmission, or drivetrain  
* If you try to repair something else, it says "can't repair that here"  
* Uses setattr() to update the car's parts (this is set attributes function used)

Reupholster(new\_color) \- Changes the interior color 

* Changes the seat/interior color  
* Prints a confirmation message

Drive(miles) \- Adds miles to the car (used some math here)

* Increases the car's mileage by the amount driven  
* Shows the new total mileage

Modify\_Price(amount) \- Changes the car's price

* If amount is less than 1: treats it as a discount percentage  
* If amount is 1 or more: sets that as the new price  
* For discounts, asks you to confirm before changing 

---

## **Seller Class**

### **What Information Each Seller Has:**

* name \- The seller's or dealership's name  
* rating \- Customer rating (like 4.5 stars)  
* inventory \- List of cars the seller owns (starts empty)

### **What Sellers Can Do:**

Buy(car) \- Adds a car to their inventory (using the append()) 

* Checks if car is already owned  
* If not owned, adds it to their car list  
* Prints a message about buying the car

Sell(car) \- Removes a car from their inventory (used the remove()) 

* Checks if they actually own the car  
* If they own it, it removes it from their list  
* Prints a message about selling the car

---

## **Reading the CSV File**

### **The Import Statement**

python

import csv

This tells Python we want to use tools for reading spreadsheet files. I downloaded it from the dataset from kaggle. 

### **Opening and Reading the File**

python  
with open("cars.csv", newline="") as csvfile:  
    reader \= csv.DictReader(csvfile)  
    for row in reader:

 

What this does:

* with open() \- Opens the CSV file safely (automatically closes when done)  
* csv.DictReader() \- Reads the file like a dictionary where column names are keys  
* for row in reader \- Goes through each row (car) in the spreadsheet one by one

### **Creating Cars from CSV Data**

python  
mileage \= float(row\["mileage"\]) if row\["mileage"\] else 0  
price \= float(row\["price"\]) if row\["mileage"\] else 0  
car \= Car(row\["manufacturer"\], row\["model"\], int(row\["year"\]), int(mileage), price)

cars.append(car)

What this does:

* Converts text from csv into numbers Python can use  
* float() makes decimal numbers, int() makes whole numbers  
* Creates a new Car object with the csv data  
* Adds the car to our main list of all cars

---

## **The Main Program Section**

python

if \_\_name\_\_ \== "\_\_main\_\_":

What this means: "Only run this code if someone runs this file directly"  
This section creates a test seller and demonstrates:

1. Creating a seller named "Person A's used cars" with 4.7 rating  
2. Having the seller buy two cars from our CSV data  
3. Showing how many cars they have  
4. Having them sell one car  
5. Showing the updated inventory count

---

## **Files Needed**

* Your Python code file (.py)  
* cars.csv \- The car data downloaded from the assignment  
* This README file

## **How to Run**

1. Make sure the CSV file is in the same folder as your Python file  
2. Run your Python file  
3. The program will load all cars from the CSV and run the demo

---

## **What the Program Demonstrates**

* Loading real car data from a file  
* Creating car and seller objects  
* Using object methods to modify cars and manage inventory  
* Basic inventory management for a used car dealership

**AI assistance used:** 

- Used Claude AI for:   
  - Code review and suggestions for missing attributes   
  - Thorough explanation of assignment and criteria grading rubric  
  - Help understanding object oriented concepts   
  - Help understanding modules more better, a lot of explanations asked   
  - Debugging advice for class methods   
- Used Github Copilot for:   
  - Terminal explanations   
  - Incorrect files and directory structure  
  - Alignment of if, else and print  
  - Helped with float and int updates   
  - Explanation of setattr   
  - CSV explanations   
  - Error explanations   
- Used ChatGPT for:  
  - Review on class and modules   
  - How to get started on “class Car:” part (refresher)  
  - Correction on if/else and recommendation on code   
  - Understanding what is being asked of in the assignment   
  - Moral support (because still unable to code without help and format) 