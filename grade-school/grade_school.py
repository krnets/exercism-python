# from collections import defaultdict
# from bisect import insort

# class School:
#     def __init__(self):
#         self.school = defaultdict(list)

#     def add_student(self, name, grade):
#         insort(self.school[grade], name)

#     def roster(self):
#         return [item for k, v in sorted(self.school.items()) for item in v]

#     def grade(self, grade_number):
#         return [item for item in self.school[grade_number]]

from collections import defaultdict


class School(object):
    def __init__(self):
        self.db = defaultdict(set)

    def grade(self, n):
        return sorted(list(self.db[n])) or []
        # return 1

    def add_student(self, name, grade):
        self.db[grade].add(name)

    def roster(self):
        return [name
                for k, v in sorted(self.db.items())
                for name in sorted(v)
                ]