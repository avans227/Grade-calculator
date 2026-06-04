subject = int(input("Enter the number of subjects: "))
total_marks= subject*100
total_marks_obtained=0
   
for subjects in range(subject):
    while True:
        subject_marks = int(input("Enter your marks: ")) 
        if 0 <= subject_marks <= 100:
            break
        print("Invalid marks. try again.")

    total_marks_obtained += subject_marks
    if subject_marks > 100 or subject_marks < 0:
            print("Invalid marks. try again.")

    elif subject_marks >= 85:
            print("Grade: A+")
    elif subject_marks >=75:
            print("Grade: A")
    elif subject_marks >= 65:
            print("Grade: B+")
    elif subject_marks >= 55:
            print("Grade: B")
    elif subject_marks >= 45:
            print("Grade: C+")
    elif subject_marks >= 35: 
            print("Grade: C")
    elif subject_marks >= 30:
            print("Grade: D")
    elif subject_marks<30:
            print("Grade: F")
   
percentage= (total_marks_obtained/total_marks)*100

if percentage >= 85:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 65:
    grade = "B+"
elif percentage >= 55:
    grade = "B"
elif percentage >= 45:
    grade = "C+"
elif percentage >= 35:
    grade = "C"
elif percentage >= 30:
    grade = "D"
else:
    grade = "F"

print("\nResults")
print("Total Marks Obtained:", total_marks_obtained)
print("Total Marks:", total_marks)
print("Percentage:", round(percentage, 4), "%")
print("Final Grade:", grade)