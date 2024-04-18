package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
)

type Response struct {
	name    string    "json: 'name'"
	Pokemon []Pokemon "json: 'pokemon_entries'"
}

type Pokemon struct {
	numero  int     "json: 'entry_number'"
	especie Species "json: 'pokemon_species'"
}

type Species struct {
	name string "json: 'name'"
}

func main() {

	response, err := http.Get("http://pokeapi.co/api/v2/pokedex/kanto")

	if err != nil {
		fmt.Print(err.Error())
		os.Exit(1)
	}

	responseData, err := io.ReadAll(response.Body)

	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(string(responseData))

	var responseObject Response
	json.Unmarshal(responseData, &responseObject)
	fmt.Println(responseObject.name)
	fmt.Println((responseObject.Pokemon))

	for _, pokemon := range responseObject.Pokemon {
		fmt.Println(pokemon.especie.name)
	}

}
