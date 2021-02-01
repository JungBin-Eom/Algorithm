package main

import (
	"fmt"
	"sort"
)

type tree struct {
	x, y, age int
}

var N, M, K int
var moveX, moveY []int

func main() {
	moveX = []int{-1, -1, -1, 0, 0, 1, 1, 1}
	moveY = []int{-1, 0, 1, -1, 1, -1, 0, 1}
	fmt.Scan(&N, &M, &K)

	area := make([][]int, N)
	S2D2 := make([][]int, N)
	addition := make([][]int, N)
	var treeSlice []tree
	var alive []tree
	var die []tree
	for i := 0; i < N; i++ {
		area[i] = make([]int, N)
		addition[i] = make([]int, N)
		S2D2[i] = make([]int, N)
		for j := 0; j < N; j++ {
			var nutrient int
			fmt.Scan(&nutrient)
			area[i][j] = 5
			S2D2[i][j] = nutrient
		}
	}

	for i := 0; i < M; i++ {
		var x, y, age int
		fmt.Scan(&x, &y, &age)
		treeSlice = append(treeSlice, tree{x - 1, y - 1, age})
	}

	for year := 0; year < K; year++ {
		sort.Slice(treeSlice, func(i, j int) bool {
			return treeSlice[i].age < treeSlice[j].age
		})

		// 봄(나이만큼 양분을 섭취)
		for _, t := range treeSlice {
			if area[t.x][t.y] >= t.age {
				area[t.x][t.y] -= t.age
				alive = append(alive, tree{t.x, t.y, t.age + 1})
			} else {
				die = append(die, tree{t.x, t.y, t.age})
			}
		}
		treeSlice = []tree{}

		// 여름(죽은 나무 양분 추가)
		for _, t := range die {
			area[t.x][t.y] += t.age / 2
		}
		die = []tree{}

		// 가을(나이가 5의 배수인 나무는 번식)
		for _, t := range alive {
			if t.age%5 == 0 {
				for k := 0; k < 8; k++ {
					var tempX, tempY int
					tempX = t.x + moveX[k]
					tempY = t.y + moveY[k]
					if tempX >= 0 && tempX < N && tempY >= 0 && tempY < N {
						treeSlice = append(treeSlice, tree{tempX, tempY, 1})
					}
				}
			}
			treeSlice = append(treeSlice, t)
		}
		alive = []tree{}

		// 겨울(S2D2가 양분 추가)
		for i := 0; i < N; i++ {
			for j := 0; j < N; j++ {
				area[i][j] += S2D2[i][j]
			}
		}
		// fmt.Println("========", year+1, "년후=======")
		// fmt.Println("현재 나무")
		// fmt.Println(treeSlice)
		// fmt.Println()
		// fmt.Println("양분")
		// for i := 0; i < N; i++ {
		// 	fmt.Println(area[i])
		// }
		// fmt.Println("======================")
	}

	result := len(treeSlice)

	fmt.Println(result)
}
