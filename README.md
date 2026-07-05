# Python Grade Manager

This is a small beginner-friendly Python project for practicing Git and GitHub while building a simple student grade calculator.

## Project Overview

The app takes a student name and a score from 0 to 100, then prints the corresponding grade.

## Features

- Accepts student name from the user
- Accepts a score from 0 to 100
- Converts the score into a grade
- Prints a simple result to the terminal

## Grade Rules

- 90 and above: A
- 75 to 89: B
- 60 to 74: C
- 40 to 59: D
- Below 40: F

## Requirements

- Python 3.x
- Git installed for version control practice

## How To Run

1. Open a terminal in this folder.
2. Run the app:

```bash
python app.py
```

3. Enter the student name and score when prompted.

## Example

```text
Student name: Prakash
Score (0-100): 88
Prakash: 88/100 - Grade B
```

## Git Practical Steps

This project is also used to practice Git workflow.

```bash
git init
git add .
git commit -m "Initial commit: add grade manager app"
git branch -M main
git remote add origin https://github.com/prakashgangurde-ux/python-grade-manager.git
git push -u origin main
```

## File Structure

```text
python-grade-manager/
├── app.py
├── README.md
└── .gitignore
```

## Notes

- The `.gitignore` file excludes Python cache files, virtual environments, and environment files.
- This project is intentionally simple so it can be used as a Git and Python practice exercise.

## Future Improvements

- Validate score input so only numbers between 0 and 100 are accepted
- Add support for multiple subjects
- Save results to a file
- Turn it into a menu-based application

