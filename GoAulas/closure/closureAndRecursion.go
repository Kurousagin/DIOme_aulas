package main 

import "fmt"

func main(){
	x := 0 

	numero := func() int{
		
		x++
		return(x)
	}	

fmt.Println(numero())
fmt.Println(numero())
fmt.Println(fatorial(2))
}


func fatorial (x int ) int {

	if x == 0 {
		
	return 1

	}
	return x * fatorial(x-1)
}


