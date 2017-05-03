package main

import "fmt"


type User interface{
    permissions() int // 1-7
    name() string
}

type Admin struct {
    nombre string
    permiso int
}

func (this Admin) permissions() int{
     return this.permiso
}

func (this Admin) name() string{
     return this.nombre
}

func auth(usuario User) string{
    allpermissions :=""
    if usuario.permissions() ==1  {
        allpermissions = "ejecucion "
    }
    if usuario.permissions() == 2{
        allpermissions += "escritura "
    }
    if usuario.permissions() == 3{
        allpermissions += "escritura y ejecucion"
    }
    if usuario.permissions() == 4{
        allpermissions += "lectura "
    }
    if usuario.permissions() == 5{
        allpermissions += "lectura y ejecucion"
    }
    if usuario.permissions() == 6{
        allpermissions += "lectura y escritura"
    }
    if usuario.permissions() == 7{
        allpermissions += "lectura, escritura y ejecucion "
    }

    if allpermissions=="" || usuario.permissions()>=8 {
        return "No son validos los permisos de " + usuario.name()
    }

   return "los permisos que tiene "+ usuario.name()+" son de "+allpermissions
}

func main() {
    //admin := Admin{"Vito", 8}
    //fmt.Println(auth(admin))
    usuarios := []User{Admin{"Vito",4}, Admin{"Dante",7}}
    for _,usuario := range usuarios {
        fmt.Println(auth(usuario))
    }
}

