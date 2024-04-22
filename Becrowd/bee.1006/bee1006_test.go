package main

import "testing"

func TestMedia(t *testing.T) {
	teste := media(5,6,9)
	resultado := 10.0

	if teste != float64(resultado) {
		t.Error("Valor esperado:", resultado, "Valor retornado", teste)

	}

}
