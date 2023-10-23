class Student:#to jest tzw Classa, typ obiektu , kazda klasa to inny typ jak typ : str, int , bol
    pass

class Grade:#nazwy Class piszemy z wielkiej litery
    pass

class School:
    pass


if __name__ == '__main__':
    student_radek = Student()#obiekt klasy Student

    grade_a = Grade()#obiekty klasy Grade
    grade_b = Grade()

    my_school = School()#obiekt klasy School

    print(grade_b,grade_a)
    print(student_radek)
    print(my_school)

    # print("type(student_radek)",type(student_radek))
    # print("type(grade_a)", type(grade_a))
    # print("type(grade_b)", type(grade_b))
    # print("type(my_school)", type(my_school))

    all_students = [Student(),Student(),Student(),Student()]
    print(all_students)
    print(all_students[0])

    grades = {
        1:Grade(),
        2:Grade(),
        3:Grade(),
        4:Grade(),
        5:Grade()
    }
    print(grades)


    #ZADANIE Klasy i Obiekty


class Ziemniaki:
    pass
class Jablka:
    pass
class Zamow:
    pass
class Produkt:
    pass

if __name__ == '__main__':
    bataty = Ziemniaki()
    mlode_ziemniaki  = Ziemniaki()

    antonowka = Jablka()
    idared = Jablka()
    ligol = Jablka()

    print("typ batata to ",type(bataty))
    print(f"typ mlodego ziemniaka to",type(mlode_ziemniaki))
    print(f"typ antonowki to ",type(antonowka))
    print(f"typ idaredu to ",type(idared))
    print(f"typ ligol to ",type(ligol))

    zamowienie = [Zamow(),Zamow(),Zamow(),Zamow()]
    print(zamowienie)

    produkty = {
        "batat":Produkt(),
        "mlody_ziemniak": Produkt(),
        "antonowka": Produkt(),
        "idared": Produkt(),
        "ligol": Produkt(),
    }
    print(produkty)
