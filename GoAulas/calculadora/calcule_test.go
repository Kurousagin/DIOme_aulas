package main

import (
    "testing"
)

func TestCalcular(t *testing.T) {
    // Teste de adição
    if resultado := calcular(2, 3, "+"); resultado != 5 {
        t.Errorf("Erro ao somar 2 e 3. Esperado: 5, Obtido: %f", resultado)
    }

    // Teste de subtração
    if resultado := calcular(5, 3, "-"); resultado != 2 {
        t.Errorf("Erro ao subtrair 3 de 5. Esperado: 2, Obtido: %f", resultado)
    }

    // Teste de multiplicação
    if resultado := calcular(2, 3, "*"); resultado != 6 {
        t.Errorf("Erro ao multiplicar 2 e 3. Esperado: 6, Obtido: %f", resultado)
    }

    // Teste de divisão
    if resultado := calcular(6, 3, "/"); resultado != 2 {
        t.Errorf("Erro ao dividir 6 por 3. Esperado: 2, Obtido: %f", resultado)
    }

    // Teste de divisão por zero
    if resultado := calcular(6, 0, "/"); resultado != 0 {
        t.Errorf("Erro: Divisão por zero. Esperado: 0, Obtido: %f", resultado)
    }

    // Teste de operador inválido
    if resultado := calcular(6, 3, "%"); resultado != 0 {
        t.Errorf("Erro: Operador inválido. Esperado: 0, Obtido: %f", resultado)
    }
}
