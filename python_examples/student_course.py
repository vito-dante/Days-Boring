__author__ = 'dante'

from typing import Optional, Tuple
import datetime as fecha

class Person(object):

    __Name: str = ""
    __last_name: str = ""
    __date_of_birth: fecha

    def __init__(self, name: str, last_name: str, date_of_birth: fecha) -> None:
        self.__Name = name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth

    def get_name(self) -> str:
        return self.__Name

    def get_last_name(self) -> str:
        return self.__last_name

    def get_date_of_birth(self) -> fecha:
        return self.__date_of_birth

    def get_age(self) -> int:
        _Today = fecha.date.today()
        born = self.get_date_of_birth()
        return _Today.year - born.year - ((_Today.month, _Today.day) < (born.month, born.day))


class Estudiante(Person):
    _CedulaID: int
    _Course: 'Course'

    def __init__(self, name: str, last_name: str, date_of_birth: fecha,
                 cedulaid: int, curso: 'Course'):
        super(Estudiante, self).__init__(name, last_name, date_of_birth)
        self._CedulaID = cedulaid
        self._Course = curso

    def get_course(self) -> 'Course':
        return self._Course

    def get_cedule_id(self) -> int:
        return self._CedulaID


class Course(object):
    _name_course: str
    _Capacity: int
    _list_students = []  # type [Estudiantes]

    def __init__(self, nombreCurso: str, capacidad: int) -> None:
        self._name_course = nombreCurso
        self._Capacity = capacidad

    def add_student(self, estudiante: Estudiante) -> None:
        if len(self._list_students) < self._Capacity:
            self._list_students.append(estudiante)
        else:
            return

    def list_all_students(self) -> None:
        for student in self._list_students:
            print(student.get_name())


fechaNacimiento = fecha.date(1991, 1, 25)
miCurso = Course("CLASE777", 2)
vito = Estudiante("vito", "marca", fechaNacimiento, 456, miCurso)
carlos = Estudiante("Carlos", "Alpires", fechaNacimiento, 456, miCurso)
david = Estudiante("David", "Cercado", fechaNacimiento, 456, miCurso)


miCurso.add_student(vito)
miCurso.add_student(carlos)
miCurso.add_student(david)
miCurso.list_all_students()

print(vito.get_age())
