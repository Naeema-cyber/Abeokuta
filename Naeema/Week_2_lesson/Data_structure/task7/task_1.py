name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("State your gender: ")
empty_list = []
course1 = input("Your course: ")
course2 = input("Enter the second course: ")
course3 = input("Enter the third course: ")
empty_list.append("{course1}")
empty_list.append("{course2}")
empty_list.append("{course3}")


print(f"\tName: {name}\n\tAge: {age}\n\tGender: {gender}\n\tCourses: {empty_list} ")
