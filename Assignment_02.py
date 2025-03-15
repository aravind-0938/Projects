#Accept the following data from user and calculate the percentage
total_days=int(input("Enter the total number of working days: "))
worked_days=int(input("Enter the total number of worked days: "))

percentage=(worked_days/total_days)*100
print(percentage,"%")

if percentage<75:
    print("Your not eligible for attending exams")
else:
    print("Your eligible for attending exams")