def BMI(name,weight,height_meter):
    bmi_val= round(weight/(height_meter * height_meter), 2)
    print("your BMI level is=",bmi_val)
    return bmi_val

name=input("Enter your name")
weight=float(input ("Enter your weight (in kilogram)="))
height_feet = float(input("Enter your height (in feet)="))

height_meter=(height_feet*0.3048)

bmi_val=BMI(name,weight,height_meter)

if(bmi_val <= 18.4):
    print("Underweight")

elif(bmi_val <= 24.9):
    print("Normal weight")
    
elif(bmi_val <= 29.9):
    print("Over weight")

elif(bmi_val <= 34.9):
    print("Obese")

elif(bmi_val >= 35):
    print("Highly Obese")
    