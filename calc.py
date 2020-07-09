total = 0
cost_car=0
​
gas = {
    "new york": "2.08"
}
parking = {
    "new york city": "1000"
}
​
insurance = {
    "16-17": "6100",
    "18-19": "4334",
    "20-24": "2350",
    "25-29": "1608",
    "30-39": "1449",
    "40-49": "1396",
    "50-59": "1296",
    "60-69": "1325",
    "70-79": "1556",
    "80+": "2847",
}

def cost_of_car():
   global total
   global cost_car
   budget =  int(input("What is your budget? \n"))
   cost = int(input("How much does the car you want to buy cost? \n"))
   
   if cost > budget:
    print("You cannot afford this car!")
   else:
    print("Excellent choice! You can afford this car ")
    #total += int(cost)
    cost_car += int(cost)
#cost_of_car()
​
def monthly_cost_gas():
    global total
    location = input("What state do you live in? \n").lower()
    miles = int(input("How many miles do you expect to drive each month? \n"))
    cost_of_gas = int(miles)/25 * float(gas[location]) 
​
    total+= cost_of_gas
​
    return "In " + location.capitalize() + " the average cost of gas (per gallon) is $" + gas[location].upper() + ". If you drive " + str(miles) + " per month you can expect to pay $" + str(cost_of_gas) + " monthly"
​
#print(monthly_cost_gas())
​
def monthly_cost_parking():
    global total
    cost_parking = 1000
    location = input("What city do you live in? ").lower()
    parking_lot = input("Will you require a space in a parking lot? ").lower()
    if parking_lot == "yes":
        total += cost_parking
        return "Monthly parking in the city can cost about $" + str(cost_parking) +"\n"
​
    else:
        return "If you're able to park in your own garage, for example, you will be saving a lot! Parking was the largest cost of driving in the U.S. in 2017."

#print(monthly_cost_parking())
​
def insurance_cost():
    global total
    print("The estimated of insurance is based on the National average for age groups")
    age = input("Please enter your age group as followed: \n 16-17 \n 18-19 \n 25-29 \n 30-39 \n 40-49 \n 50-59 \n 60-69 \n 70-79 \n 80+ \n")
    total += int(insurance[age])
    return "The cost of your insurance premium monthly is estimated to be $" + str(round(int(insurance[age])/12))
​
def call_all(): 
    cost_of_car()
    print(monthly_cost_gas())
    print(monthly_cost_parking())
    print(insurance_cost())
    print("The cost of your car would be: $" + str(cost_car) + " \n The total cost for owning your car per month would be around: $" + str(total))
​
call_all()

