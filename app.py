# Student Grade Manager v2.0
# Written by Prakash Gangurde

def get_grade(score):
    if score >= 90: return "A"
    elif score >= 75: return "B"
    elif score >= 60: return "C"
    elif score >= 40: return "D"
    else: return "F"

subjects = ["Python", "Linux", "Web Dev"]
name = input("Student name: ")
scores = []
for subject in subjects:
    score = int(input(f"{subject} score: "))
    scores.append(score)

print(f"\nReport for {name}:")
for subject, score in zip(subjects, scores):
    print(f"  {subject}: {score}/100 — Grade {get_grade(score)}")
print(f"  Average: {sum(scores)//len(scores)}/100")
