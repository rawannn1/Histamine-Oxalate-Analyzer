import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("results", exist_ok=True)

# Load foods data
foods = pd.read_csv("data/foods.csv")

# 1 Summary statistics
summary_hist = foods["Histamine_mg_per_kg"].describe()
summary_ox = foods["Oxalate_mg_per_100g"].describe()

with open("results/summary.txt", "w") as f:
    f.write("Histamine Summary (mg/kg):\n")
    f.write(summary_hist.to_string())
    f.write("\n\nOxalate Summary (mg/100g):\n")
    f.write(summary_ox.to_string())

# 2️ Histogram of histamine content
plt.hist(foods["Histamine_mg_per_kg"], bins=10, color='salmon', edgecolor='black')
plt.title("Histamine Content in Foods")
plt.xlabel("Histamine (mg/kg)")
plt.ylabel("Frequency")
plt.savefig("results/histamine_hist.png")
plt.close()

# 3️ User input example: foods eaten
# Example: user ate 100g of tomato, 50g cheese
meal = {"Tomato": 100, "Cheese": 50, "Spinach": 50}  # grams

total_histamine = 0
total_oxalate = 0

print("Food Intake Warnings:")
for food, grams in meal.items():
    row = foods[foods["Food"].str.lower() == food.lower()]
    if not row.empty:
        hist_val = row["Histamine_mg_per_kg"].values[0] * grams / 1000  # mg/kg -> mg
        ox_val = row["Oxalate_mg_per_100g"].values[0] * grams / 100
        total_histamine += hist_val
        total_oxalate += ox_val

        if hist_val > 5:  # arbitrary threshold
            print(f"High histamine from {food}: {hist_val:.1f} mg")
        if ox_val > 50:
            print(f"High oxalate from {food}: {ox_val:.1f} mg")

print(f"\nTotal histamine intake: {total_histamine:.1f} mg")
print(f"Total oxalate intake: {total_oxalate:.1f} mg")

print("\n Analysis complete! See results/summary.txt and histamine_hist.png")
