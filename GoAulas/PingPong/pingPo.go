package main

import (
	"fmt"
	"time"
)

func ping(p chan string) {
	for i := 0; i <= 2; i++ {
		p <- "ping"

	}
}

func pong(p chan string) {
	for i := 0; i <= 2; i++ {

		p <- "pong"
	}
}

func exibir(p chan string) {

	for {

		pings := <-p

		fmt.Println(pings)
		time.Sleep(time.Second * 1)

	}

}

func main() {

	p := make(chan string)

	go ping(p)
	go exibir(p)
	go pong(p)

	var entrada string
	fmt.Scanln(&entrada)

}
