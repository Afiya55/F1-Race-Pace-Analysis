import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_excel("2023_verstappen_hungary.xlsx", header = 1)
df = df[df["Lap"] != 23]
average_lap = df["Lap Time(s)"].mean()
fastest_lap = df["Lap Time(s)"].min()
slowest_lap = df["Lap Time(s)"].max()
print("🏎️ Hungary 2023 Stint Analysis- Verstappen")
print(f"Average Lap Time: {average_lap:.3f} seconds")
print(f"Fastest Lap Time: {fastest_lap:.3f} seconds")
print(f"Slowest Lap Time: {slowest_lap:.3f} seconds")
sns.regplot(x="Lap", y="Lap Time(s)", data=df, marker="o", color="darkblue")
plt.title("Verstappen Hungary 2023 Stint Analysis\nRegression Trend")
plt.xlabel("Lap")
plt.ylabel("Lap Time (s)")
plt.grid(True)
plt.savefig("verstappen_2023_hungary_regression.png")
input("Press Enter to view the regression plot...")
plt.show()