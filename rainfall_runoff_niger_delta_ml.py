
# ============================================================
# Rainfall–Runoff Modeling for Niger Delta River Basins
# Using Hydrological Machine Learning (Synthetic Data)
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

def generate_synthetic_rainfall_runoff(days=1500):
    np.random.seed(42)

    rainfall = np.random.gamma(shape=2.5, scale=12, size=days)
    temperature = np.random.normal(28, 2.5, size=days)
    evapotranspiration = np.random.normal(4.5, 0.7, size=days)

    soil_moisture = np.clip(
        np.cumsum(rainfall - evapotranspiration) * 0.01 +
        np.random.normal(0.4, 0.05, days),
        0.1, 0.6
    )

    runoff = (
        0.45 * rainfall +
        0.35 * soil_moisture * rainfall -
        0.25 * evapotranspiration +
        np.random.normal(0, 5, days)
    )
    runoff = np.clip(runoff, 0, None)

    return pd.DataFrame({
        "rainfall_mm": rainfall,
        "temperature_c": temperature,
        "evapotranspiration_mm": evapotranspiration,
        "soil_moisture_index": soil_moisture,
        "river_discharge_m3s": runoff
    })

df = generate_synthetic_rainfall_runoff()

X = df[[
    "rainfall_mm",
    "temperature_c",
    "evapotranspiration_mm",
    "soil_moisture_index"
]]
y = df["river_discharge_m3s"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = RandomForestRegressor(
    n_estimators=200,
    max_depth=15,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("Rainfall–Runoff Model Performance")
print(f"RMSE: {rmse:.2f} m³/s")
print(f"R² Score: {r2:.3f}")

plt.figure(figsize=(12, 5))
plt.plot(y_test.values[:200], label="Observed Runoff")
plt.plot(y_pred[:200], label="Predicted Runoff", linestyle="--")
plt.legend()
plt.show()

plt.figure(figsize=(7, 4))
plt.barh(X.columns, model.feature_importances_)
plt.show()
