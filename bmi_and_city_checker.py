# --- Task 1: BMI Category Checker ---
print("BMI Category Checker")
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")

if bmi >= 30:
    print("Category: Obesity")
elif 25 <= bmi < 30:
    print("Category: Overweight")
elif 18.5 <= bmi < 25:
    print("Category: Normal")
else:
    print("Category: Underweight")

print("\n" + "-"*40 + "\n")

# --- Task 2: City-to-Country Identifier ---
print("City to Country Identifier")
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter a city name: ").strip()

if city in australia:
    print(f"{city} is in Australia")
elif city in uae:
    print(f"{city} is in UAE")
elif city in india:
    print(f"{city} is in India")
else:
    print(f"Sorry, {city} is not in our database.")
