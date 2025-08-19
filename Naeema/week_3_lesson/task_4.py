student = {}
name = input("Enter your name: ")
age = int(input("Enter your age: "))
scores = [70, 85, 90]

student.update({"Name": name})
student.update({"Age": age})
student.update({"Scores": scores})

average_score = (student[scores][0] + student[scores][1] + student[scores][2])/ 4