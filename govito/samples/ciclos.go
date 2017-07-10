package main

import "fmt"

func main() {
    i:=0
    for {
        i++
        fmt.Println(i)
        if(i == 10){
            break
        }
        if (i == 3){
            fmt.Println("ya entre al continue")
            continue
            fmt.Println("Esta linea ya no se imprime por que hay un continue arriba")
        }

    }
}

