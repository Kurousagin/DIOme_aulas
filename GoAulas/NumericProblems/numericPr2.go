package main 
import "fmt"

func main(){
	x:=0
	y:=0
	for i:=1 ; i<=100 ; i++{
			
		if i%3 == 0 {
			x++
			fmt.Println("Pin")
		}else if i%5 == 0 {
			y++
			fmt.Println("Pan")
		}

	}

	fmt.Printf("foram ditas %vx Pin e %vx Pan",x,y)


}
	

