from interfaces import NSSPerson

class Instructor(NSSPerson):
    def __init__(self, first_name, last_name, slack_handle):
        self.specialty = ""
        NSSPerson.__init__(self, first_name, last_name, slack_handle)

    def assign(self, student, exercise):
        student.exercises.append(exercise)

    def specialty(self, specialty):
        self.specialty = specialty
