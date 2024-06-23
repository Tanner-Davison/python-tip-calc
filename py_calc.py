print('Welcome to the tip calculator!')

total_bill = float(input("What is the total bill?\n"))

tip_percent = float(input("Percentage to tip? ex) 25, 15, 10, ect..\n")) / 100

num_people = int(input("how many people would like to split the bill?\n"))

if num_people != 0: 
    bill_per_person = total_bill / num_people
    final_bill = bill_per_person * (1 + tip_percent)
    print(f"Each person should pay: \n${final_bill:.2f}")
else:
    final_bill = total_bill * (1 + tip_percent)
    print(f"The total bill is: ${final_bill:.2f}")