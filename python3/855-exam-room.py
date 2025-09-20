class ExamRoom:

    def __init__(self, n: int):
        self.size = n
        self.students = []

    def seat(self) -> int:
        if self.students:
            max_dist = self.students[0]
            next_student = 0
            for i in range(1, len(self.students)):
                u = self.students[i-1]
                v = self.students[i]
                gap = v - u
                center = u + gap // 2

                if center - u > max_dist:
                    max_dist = center - u
                    next_student = center

            if self.size - 1 - self.students[-1] > max_dist:
                next_student = self.size - 1
            bisect.insort(self.students, next_student)
            return next_student

        else:
            self.students.append(0)
            return 0

    def leave(self, p: int) -> None:
        self.students.remove(p)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)