package main

import (
	"fmt"
	"net/http"
)

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "<h1>Hi World</h1>")
	})
	mux.HandleFunc("/test", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "<h1>my test</h1>")
	})
	mux.HandleFunc("/another", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "<h1>this is another test</h1>")
	})

	http.ListenAndServe(":8080", mux)
}
