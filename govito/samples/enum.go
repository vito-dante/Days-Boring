package main

import "fmt"

func main() {
	const (
		foo  = iota
		foo2 = iota
		foo3 = iota
		foo4 = iota
	)
	fmt.Println(foo)
	fmt.Println(foo2)
	fmt.Println(foo3)
	fmt.Println(foo4)
}
