import pandas as pd
import matplotlib.pyplot as plt

# ---------- Step 1: Load Data ----------
df = pd.read_excel("input.xlsx")   # <- Change file name if needed

subjects = df.columns[1:]  # Skip Name column

# ---------- Step 2: Calculations ----------
df["Total"] = df[subjects].sum(axis=1)
df["Percentage"] = df["Total"] / (len(subjects) * 100) * 100

def get_grade(p):
    if p >= 90: return "A+"
    elif p >= 80: return "A"
    elif p >= 70: return "B"
    elif p >= 60: return "C"
    elif p >= 50: return "D"
    else: return "Fail"

df["Grade"] = df["Percentage"].apply(get_grade)
df["Pass/Fail"] = df["Grade"].apply(lambda g: "Pass" if g != "Fail" else "Fail")

# ---------- Step 3: Show Toppers ----------
print("\n=== CLASS TOPPERS ===")
print(df.sort_values(by="Total", ascending=False).head(3)[["Name", "Total", "Percentage", "Grade"]])

# ---------- Step 4: Subject Average ----------
avg_scores = df[subjects].mean()
print("\n=== SUBJECT-WISE AVERAGE ===")
print(avg_scores)

# ---------- Step 5: Graph ----------
avg_scores.plot(kind="bar", title="Subject-wise Average Performance", figsize=(8,4))
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show()

# ---------- Step 6: Export ----------
df.to_excel("result_output.xlsx", index=False)
print("\n🎉 Analysis complete! Results saved in result_output.xlsx")
