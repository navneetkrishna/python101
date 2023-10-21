# write a program to check BMI
# BMI = weight/(height^2)

# The BMI should be classified as follows
# Underweight : BMI under or equal to 18.5
# Normal : BMI between 18.5 and 25(Not including 18.5 but including 25)
# Overweight : BMI between 25 and 30(Not including 25 but including 30)
# Obese : BMI greater than 30

import math

height = float(input("Enter your height(in meters): "))
weight = float(input("Enter your weight(in kgs): "))

BMI = float(weight / math.pow(height, 2)).__round__(2)
# print(height ** 2) will square the height value

if BMI < 18.5:
    print(f"Your BMI is {BMI}\nYou are Underweight :(")

elif 18.5 < BMI <= 25:
    print(f"Your BMI is {BMI}\nYou are Normal :)")

elif 25 < BMI <= 30:
    print(f"Your BMI is {BMI}\nYou are Overweight :(")

else:
    print(f"Your BMI is {BMI}\nYou are Obese : (")
