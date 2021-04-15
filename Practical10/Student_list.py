class Student_list:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.program = None

    def set_first_name(self, fname):
        self.first_name = fname

    def set_last_name(self,lname):
        self.last_name = lname

    def set_program(self,pro):
        self.program = pro

    def print(self):
        print('student is ' + self.last_name + ' ' + self.first_name + ', and program is ' + self.program)


#example
student = Student_list()
student.set_first_name('xukai')
student.set_last_name('Gao')
student.set_program('BMS')
student.print()
