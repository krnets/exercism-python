SEEDS = dict(C="Clover", G="Grass", R="Radishes", V="Violets")

STUDENTS = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred",
            "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]


class Garden:
    def __init__(self, diagram, students=STUDENTS):
        self.diagram = diagram.splitlines()
        self.students = sorted(students)

    def plants(self, student):
        student_idx = self.students.index(student) * 2
        return [SEEDS[row[i]] for row in self.diagram for i in (student_idx, student_idx+1)]
