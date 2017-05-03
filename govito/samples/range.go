package main

import "fmt"

func main() {
	//var consolas []string
	//consolas = []string{"ps3", "xbox", "nintendo"}
	var something int
	consolas := []string{"ps3", "xbox", "nintendo"}
	for _, mivalor := range consolas {
		fmt.Println(mivalor)
	}
	another := some
	fmt.Println(another())
}

func some() string {
	return "something"
}
