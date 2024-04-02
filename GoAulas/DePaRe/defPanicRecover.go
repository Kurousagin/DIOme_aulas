// panic: usado para erros 
// recover interrompe o panic 


package main 

import "fmt"

func dayOne(){

fmt.Println("Segunda")

}


func dayTwo(){

fmt.Println("Terça")


}


func main(){


	defer func () {
	
	x := recover()
	fmt.Println(x)
	}()
	panic("Pânico")



	//// usado para iverter a ordem de execução?
	defer
	dayTwo()
	dayOne()
}



