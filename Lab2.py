# Program to calculate the sum of two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum = num1 + num2
print("The sum of the ", num1, " and ", num2, " is ", sum)

# Program to swap the values of two variables
var1 = float(input("Enter the value of variable 1: "))
var2 = float(input("Enter the value of variable 2: "))
# Swapping values
var1, var2 = var2, var1
print(f"After swapping, variable 1 is: ", var1)
print(f"After swapping, variable 2 is: ", var2)

# Program to calculate the perimeter and area of a rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
perimeter = 2 * (length + width)
area = length * width
print("The perimeter of the rectangle is: ", perimeter)
print("The area of the rectangle is: ", area)

# Program to calculate the circumference and area of a circle
import math
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
area = math.pi * radius**2
print("The circumference of the circle is: ", circumference)
print("The area of the circle is: ", area)

# Program to convert temperatures from Fahrenheit to Celsius
fahrenheit_temp = float(input("Enter the temperature in Fahrenheit: "))
celsius_temp = (fahrenheit_temp - 32) * 5/9
print("The temperature in Celsius is: ", celsius_temp)

def solve_quadratic_equation(a, b, c):
    # Calculate discriminant
    discriminant = b**2 - 4*a*c

    # Check if the discriminant is positive, negative, or zero
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root,
    else:
        return None

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
roots = solve_quadratic_equation(a, b, c)

if roots is not None:
        print("The solutions of the quadratic equation are:", roots[0], roots[1])
else:
        print("No real roots exist for the quadratic equation.")

# Program to determine compound interest
principal_amount = 5000
annual_interest_rate = 3
years = 10

# Convert APR to a decimal
apr_decimal = annual_interest_rate / 100

# Calculate future value using compound interest formula
future_value = principal_amount * (1 + apr_decimal) ** years
print("The future value of the investment after ", years, " is: ", future_value)