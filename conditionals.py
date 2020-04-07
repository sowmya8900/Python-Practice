height= float(input("Enter your height in meters"))
weight= float(input("Enter your weight in kgs"))

bmi= float(weight/(height**2))
print("Your BMI=", round(bmi, 2))

if(bmi<=18.5): print("Underweight")
elif(bmi>18.5 and bmi<=24.9): print("Normal Weight")
elif(bmi>24.9 and bmi<=29.9):print("Overweight")
else: print("Obesity")
