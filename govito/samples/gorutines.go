package main

import (
	"fmt"
	"strings"
	"time"
)

func main() {
	go mi_nombre_lento("Vito Marca")
	fmt.Println("Waiting ....")
	go func() {
		var variable string
		fmt.Scanln(&variable)
		fmt.Println("DESDE LA FUNCION " + variable)
	}()
	var variable string
	fmt.Scanln(&variable)
	fmt.Println(" DESDE EL METHOD" + variable)
}

func mi_nombre_lento(name string) {
	letras := strings.Split(name, "")
	for _, letra := range letras {
		time.Sleep(1000 * time.Millisecond)
		fmt.Println(letra)
	}

}
