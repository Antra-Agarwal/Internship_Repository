print("=== Exception Handling Examples ===\n")

# -------------------------------
# Example 1: ZeroDivisionError
# -------------------------------
try:
    number = int(input("Enter a number to divide 100 by: "))
    result = 100 / number
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter a valid integer.")

print("\n-------------------------------")

# -------------------------------
# Example 2: File Handling
# -------------------------------
try:
    with open("sample.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Error: sample.txt does not exist.")

print("\n-------------------------------")

# -------------------------------
# Example 3: Generic Exception
# -------------------------------
try:
    numbers = [10, 20, 30]
    print(numbers[5])

except Exception as e:
    print("Unexpected Error:", e)

print("\nProgram executed successfully!")