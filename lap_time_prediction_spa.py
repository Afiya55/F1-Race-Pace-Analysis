import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df = pd.read_excel('2023_spa_verstappen.xlsx', header=1)
print("\n🏎️ Belgian Grand Prix Lap Time Prediction- Verstappen")
x = df[["Lap"]]
y = df[["Lap Time(s)"]]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(x_train,y_train)
future_laps = pd.DataFrame({
    "Lap":[39,40]
})
future_predictions = model.predict(future_laps)
print(" 🤖 Future Lap Predictions: ")
for lap, pred in zip([39,40], future_predictions):
    print(f"Lap {lap}: {pred[0]:.3f}s")