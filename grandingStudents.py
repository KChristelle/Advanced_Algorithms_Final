# Algorithms summative Question 2


# Grading student function
def gradingStudents(grades):
    print("The original grades: ", grades)
    # final = []
    # pop first element of the list to start with grades
    grades.pop(0)
    # Loop through the list
    for i in range(0, len(grades)):
        # Check the first condition if grade is less than 38 skip
        if grades[i] < 38:
            continue
        else:
            # get the val of the grade mod 5
            rem = grades[i] % 5
            # Check next condition
            # print(rem)
            # print(grades[i])
            # if remainder is equal to 3 then add 5-3
            if rem == 3:
                grades[i] = grades[i] + 2
            # if remainder is equal to 4 then add 5-4
            elif rem == 4:
                grades[i] = grades[i] + 1
            # Else continue
            else:
                continue
    print("The final grades: ", grades)

    return grades

# Test Values
# grades = [4, 73, 67, 38, 33]
# print(gradingStudents(grades))
