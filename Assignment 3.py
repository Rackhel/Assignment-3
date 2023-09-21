#Number 1
print("This is Number 1.\n")
try:
    Hour = int(input("Enter the hours: "))
except:
    print("Input data is wrong.")
else:
        try:
            Rate = float(input("Enter the rate: "))
        except:
             print("Error. Please enter a numeric input.")
        else:
             if (Hour <= 40):
                  Salary = Hour * Rate
                  print("This is the Salary,",Salary,".")
             elif (Hour > 40):
                  Salary = (40 * Rate) + (((Hour - 40) * Rate) * 1.5)
                  print("This is the Salary,",Salary,".")
print("\n")

#Number 2
print("This is Number 2.\n")
try:
    score = float(input("Enter the score: "))
    if 0 <= score <= 100:
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        print("Grade: ",grade)   
    else:
        print("Error, Please enter numeric input between 0 and 100.")       
except ValueError:
    print("Error, Please enter numeric input between 0 and 100.")
print("\n")

#Number 3
print("This is Number 3.\n")
total = 0
count = 0
while True:
    try:
        Number = input("Enter a number: ")
        if Number.lower() == "done":
            break
        numba = float(Number)
        total += numba
        count += 1
    except ValueError:
        print("Invalid input. Enter a number.")

if count > 0:
    average = total / count
else:
    average = 0

print("\n")
print("Sum: ",total)
print("Count: ",count)
print("Average: ",average)
print("\n")

print("End of Program")
print("Rackhel, 202312229")


    
