package main
 
import (
    "fmt"
)
 
func main() {

var numeroFunc, horasTrabalhadas int64
var valorHora float64

 
 fmt.Scan(&numeroFunc)
 fmt.Scan(&horasTrabalhadas)
 fmt.Scan(&valorHora)
  calculoSalario := float64(horasTrabalhadas) * valorHora
 
 
fmt.Printf("NUMBER = %v\nSALARY = U$ %.2f\n", numeroFunc, calculoSalario)
}
