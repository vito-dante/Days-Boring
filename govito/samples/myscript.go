 package main

import (
    "fmt"
    "os"
)

func main() {
    var s, sep string
    for i := 1; i < len(os.Args); i++{
        s += sep + os.Args[i]
        sep = " "
        fmt.Println(os.Args[i])
    }
    fmt.Println(s)
    //fmt.Println(os.Args)
    //for i:=0; i<10; i++ {
        //fmt.Println(i)
    //}

    var consolasGame [3]string
    consolasGame[0] = "PS3"
    consolasGame[1] = "xbox one"
    consolasGame[2] = "nintendo"
    for i:=0; i<len(consolasGame); i++{
         fmt.Println(consolasGame[i])
    }

    juegos := []string{ "call of duty", "need for speed", "Pro evolution" }
    for i:=0; i<len(juegos); i++ {
        fmt.Println(juegos[i])
    }

    for pos, char := range"aΦx"{
         fmt.Printf("character '%c' starts at byte position  %d\n", char, pos)
    }

}

