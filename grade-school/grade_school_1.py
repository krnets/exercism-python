from collections import defaultdict
from bisect import insort

class School:
    def __init__(self):
        self.school = defaultdict(list)

    def add_student(self, name, grade):
        insort(self.school[grade], name)

    def roster(self):
        return [item for k, v in sorted(self.school.items()) for item in v]

    def grade(self, grade_number):
        return [item for item in self.school[grade_number]]