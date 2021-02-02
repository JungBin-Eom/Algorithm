package main

import (
	"fmt"
	"strconv"
)

var board [][]int
var moveX, moveY []int
var result map[string]bool

func search(x, y int, before string) {
	for k := 0; k < 4; k++ {
		newX := x + moveX[k]
		newY := y + moveY[k]
		if newX >= 0 && newX < 5 && newY >= 0 && newY < 5 {
			// fmt.Println("befX:", x, " befY: ", y, before)
			newString := before + strconv.Itoa(board[newX][newY])
			// fmt.Println("newX:", newX, " newY: ", newY, newString)
			if len(newString) == 6 {
				_, ok := result[newString]
				if !ok {
					result[newString] = true
				}
				// return
			} else {
				search(newX, newY, newString)
			}
		}
	}
}

func main() {
	moveX = []int{-1, 0, 1, 0}
	moveY = []int{0, -1, 0, 1}
	result = make(map[string]bool)
	board = make([][]int, 5)
	for i := 0; i < 5; i++ {
		board[i] = make([]int, 5)
		for j := 0; j < 5; j++ {
			var digit int
			fmt.Scan(&digit)
			board[i][j] = digit
		}
	}

	for i := 0; i < 5; i++ {
		for j := 0; j < 5; j++ {
			var number string
			// fmt.Println("============================")
			// fmt.Println("Start x: ", i, "Start y: ", j)
			number = strconv.Itoa(board[i][j])
			search(i, j, number)
			// fmt.Println("============================")
		}
	}

	// fmt.Println(result)
	fmt.Println(len(result))
}
