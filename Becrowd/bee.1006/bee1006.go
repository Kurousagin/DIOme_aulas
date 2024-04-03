package main

import (
	"fmt"
)

func main() {
	var A,B,C float64
	
	fmt.Scan(&A)
	fmt.Scan(&B)
	fmt.Scan(&C)

	
	media := (A*2 + B*3 + C*5) / (2 + 3 + 5)
	
	fmt.Printf("MEDIA = %.1f\n", media)
	

}
