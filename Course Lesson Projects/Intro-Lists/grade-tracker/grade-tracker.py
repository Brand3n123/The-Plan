#create lists of students and grades
students = ["Alice", "Bob", "Charlie", "Diana"]
grades = [85, 92, 78, 90]

#identify how many students and print
amount_of_students = len(students)
print("There are", amount_of_students, "students in the class.")

#determine the highest and lowest grades of all students
highest_grade = max(grades)
lowest_grade = min(grades)
print("The highest grade is", highest_grade, "and the lowest grade is", lowest_grade,".")

#add new student Joshua and his grade to the class
students.append("Joshua")
grades.append(91)
print("New student", students[-1], "got a grade of", grades[-1], ".")

#remove student Charlie from the class and re-print our new lowest grade
students.pop(2)
grades.pop(2)
print("We had a student leave the class, which changes our lowest grade to", min(grades), ".")

#created a nested list that comtaining all student information (name and grade), 
#sort it descending by grade, and print the info about the top two students
student_file = sorted(list(zip(students, grades)), key=lambda x: x[1], reverse=True)
top_two = student_file[0:2]
print("The top two  students in the class are", top_two[0][0], 
      "with a grade of", top_two[0][1], "and", top_two[1][0], 
      "with a grade of", top_two[1][1], ".")
