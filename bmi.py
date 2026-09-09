# BMI Calculator using conditional statements

weight = float(input("enter your weight in kg: "))
height = float(input("enter your height in meters: "))
bmi = weight / (height ** 2)
print(f"your bmi is: {bmi:.2f}")
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
