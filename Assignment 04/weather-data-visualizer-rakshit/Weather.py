# WEATHER DATA VISUALIZER
# Author: Rakshit Yadav
# Date: 30 Nov 2025

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Create folder for images
os.makedirs("plots", exist_ok=True)


# Task 1: Load and Inspect Data


df = pd.read_csv("weather.csv")

print(df.head())
print(df.info())
print(df.describe())


# Task 2: Data Cleaning and Processing


# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Remove rows with invalid dates
df = df.dropna(subset=['date'])

# Fill missing numeric values with forward fill
df['temperature'] = df['temperature'].fillna(method='ffill')
df['rainfall'] = df['rainfall'].fillna(0)
df['humidity'] = df['humidity'].fillna(df['humidity'].mean())

# Keep only relevant columns
df_clean = df[['date', 'temperature', 'rainfall', 'humidity']]

# Save cleaned CSV
df_clean.to_csv("cleaned_weather.csv", index=False)

# Task 3: NumPy Statistics


daily_mean = np.mean(df_clean['temperature'])
daily_min = np.min(df_clean['temperature'])
daily_max = np.max(df_clean['temperature'])
daily_std = np.std(df_clean['temperature'])

print("\n=== Temperature Statistics ===")
print("Mean:", daily_mean)
print("Min:", daily_min)
print("Max:", daily_max)
print("Std Dev:", daily_std)


# Task 4: Visualization


# Line Chart - Daily Temperature Trend
plt.figure(figsize=(10,5))
plt.plot(df_clean['date'], df_clean['temperature'])
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.savefig("plots/daily_temperature.png")
plt.close()

# Bar Chart - Monthly Rainfall
df_clean['month'] = df_clean['date'].dt.month
monthly_rain = df_clean.groupby('month')['rainfall'].sum()

plt.figure(figsize=(10,5))
plt.bar(monthly_rain.index, monthly_rain.values)
plt.title("Monthly Rainfall Totals")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.savefig("plots/monthly_rainfall.png")
plt.close()

# Scatter Plot - Humidity vs Temperature
plt.figure(figsize=(7,5))
plt.scatter(df_clean['temperature'], df_clean['humidity'])
plt.title("Humidity vs Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.savefig("plots/humidity_vs_temperature.png")
plt.close()

# Combined Plot
plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.plot(df_clean['date'], df_clean['temperature'])
plt.title("Temperature Trend")
plt.xlabel("Date")

plt.subplot(1,2,2)
plt.scatter(df_clean['temperature'], df_clean['humidity'])
plt.title("Humidity vs Temperature")
plt.xlabel("Temperature")

plt.tight_layout()
plt.savefig("plots/combined_plot.png")
plt.close()


# Task 5: Grouping and Aggregation


monthly_stats = df_clean.groupby('month').agg({
    'temperature':['mean','min','max'],
    'rainfall':'sum',
    'humidity':'mean'
})

print("\n=== Monthly Weather Summary ===")
print(monthly_stats)

# 
# Task 6: Export + Storytelling


with open("summary_report.md", "w") as f:
    f.write("# Weather Data Analysis Report\n")
    f.write("## Summary of Insights\n\n")
    f.write(f"- Average daily temperature: {daily_mean:.2f}°C\n")
    f.write(f"- Minimum recorded temperature: {daily_min:.2f}°C\n")
    f.write(f"- Maximum recorded temperature: {daily_max:.2f}°C\n")
    f.write(f"- Temperature standard deviation: {daily_std:.2f}\n\n")
    f.write("## Monthly Rainfall\n")
    f.write(monthly_rain.to_string())
    f.write("\n\n## Notes:\n- Rainfall fluctuates per season.\n")
    f.write("- Temperature follows a clear trend.\n")
    f.write("- Humidity correlates moderately with temperature.\n")

print("\nAll tasks completed successfully!")