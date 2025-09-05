try:
    score = int(input("Enter a score: "))
    grade = ""

    if (score < 0 or score > 100):
        print("Error: Score must be between 0 and 100")
    elif (90 <= score <= 100):
        grade = "A"
    elif (score >= 80):
        grade = "B"
    elif (score >= 70):
        grade = "C"
    elif (score >= 60):
        grade = "D"
    elif (score < 60):
        grade = "F"

    if grade:
        print("Score:", score)
        print("Grade:", grade)

except ValueError:
    print("Make sure you're only entering in a valid number (1-100)")
