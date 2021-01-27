package main

import (
	"fmt"
	"sort"
)

type Tree struct {
	x, y, age int
	live      bool
}

type area struct {
	nutrient int
	trees    []Tree
}

var N, M, K int
var moveX, moveY []int

func spring(areas [][]area) [][]area {
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			for k, tree := range areas[i][j].trees {
				if areas[i][j].nutrient >= tree.age {
					areas[i][j].nutrient -= tree.age
					areas[i][j].trees[k].age++
					areas[i][j].trees[k].live = true
				}
			}
		}
	}
	// fmt.Println("====spring 직후 areas 확인=========")
	// for j := 0; j < N; j++ {
	// 	fmt.Println(areas[j])
	// }
	// fmt.Println("=============================")
	return areas
}

func summer(areas [][]area) [][]area {
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			dieIndex := 999
			for k, tree := range areas[i][j].trees {
				if !tree.live {
					areas[i][j].nutrient += tree.age / 2
					if k < dieIndex {
						dieIndex = k
					}
				} else {
					areas[i][j].trees[k].live = false
				}
			}
			if dieIndex != 999 {
				areas[i][j].trees = areas[i][j].trees[:dieIndex]
			}
		}
	}
	// fmt.Println("===summer 직후 areas 확인=========")
	// for j := 0; j < N; j++ {
	// 	fmt.Println(areas[j])
	// }
	// fmt.Println("=============================")
	return areas
}

func fall(areas [][]area) [][]area {
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			for _, tree := range areas[i][j].trees {
				if tree.age%5 == 0 {
					for k := 0; k < 8; k++ {
						if i+moveX[k] >= 0 && i+moveX[k] < N && j+moveY[k] >= 0 && j+moveY[k] < N {
							areas[i+moveX[k]][j+moveY[k]].trees = append([]Tree{Tree{i + moveX[k], j + moveY[k], 1, false}}, areas[i+moveX[k]][j+moveY[k]].trees...)
						}
					}
				}
			}
		}
	}
	// fmt.Println("====fall 직후 areas 확인=========")
	// for j := 0; j < N; j++ {
	// 	fmt.Println(areas[j])
	// }
	// fmt.Println("=============================")
	return areas
}

func winter(areas [][]area, nutrients [][]int) [][]area {
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			areas[i][j].nutrient += nutrients[i][j]
		}
	}
	// fmt.Println("====winter 직후 areas 확인=========")
	// for j := 0; j < N; j++ {
	// 	fmt.Println(areas[j])
	// }
	// fmt.Println("=============================")
	return areas
}

func main() {

	moveX = []int{-1, -1, -1, 0, 0, 1, 1, 1}
	moveY = []int{-1, 0, 1, -1, 1, -1, 0, 1}
	fmt.Scan(&N, &M, &K)

	areas := make([][]area, N)
	nutrients := make([][]int, N)
	for i := 0; i < N; i++ {
		areas[i] = make([]area, N)
		nutrients[i] = make([]int, N)
		for j := 0; j < N; j++ {
			var nutrient int
			fmt.Scan(&nutrient)
			areas[i][j].nutrient = 5
			nutrients[i][j] = nutrient
		}
	}

	for i := 0; i < M; i++ {
		var x, y, age int
		fmt.Scan(&x, &y, &age)
		areas[x-1][y-1].trees = append(areas[x-1][y-1].trees, Tree{x - 1, y - 1, age, false})
	}

	// fmt.Println("====입력 직후 areas 확인=========")
	// for j := 0; j < N; j++ {
	// 	fmt.Println(areas[j])
	// }
	// fmt.Println("=============================")

	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			if len(areas[i][j].trees) > 1 {
				sort.Slice(areas, func(n, m int) bool {
					return areas[i][j].trees[n].age < areas[i][j].trees[m].age
				})
			}
		}
	}

	for i := 0; i < K; i++ {
		areas = winter(fall(summer(spring(areas))), nutrients)
		// fmt.Println("한해가 지났습니다.")
		// fmt.Println()
	}

	var result int
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			result += len(areas[i][j].trees)
		}
	}

	fmt.Println(result)
}
