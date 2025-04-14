print("📊 GRADE CALCULATOR 📊")

number_of_inputs = 0
grade_total = 0
scores = []


def grade_student(curr_avg):
    if (curr_avg >= 90):
        print("Your grade is A")
    elif (curr_avg >= 80):
        print("Your grade is B")
    elif (curr_avg >= 70):
        print("Your grade is C")
    elif (curr_avg >= 60):
        print("Your grade is D")
    else:
        print("Your grade is E")


try:
    while (True):
        grade_input = input("Enter grade (1 to 100 or done): ")
        if (grade_input == "done"):
            break
        else:
            grade = int(grade_input)
            scores.append(grade)
            grade_total += grade
            number_of_inputs += 1
            current_avg = grade_total / number_of_inputs
            print("Scores:", scores)
            print("Your Average is ", current_avg)
            grade_student(current_avg)

except:
    print("❌ Enter a valid input ❌")
