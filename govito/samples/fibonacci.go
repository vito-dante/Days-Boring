package main

import "fmt"

func main() {
	var a, b, c int
	a = 0
	c, b = 1, 1

	fmt.Printf("%d \n%d \n", a, b)
	for i := 1; i < 5; i++ {
		fmt.Println(c)
		a = b + c
		b = c + a
		c = a + b
		fmt.Println(a)
		fmt.Println(b)
	}
}
