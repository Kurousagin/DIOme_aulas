package main

import (
	"encoding/json"
	"fmt"
	"io"
	"os"
	"strconv"
)

type Users struct {
	Users []User `json:"usuarios"`
}

type User struct {
	Nome   string `json:"name"`
	Age    int    `json:"age"`
	Tipo   string `json:"tipo"`
	Social Social `json:"social"`
}

type Social struct {
	Facebook  string `json:"facebook"`
	Instagram string `json:"instagram"`
}

func main() {
	jsonFile, err := os.Open("users.json")
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println("Arquivo aberto!")
	defer jsonFile.Close()

	byteValue, _ := io.ReadAll(jsonFile)

	var usuarios Users

	json.Unmarshal(byteValue, &usuarios)

	for i := 0; i < len(usuarios.Users); i++ {
		fmt.Println("Usuario tipo: " + usuarios.Users[i].Tipo)
		fmt.Println("Usuario idade: " + strconv.Itoa(usuarios.Users[i].Age))
	}

}
