package main

import "fmt"

func main() {
	exam := func(name string) string {
		return "Hello " + name
	}
	fmt.Println(exam("dante"))
}
