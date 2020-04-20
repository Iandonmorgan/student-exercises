class Cohort:
    def __init__(self, name):
        self.name = name
    
    def add_person(self, person):
        person.cohort = self.name