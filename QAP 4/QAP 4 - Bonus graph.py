# Program to chart the monthly sales inputed from Jan. to Dec.
# Written on: Nov. 19, 2023
# Written by: Rodney Stead

# Imported libraries
import matplotlib.pyplot as plt

# Empty sales list
sales = []

# Month Sale entry
MonthsLst = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
for month in MonthsLst:
    while True:
        try:
            sale = float(input(f"Enter the total amount of sales for {month}: "))
            if sale == "":
                print("Sales cannot be blank. Please re-enter.")
            else:
                break
        except ValueError:
            print("Must be a number, please re-enter.")
 
    sales.append(sale)

# Graph plot the go is green circles, can also use r for red, b for blue, etc.
# Can also use -- for dashed lines, - for solid lines, etc.
# (Never thought id enjoy graphing)
plt.plot(MonthsLst, sales, "go")

# Graph labels
plt.title("Total Sales per Month")
plt.xlabel("Months")
plt.ylabel("Sales ($)")

plt.show()