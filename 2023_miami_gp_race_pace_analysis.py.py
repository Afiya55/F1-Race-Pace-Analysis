import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("matplotlib_starter.xlsx")

plt.plot(df["Lap"], df["Verstappen"], label="Verstappen",marker="o",color="darkblue")
plt.plot(df["Lap"], df["Sainz"], label="Sainz",marker="o",color="lightblue")
plt.plot(df["Lap"], df["Leclerc"], label="Leclerc",marker="o",color="red")

plt.title("2023 Miami GP Race Pace")
plt.legend()
plt.savefig("matplotlib_starter_race_pace.png")
plt.xlabel("Lap")

plt.ylabel("Lap Time(s)")
plt.grid(True)

plt.show()
