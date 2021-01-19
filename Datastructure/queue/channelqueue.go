package main

import "fmt"

type Queue struct {
	items chan int
}

func (q *Queue) Push(value int) {
	q.items <- value
}

func (q *Queue) Pop() int {
	return <-q.items
}

func main() {
	q := Queue{items: make(chan int, 1000)}
	q.Push(1)
	close(q.items)

	fail := 100

	defer func() {
		fmt.Println(fail)
		if err := recover(); err != nil {
			fmt.Println("끝!")
		}
	}()

	fmt.Println(q.Pop())
	fmt.Println(q.Pop())
}
