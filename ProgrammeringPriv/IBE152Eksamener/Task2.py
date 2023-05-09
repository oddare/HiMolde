courses = {
    'IBE152': ['Juan', 'Ana', 'Claudia'],
    'IBE500': ['Pedro', 'Linda', 'Maria'],
    'HIST01': ['David', 'Laura'],
}

def getFemales(courses: dict) -> tuple:
    females = []

    for course in courses:
        for student in courses[course]:
            if student[-1] == 'a':
                females.append(student)
    return tuple(females)

print(getFemales(courses))