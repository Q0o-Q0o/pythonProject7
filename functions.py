import json


def load(filename):
    with open(filename, 'r', encoding='utf8') as json_file:
        return json.load(json_file)


def load_students():
    return load('students.json')


def load_profession():
    return load('professions.json')


def get_student_by_pk(pk):
    students = load_students()
    for i in range(len(students)):
        student = students[i]
        if str(student.get('pk')) == pk:
            return student
    return None


def get_profession_by_title(title):
    professions = load_profession()
    for i in range(len(professions)):
        profession = professions[i]
        if profession.get('title') == title:
            return profession
    return None


def check_fitness(student, profession):
    d = dict()
    d['has'] = list(set(student.get('skills')) & set(profession.get('skills')))
    a = list(set(student.get('skills')) - set(profession.get('skills')))
    b = list(set(profession.get('skills')) - set(student.get('skills')))
    d['lacks'] = a + b
    d['fit'] = len(d['has']) / len(profession.get('skills')) * 100
    return d
