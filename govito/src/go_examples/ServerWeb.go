package main

import (
	"fmt"
	"net/http"
)

type message struct {
	msg string
}
func(m message) ServeHTTP(w http.ResponseWriter, r *http.Request){
	fmt.Fprint(w, m.msg)
}

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprint(w, "<h1>hello vito from goland IDE</h1>")
	})

	mux.Handle("/test", message{"vito marca my struct"})
	http.ListenAndServe(":8080",mux)
}
