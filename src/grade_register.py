class GradeRegister:

    def __init__(self):
        self.grades = []

    def add_grade_based_on_points(self,points):
        self.grades.append(self.points_to_grades(points))

    def number_of_grades(self,grade):
        count = 0
        for received in self.grades:
            if (received == grade):
                count += 1

        return count

    def points_to_grades(self,points):

        grade = 0
        if (points < 50):
            grade = 0
        elif (points < 60):
            grade = 1
        elif (points < 70):
            grade = 2
        elif (points < 80):
            grade = 3
        elif (points < 90):
            grade = 4
        else:
            grade = 5

        return grade
