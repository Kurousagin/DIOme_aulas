package main

import (
	"fmt"
)

func main() {

	var nameFuncionario string
	var salarioFixo, totalVendas float64

	fmt.Scan(&nameFuncionario)
	fmt.Scan(&salarioFixo)
	fmt.Scan(&totalVendas)
	salarioFinal := salarioFixo + ((totalVendas * 15) / 100)

	fmt.Printf("TOTAL = %.2f\n", salarioFinal)

}
