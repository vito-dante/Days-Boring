package main

import (
	"fmt"
)

func main() {

	function_anonimate := func(name string) string {
		return "Hello " + name
	}
	message := test1("vito", "marca", function_anonimate)
	fmt.Println(message)
}

func test1(name string, name2 string, myfunc func(string) string) string {
	return "hello function -> " + myfunc(name) + " " + myfunc(name2)
}

//expect message
//hello function -> Hello vito, Hello marca
