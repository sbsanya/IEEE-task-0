import numpy as np
hours = np.array([5, 7, 3, 8, 6])
attendance = np.array([90, 85, 75, 95, 88])
previous_scores = np.array([65, 80, 55, 82, 70])
final_scores = np.array([70, 91, 58, 87, 76])
print("Hours studied:", hours.shape, hours.dtype)
print("Attendance:", attendance.shape, attendance.dtype)
print("Previous scores:", previous_scores.shape, previous_scores.dtype)
print("Final scores:", final_scores.shape, final_scores.dtype)
print("Mean final score:", np.mean(final_scores))
print("Maximum final score:", np.max(final_scores))
print("Minimum final score:", np.min(final_scores))
print("Standard deviation:", np.std(final_scores))
bonus_scores = final_scores + 5
print("Scores after bonus:", bonus_scores)
passed = bonus_scores >= 75       #True False ki list
print("Boolean array:", passed)
print("Scores >= 75:", bonus_scores[passed])       #wahi marks print honge jo 'True' h in passed
