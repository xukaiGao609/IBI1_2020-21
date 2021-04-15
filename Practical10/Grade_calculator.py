student_name = input('the name of student is: ')
grade_portfolio = input('the grade of portfolio for the student is: ')
grade_presentation = input('the grade of presentation for the student is: ')
grade_exam = input('the grade of final exam for the student is: ')
def grade_calculate():
    total_grade=0
    total_grade = 0.4*int(grade_portfolio)+0.3*int(grade_presentation)+0.3*int(grade_exam)
    print(str(student_name)+'    '+str(total_grade))
    return student_name
    return total_grade
grade_calculate()

#example
#Tony Stuck
#100
#100
#100
