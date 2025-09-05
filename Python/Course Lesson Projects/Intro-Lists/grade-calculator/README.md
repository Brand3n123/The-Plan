# 🎓 Grade Calculator

A Python program that takes a numeric score (0–100) as input and outputs the corresponding letter grade (A–F).  
Built to practice control flow (`if/elif/else`) and input validation.

---

## 📌 Features
- Converts numeric scores to letter grades:
  - A: 90–100  
  - B: 80–89  
  - C: 70–79  
  - D: 60–69  
  - F: < 60
- Validates that the score is between 0 and 100.
- Catches invalid inputs (non-numeric values) with a friendly error message.

---

## ▶️ Usage
Run with Python 3:

```bash
python3 grade_calculator.py


Example Outputs:

Enter a score: 92
Score: 92
Grade: A


Enter a score: 73
Score: 73
Grade: C


Enter a score: 150
Error: Score must be between 0 and 100


Enter a score: dog
Make sure you're only entering in a valid number (1-100)
