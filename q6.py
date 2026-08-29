import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/processed_student_performance.csv")


plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Final_Score"])
plt.title("Student Names vs Final Scores")
plt.xlabel("Student Names")
plt.ylabel("Final Score")
plt.tight_layout()
plt.savefig("final_scores.png")
plt.show()


plt.figure(figsize=(8, 5))
plt.scatter(df["Hours_Studied"], df["Final_Score"])
plt.title("Hours Studied vs Final Score")
plt.xlabel("Hours Studied")
plt.ylabel("Final Score")
plt.tight_layout()
plt.savefig("study_vs_score.png")
plt.show()


plt.figure(figsize=(8, 5))
plt.hist(df["Final_Score"], bins=5)
plt.title("Distribution of Final Scores")
plt.xlabel("Final Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("score_distribution.png")
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(df["Attendance"], df["Final_Score"])
plt.title("Attendance vs Final Score")
plt.xlabel("Attendance")
plt.ylabel("Final Score")
plt.tight_layout()
plt.savefig("custom_plot.png")
plt.show()
