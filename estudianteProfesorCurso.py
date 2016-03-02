__author__ = 'dante'

import datetime as fecha

class Persona(object):

    __Nombre= str()
    __Apellido= str()
    __Nacimiento =""

    def __init__(self,nombre, apellido, nacimiento):
        self.__Nombre=nombre
        self.__Apellido=apellido
        self.__Nacimiento=nacimiento

    def getNombre(self):
        return self.__Nombre

    def getApellido(self):
        return self.__Apellido

    def getNacimiento(self):
        return self.__Nacimiento

    def getEdad(self):
        _Today = fecha.date.today()
        born = self.getNacimiento()
        return _Today.year - born.year - ((_Today.month, _Today.day) < (born.month, born.day))



class Curso(object):
    _NombreCourse=str()
    _Capacidad=int()
    _EstudiantesAll = list()


    def __init__(self, nombreCurso, capacidad):
        self._NombreCourse=nombreCurso
        self._Capacidad=capacidad

    def addStudent(self, estudiante):
        if(type(estudiante) == Estudiante):
            self._EstudiantesAll.append(estudiante)
        else:
            print("EL VALOR QUE ACABAS DE INSERTAR NO ES VALIDO")

    def listAllStudent(self):
        for student in self._EstudiantesAll:
            print(student.getNombre())


class Estudiante(Persona):

    _CedulaID = int()
    _Curso = Curso("",0)

    def __init__(self, nombre, apellido, nacimiento, cedulaid, curso):
        super(Estudiante, self).__init__(nombre,apellido,nacimiento)
        self._CedulaID = cedulaid
        self._Curso = curso

    def getCurso(self):
        return self._Curso

    def getCedulaId(self):
        return self._CedulaID

fechaNacimiento = fecha.date(1991,6,15)
miCurso = Curso("CLASE777", 28)
soyYo = Estudiante("vito","marca",fechaNacimiento,456,miCurso)
soyYo1 = Estudiante("Carlos","Alpires",fechaNacimiento,456,miCurso)
soyYo2 = Estudiante("David","Cercado",fechaNacimiento,456,miCurso)

miCurso.addStudent(456)
miCurso.addStudent(soyYo)
miCurso.addStudent(soyYo1)
miCurso.addStudent(soyYo2)
miCurso.listAllStudent()

print(soyYo.getEdad())

