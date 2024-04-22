package main

import (
    "fmt"
)

func main() {
    var num1, num2 float64
    var operador string

    fmt.Println("Bem-vindo")
    fmt.Println("Digite o primeiro número:")
    fmt.Scanln(&num1)

    fmt.Println("Digite o operador (+, -, *, /):")
    fmt.Scanln(&operador)

    fmt.Println("Digite o segundo número:")
    fmt.Scanln(&num2)

    resultado := calcular(num1, num2, operador)
    fmt.Printf("Resultado: %.2f\n", resultado)
}

func calcular(num1, num2 float64, operador string) float64 {
    var resultado float64
    switch operador {
    case "+":
        resultado = num1 + num2
    case "-":
        resultado = num1 - num2
    case "*":
        resultado = num1 * num2
    case "/":
        if num2 != 0 {
            resultado = num1 / num2
        } else {
            fmt.Println("Erro: divisão por zero!")
            return 0
        }
    default:
        fmt.Println("Operador inválido!")
        return 0
    }
    return resultado
}
