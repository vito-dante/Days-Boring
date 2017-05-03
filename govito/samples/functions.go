package main

import (
	"fmt"
	"reflect"
)

func main() {
	//vito := usuario{"vito", "vito@gmail.com"}
	vergil := struct {
		name string
		age  int
	}{
		name: "vergil",
		age:  33,
	}
	vergil.name = "dante"
	fmt.Println(vergil.name)

	value := usertest(vergil)
	fmt.Println(reflect.TypeOf(vergil))
	//fmt.Println(value.name)
	//u, err := newUsuario(vergil)
	//if err != "" {
	//fmt.Println(err)
	//}
	//fmt.Println(u.name)
}

type usuario struct {
	name  string
	email string
}

func usertest(a *struct)(*struct){
a.name = "another name "
return a
}

//func newUsuario(myuser struct) (struct, string) {
//return myuser, "there is one error"
//}
