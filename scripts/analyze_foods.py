#analyze_foods.py

import pandas as pd

# Load the Excel file directly from Downloads
foods = pd.read_csv(r"C:\Users\foods.csv")
foods.columns = foods.columns.str.strip()  # clean column names

print("Data loaded correctly:")
print(foods)

# Example: user ate some foods
meal = {"Tomato": 999, "Cheese": 50, "Spinach": 0}

total_histamine = 0
total_oxalate = 0

print("\nFood Intake Warnings:")
for food, grams in meal.items():
    row = foods[foods["Food"].str.lower() == food.lower()]
    if not row.empty:
        hist_val = row["Histamine_mg_per_kg"].values[0] * grams / 1000
        ox_val = row["Oxalate_mg_per_100g"].values[0] * grams / 100
        total_histamine += hist_val
        total_oxalate += ox_val

        if hist_val > 5:
            print(f"High histamine from {food}: {hist_val:.1f} mg")
        if ox_val > 50:
            print(f"High oxalate from {food}: {ox_val:.1f} mg")

print(f"\nTotal histamine intake: {total_histamine:.1f} mg")
print(f"Total oxalate intake: {total_oxalate:.1f} mg")

