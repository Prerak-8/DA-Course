import math

# Mathematical utility functions.

def cal_factorial():
    num = int(input("Enter a number: "))
    fact = math.factorial(num)

    print("Factorial:", fact)
    print("--------------------------\n")

def compound_interest():
    principal_amt = int(input("Enter principal amount: "))
    rate_interest = int(input("Enter rate of interest (in %): "))
    time_year = int(input("Enter time (in years): "))

    comp_inte = principal_amt * ((1 + rate_interest / 100) ** time_year)

    print("Compound Interest:", comp_inte)
    print("--------------------------\n")

def trigo_cal():
    sin_val = int(input("Enter value for sin in degrees: "))
    cos_val = int(input("Enter value for cos in degrees: "))
    tan_val = int(input("Enter value for tan in degrees: "))

    sin_rad = math.sin(math.radians(sin_val))
    cos_rad = math.cos(math.radians(cos_val))
    tan_rad = math.tan(math.radians(tan_val))

    print("Value of sin:", sin_rad)
    print("Value of cos:", cos_rad)
    print("Value of tan:", tan_rad)
    print("--------------------------\n")

def area_geo():
    radius = float(input("Enter radius (in cm) for circle: "))
    length = float(input("Enter length (in cm) for rectangle: "))
    breadth = float(input("Enter breadth (in cm) for rectangle: "))
    base = float(input("Enter base (in cm) for triangle: "))
    height = float(input("Enter height (in cm) for triangle: "))

    area_circ = math.pi * radius**2
    area_rec = length * breadth
    area_tri = base * height * 0.5

    print("Area of Circle:", round(area_circ, 3))
    print("Area of Rectangle:", round(area_rec, 3))
    print("Area of Triangle:", round(area_tri, 3))
    print("--------------------------\n")