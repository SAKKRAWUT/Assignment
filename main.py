class ABACStudent:
    def __init__(self, student_id: int, student_name: str, previous_institute: str):
        self.student_id = student_id
        self.student_name = student_name
        self.previous_institute = previous_institute

    def display_gpa(self):
        gpa = 3.5
        print(f"GPA of {self.student_name}: {gpa}")

    def display_credits_earned(self):
        credits = 120
        print(f"Credits earned by {self.student_name}: {credits}")


class MSMEStudent(ABACStudent):
    def __init__(self, student_id: int, student_name: str, previous_institute: str,
                 major: str, specialization: str, certificate: bool):
        super().__init__(student_id, student_name, previous_institute)
        self.major = major
        self.specialization = specialization
        self.certificate = certificate

    def display_major(self):
        print(f"Major of {self.student_name}: {self.major}")

    def display_certification(self):
        if self.certificate:
            print(f"{self.student_name} has earned a certificate.")
        else:
            print(f"{self.student_name} has not earned a certificate.")



student1 = MSMEStudent(6221003, "Sakkrawut", "Phanatpittayakarn School", "MIS", "Python", True)
student1.display_gpa()
student1.display_credits_earned()
student1.display_major()
student1.display_certification()




