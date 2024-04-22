package main

import (
	"fmt"
)

func main() {
	media(1,4,5)
}

func media(A float64, B float64, C float64) float64 {

	fmt.Scan(&A)
	fmt.Scan(&B)
	fmt.Scan(&C)

	media := (A*2 + B*3 + C*5) / (2 + 3 + 5)

	fmt.Printf("MEDIA = %.1f\n", media)
	return media
}
