# Student Grade Manager v1.0
# Written by Prakash Gangurde

def get_grade(score):
    if score >= 90: return "A"
    elif score >= 75: return "B"
    elif score >= 60: return "C"
    elif score >= 40: return "D"
    else: return "F"

name = input("Student name: ")
score = int(input("Score (0-100): "))
print(f"{name}: {score}/100 — Grade {get_grade(score)}")
