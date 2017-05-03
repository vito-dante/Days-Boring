package main

import (
    "fmt"
    "strconv"
)

func main(){
    edad :="22"
    //conversion de int to str
    //edad_str := strconv.Itoa(edad)
    //conversion de str to int
    edad_int,_ := strconv.Atoi(edad)
    //fmt.Println("mi edad es "+edad_str)
    fmt.Println(33+edad_int)

}
