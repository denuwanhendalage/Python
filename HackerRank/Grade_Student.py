def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        element = grades[i]
        if element >= 38:
            get_difference = 5-element % 5
            print(get_difference)
            if get_difference < 3:
                element = (element//5)*5+5
        grades[i] = element
    return grades


print(gradingStudents([73, 67, 38, 33]))  # [75, 67, 40, 33]
