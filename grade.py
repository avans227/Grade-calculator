marks= int(input("Enter your marks: ")) 

if marks > 100 or marks < 0:
    print("Invalid marks")
elif marks >= 85:
    print("Grade: A+")
elif marks >=75:
    print("Grade: A")
elif marks >= 65:
    print("Grade: B+")
elif marks >= 55:
    print("Grade: B")
elif marks >= 45:
    print("Grade: C+")
elif marks >= 35: 
    print("Grade: C")
elif marks >= 30:
    print("Grade: D")
elif marks<30:
    print("Grade: F")

