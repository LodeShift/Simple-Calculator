# Simple calculator made in python. will get more features soon e.g, Divided, Multiply & Subtract.
# Note: i'm still in developement learning Python, so any tips/bugs is appriceated. Thank you!

def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3_input = input("Enter the third number (Press Enter to skip): ")

    # Check if num3 is empty, if so, set it to 0
    if num3_input == "":
        num3 = 0
    else:
        num3 = float(num3_input)
    
    # Perform the calculation (example: addition)
    result = num1 + num2 + num3
    print(f"Result: {result}")

# Calling the function
calculator()
