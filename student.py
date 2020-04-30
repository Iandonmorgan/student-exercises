from interfaces import NSSPerson

class Student(NSSPerson):
    def __init__(self, first_name, last_name, slack_handle):
        self.exercises = list()
        NSSPerson.__init__(self, first_name, last_name, slack_handle)