print("Welcome to GPA calculator")
print("Please enter all your letter grade ")
print("Enter blank space to end")

points = {'A+':4.0, 'A':4.0, 'A-':3.67}

num_courses = 0

num_total = 0

done = False

while not done:
    grade = input()
    if grade == " ":
        done = True
    elif grade not in points:
        print('{0} is unknown'.format(grade))
    else:
        num_total+=1
        num_courses+=points[grade]

if num_courses > 0:
    print('Your GPA is {0}'.format(num_courses/num_total))
    print('Your GPA is {0}'.format(num_courses/num_total))
    print('Your GPA is {0}'.format(num_courses/num_total))
    print('Your GPA is {0}'.format(num_courses/num_total))
    print('Your GPA is {0}'.format(num_courses/num_total))

