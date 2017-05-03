package main

import "fmt"

type usuario struct {
	nombre string
	email  string
}
type console struct {
	nombre string
	ram    int
	juegos []string
}

func llenarDatos() *console {
	return &console{"PLAY 4", 8, []string{"COD", "STREET FIGHTER", "GOD OF WAR"}}
}
func nuevoUsuario(name string) (*usuario, error) {
	return &usuario{name, "vitoallstarz@gmail.com"}, nil
}

func main() {
	//u, err := nuevoUsuario()
	//if err != nil {
	//fmt.Println(err)
	//}
	//fmt.Println(*u)

	//_,err = nuevoUsuario()
	//if err != nil {
	//fmt.Println(err)
	//return
	//}
	valor := llenarDatos()
	//fmt.Println(valor.juegos)
	for i := 0; i < len(valor.juegos); i++ {
		fmt.Println(valor.juegos[i])
	}

	for _, itemJuegos := range valor.juegos {
		fmt.Println(itemJuegos)
	}

}
