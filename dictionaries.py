student_and_scores = {}
student_grades = {}
def grade_student_scores(score):
    if score >= 91:
        return "Outstanding"
    elif score >= 81:
        return "exceeds expectation"
    elif score >= 71:
        return "Acceptable"
    else:
        return "Fail"

inputting_scores = True
while inputting_scores:
    student_name = input("Input student's name: \n")
    student_score = int(input("Input student's score: \n"))
    to_continue = input('Type "continue" to make more inputs and "done" if there are no more inputs to make\n').lower()
    student_and_scores[student_name] = student_score
    if to_continue == "done":
        for name, score in student_and_scores.items():
            student_grades[name] = grade_student_scores(score)
            print(f"{name}'s grade: {grade_student_scores(score)}")
        inputting_scores = False