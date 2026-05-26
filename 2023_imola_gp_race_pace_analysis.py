print("🏁 Welcome to the F1 Analyzer! - 2023 Imola GP Race Pace Analysis")

import pandas as pd
import matplotlib.pyplot as plt
import statistics

plt.style.use("dark_background")

# READ EXCEL FILE
df = pd.read_excel("2023_imola_race_pace.xlsx", header=1)
# DRIVER LIST
drivers = ["Sainz","Verstappen", "Leclerc"]

 
# STORE AVERAGE PACES
average_pace = {}

print("\n📊 DRIVER ANALYSIS\n")

# LOOP THROUGH DRIVERS
for driver in drivers:

    laps = df[driver]

    average_time = laps.mean()

    fastest_lap = laps.min()

    slowest_lap = laps.max()

    stdev = statistics.stdev(laps)

    average_pace[driver] = average_time

    # SPLIT STINT INTO HALVES
    first_half = laps[:len(laps)//2]

    second_half = laps[len(laps)//2:]

    first_half_avg = first_half.mean()

    second_half_avg = second_half.mean()

    # PRINT DRIVER DATA
    print(f"🏎️ Driver: {driver}")

    print(f"Average Pace: {average_time:.3f}s")

    print(f"Fastest Lap: {fastest_lap:.3f}s")

    print(f"Slowest Lap: {slowest_lap:.3f}s")

    print(f"Consistency: {stdev:.3f}s")

    # CONSISTENCY INSIGHT
    if stdev < 0.30:
        print("Insight: Very Consistent Race Pace")

    else:
        print("Insight: Inconsistent Race Pace Detected")

    # TREND ANALYSIS
    if second_half_avg > first_half_avg:
        print("Trend: Pace became slower during later laps (possible tyre degradation).")

    elif second_half_avg < first_half_avg:
        print("Trend: Pace improved during later laps (fuel burn advantage).")

    else:
        print("Trend: Stable pace throughout stint.")

    print("----------------------------------------")


# DRIVER RANKINGS
rankings = sorted(average_pace.items(), key=lambda x: x[1])

print("\n🏆 DRIVER RANKINGS\n")

position = 1

for driver, avg in rankings:

    print(f"{position}. {driver} — {avg:.3f}s")

    position += 1


# GRAPH
plt.figure(figsize=(10,6))

plt.plot(df["Lap"], df["Verstappen"], label="Verstappen", color="darkblue",marker="o")

plt.plot(df["Lap"], df["Leclerc"], label="Leclerc", color="red",marker="o")

plt.plot(df["Lap"], df["Sainz"], label="Sainz", color="lightblue",marker="o")

plt.xlabel("Lap")

plt.ylabel("Lap Time (s)")

plt.title("2023 Imola Race Pace Analysis")

plt.legend()


plt.grid(True)


plt.savefig("2023_imola_race_pace_analysis.png")
print("\n📈 Graph has been made successfully!")




input("\nPress Enter to open graph...")

plt.show()
