name=input("Enter your name-")
weight=float(input("Enter your weight(in kilogram)="))
height_feet=float(input("Enter your height(in feet)=")) 

height_meter=height_feet*0.3048

bmi_val=weight/(height_meter*height_meter)

print("your BMI level is=",bmi_val)

