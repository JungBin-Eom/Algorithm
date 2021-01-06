package main

import (
	"Algorithm/16236_BabyShark/queue"
	"fmt"
)

type sea [][]int

func (s sea) String() string {
	len := len(s)
	var str string
	for i := 0; i < len; i++ {
		for j := 0; j < len; j++ {
			str = str + fmt.Sprint(s[i][j]) + " "
		}
		if i != len-1 {
			str += "\n"
		}
	}
	return str
}

func main() {
	var N, fish, sharkX, sharkY int
	// count := 0
	// shark := 2
	q := queue.NewQueue()
	fmt.Scanln(&N)

	mySea := make(sea, N)
	for i := 0; i < N; i++ {
		mySea[i] = make([]int, N)
	}

	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			node := queue.Node{i, j}
			q.Enque(&node)
			fmt.Scan(&fish)
			if fish == 9 {
				sharkX = i
				sharkY = j
			}
			mySea[i][j] = fish
		}
	}
	fmt.Println(mySea)
	fmt.Println("Shark is at X: ", sharkX, " Y: ", sharkY)
}
