# ============================================
# Emergency (911-style) Calls Analysis Project
# Technologies: Python, Pandas, Matplotlib, Seaborn
# ============================================

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------
# STEP 1: Create the dataset manually
# (This avoids download / internet issues)
# --------------------------------------------

data = {
    'Reason': ['EMS', 'Fire', 'Traffic', 'EMS', 'Traffic', 'Fire', 'EMS', 'Traffic'],
    'Hour': [9, 14, 18, 22, 7, 16, 11, 20],
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday', 'Monday'],
    'Calls': [120, 80, 150, 90, 200, 70, 130, 160]
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

# Display the dataset
print("Dataset Preview:")
print(df)

# --------------------------------------------
# STEP 2: Basic Analysis using Pandas
# --------------------------------------------

# Total number of calls
total_calls = df['Calls'].sum()
print("\nTotal Emergency Calls:", total_calls)

# Calls grouped by reason
calls_by_reason = df.groupby('Reason')['Calls'].sum()
print("\nCalls by Reason:")
print(calls_by_reason)

# --------------------------------------------
# STEP 3: Data Visualization
# --------------------------------------------

# Set Seaborn style
sns.set(style="whitegrid")

# ---- Visualization 1: Calls by Reason ----
plt.figure()
sns.barplot(x='Reason', y='Calls', data=df)
plt.title("Emergency Calls by Reason")
plt.xlabel("Reason")
plt.ylabel("Number of Calls")
plt.show()

# ---- Visualization 2: Calls by Hour ----
plt.figure()
sns.lineplot(x='Hour', y='Calls', data=df, marker='o')
plt.title("Emergency Calls by Hour")
plt.xlabel("Hour of the Day")
plt.ylabel("Number of Calls")
plt.show()

# ---- Visualization 3: Calls by Day ----
plt.figure()
sns.barplot(x='Day', y='Calls', data=df)
plt.title("Emergency Calls by Day")
plt.xlabel("Day")
plt.ylabel("Number of Calls")
plt.xticks(rotation=45)
plt.show()

# --------------------------------------------
# STEP 4: Key Insights (Printed for clarity)
# --------------------------------------------

print("\nKey Insights:")
print("- Traffic-related calls are generally higher.")
print("- Peak emergency calls occur during evening hours.")
print("- Weekends show varied emergency call patterns.")

# --------------------------------------------
# END OF PROJECT
# --------------------------------------------
