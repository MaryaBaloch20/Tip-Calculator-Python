print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

#Converting Tip (int) to percentage
tip_perc = tip / 100

#Calculating Total tip (According to the bill)
total_tip = bill * tip_perc

#Calculating total bill to be paid
total_bill = bill + total_tip

#Calculating bill per person
bill_per_person = total_bill / people

#Calculating Final amount (round off) to be paid by each person
final_amount = round(bill_per_person, 2)

#Printing the Answer
print(f"Each person should pay {final_amount}")