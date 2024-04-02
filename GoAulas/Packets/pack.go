package main 

import (
	//"fmt"
	//"strings"
	"io"
	"log"
	"os"
)

func main(){
	
	if _, err := io.WriteString(os.Stdout, "hello world"); err != nil{
	log.Fatal(err)
	}
	//fmt.Println(strings.Contains("computador","dor"))



}
