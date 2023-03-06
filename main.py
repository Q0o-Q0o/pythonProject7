from functions import get_student_by_pk, get_profession_by_title, check_fitness

studentPk = input(u'Введите номер студента: ')

student = get_student_by_pk(studentPk)

if student is None:
    print(u'У нас нет такого студента')
    quit()
print('Студент ' + student.get("full_name"))
print('Знает ' + ', '.join(student.get("skills")))

print('Выберите специальность для оценки студента ' + student.get("full_name"))
professionTitle = input()
profession = get_profession_by_title(professionTitle)
if profession is None:
    print("У нас нет такой специальности")
    quit()

d = check_fitness(student, profession)
print('Пригодность ' + str(d["fit"]) + '%')
print(student.get("full_name") + ' знает ' + ", ".join(d["has"]))
print(student.get("full_name") + ' не знает ' + ", ".join(d["lacks"]))

