import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("dark_background")


df = pd.read_excel("matplotlib_starter.xlsx", header=1)

plt.plot(df["Lap"], df["Verstappen"], label="Verstappen",marker="o",color="darkblue")
plt.plot(df["Lap"], df["Sainz"], label="Sainz",marker="o",color="lightblue")
plt.plot(df["Lap"], df["Leclerc"], label="Leclerc",marker="o",color="red")

plt.title("2023 Miami GP Race Pace")
plt.legend()
plt.savefig("2023_miami_gp_race_pace.png")
plt.xlabel("Lap")

plt.ylabel("Lap Time(s)")
plt.grid(True)
plt.grid(color="white", alpha=0.2)


plt.show()

