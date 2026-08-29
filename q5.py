import pandas as pd
df = pd.read_csv("data/student_performance.csv")
print("First five rows:")
print(df.head(5))
print("Number of rows and columns:", df.shape)
print("Column names:",df.columns)
print("Missing values:",df.isnull())
print("Average Final Score:", df["Final_Score"].mean())
highest = df["Final_Score"].idxmax()
print("Student with highest Final Score:", df.loc[highest])
df["Improvement"] = df["Final_Score"] - df["Previous_Score"]
students = df["Attendance"] >= 80
print("Students with attendance >= 80:", df[students])
df = df.sort_values("Final_Score", ascending=False)
print("Sorted DataFrame:",df)
df.to_csv("processed_student_performance.csv", index=False)
