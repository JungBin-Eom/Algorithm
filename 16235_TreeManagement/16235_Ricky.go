package main

import (
	"fmt"
)

type tree struct {
	age, count int
}

type allAgeTrees []tree

var N, M, K int
var moveX, moveY []int

func main() {
	moveX = []int{-1, -1, -1, 0, 0, 1, 1, 1}
	moveY = []int{-1, 0, 1, -1, 1, -1, 0, 1}
	fmt.Scan(&N, &M, &K)

	area := make([][]int, N)
	S2D2 := make([][]int, N)
	addition := make([][]int, N)
	treeSlice := make([][]allAgeTrees, N)
	for i := 0; i < N; i++ {
		area[i] = make([]int, N)
		addition[i] = make([]int, N)
		S2D2[i] = make([]int, N)
		treeSlice[i] = make([]allAgeTrees, N)
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
		treeSlice[x-1][y-1] = append(treeSlice[x-1][y-1], tree{age, 1})
	}

	for year := 0; year < K; year++ {
		for i := 0; i < N; i++ {
			for j := 0; j < N; j++ {
				if len(treeSlice[i][j]) != 0 {
					var alive, die, dieIndex int
					dieIndex = 999
					for index, t := range treeSlice[i][j] {
						if area[i][j] >= t.age*t.count { // 현재 age의 나무가 모두 섭취할 만큼의 양분이 있는 경우
							area[i][j] -= t.age * t.count
							treeSlice[i][j][index].age++
						} else if area[i][j]/t.age > 0 { // 모든 나무가 양분을 섭취할 수 없는 경우(몇그루는 가능)
							alive = area[i][j] / t.age      // 섭취할 수 있는 나무의 최대 수
							die = t.count - alive           // 나머지는 다 죽음
							area[i][j] -= alive * t.age     // 봄(양분 섭취)
							area[i][j] += (t.age / 2) * die // 여름
							treeSlice[i][j][index].age++
							treeSlice[i][j][index].count = alive
							// treeSlice[i][j] = treeSlice[i][j][:index+1]
							// break
							if index < dieIndex {
								dieIndex = index + 1
							}
						} else if area[i][j]/t.age == 0 { // 나무 모두 양분 섭취 불가능
							area[i][j] += (t.age / 2) * t.count
							treeSlice[i][j][index].count = 0
							// treeSlice[i][j] = treeSlice[i][j][:index]
							// break
							if index < dieIndex {
								dieIndex = index
							}
						}
					}
					if dieIndex != 999 {
						treeSlice[i][j] = treeSlice[i][j][:dieIndex]
					}
				}
			}
		}
		for i := 0; i < N; i++ {
			for j := 0; j < N; j++ {
				if len(treeSlice[i][j]) != 0 {
					for _, t := range treeSlice[i][j] {
						if t.age%5 == 0 { // 번식
							for k := 0; k < 8; k++ {
								if i+moveX[k] >= 0 && i+moveX[k] < N && j+moveY[k] >= 0 && j+moveY[k] < N {
									addition[i+moveX[k]][j+moveY[k]] += t.count
								}
							}
						}
					}
				}
				area[i][j] += S2D2[i][j] // 겨울 양분 추가
			}
		}

		for i := 0; i < N; i++ {
			for j := 0; j < N; j++ {
				if addition[i][j] != 0 {
					treeSlice[i][j] = append([]tree{{1, addition[i][j]}}, treeSlice[i][j]...)
					addition[i][j] = 0
				}
			}
		}
		fmt.Println("========", year+1, "년후=======")
		fmt.Println("현재 나무")
		for i := 0; i < N; i++ {
			fmt.Println(treeSlice[i])
		}
		fmt.Println()
		fmt.Println("양분")
		for i := 0; i < N; i++ {
			fmt.Println(area[i])
		}
		fmt.Println("======================")
	}

	var result int
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			if len(treeSlice[i][j]) != 0 {
				for _, t := range treeSlice[i][j] {
					result += t.count
				}
			}
		}
	}

	fmt.Println(result)
}
