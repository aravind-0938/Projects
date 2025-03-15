#Find the net salary
salary=int(input("Enter your salary: "))

if salary<15000 and salary>10000:
    tax_percetage=5/100
    print("Your tax percentage is: ",tax_percetage)
elif salary<20000 and salary>15000:
    tax_percetage=10/1000   
    print("Your tax percentage is: ",tax_percetage)
elif salary<30000 and salary>20000:
    tax_percetage=15/100
    print("Your tax percentage is: ",tax_percetage)
elif salary>30000:
    tax_percetage=18/100
    print("Your tax percentage is: ",tax_percetage)
else:
    print("Your salary is below 10000")
    quit()

tax_amount=salary*tax_percetage
net_salary=salary-tax_amount
print("Your tax amaount is",tax_amount)
print("Your net amount is",net_salary)