class Registration:
    def __init__(self):
        self.courses = []

    def add(self, name):
        self.courses.append(name)

    def show(self):
        for c in self.courses:
            print(c)


r = Registration()
r.add("Math")
r.add("CS")
r.show()

