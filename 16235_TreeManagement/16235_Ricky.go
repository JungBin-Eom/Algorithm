package main

import (
	"fmt"
)

type treeSlice []Tree

type Tree struct {
	x, y int
}

type area struct {
	nutrient int
	trees    []treeSlice
}

var N, M, K int
var moveX, moveY []int

// func spring(areas [][]area) [][]area {
// 	for i := 0; i < N; i++ {
// 		for j := 0; j < N; j++ {
// 			for k, tree := range areas[i][j].trees {
// 				if areas[i][j].nutrient >= tree.age {
// 					areas[i][j].nutrient -= tree.age
// 					areas[i][j].trees[k].age++
// 					areas[i][j].trees[k].live = true
// 				}
// 			}
// 		}
// 	}
// 	fmt.Println("====봄 후 areas 확인=========")
// 	for j := 0; j < N; j++ {
// 		fmt.Println(areas[j])
// 	}
// 	fmt.Println("=============================")
// 	fmt.Println()
// 	return areas
// }

// func summer(areas [][]area) [][]area {
// 	for i := 0; i < N; i++ {
// 		for j := 0; j < N; j++ {
// 			dieIndex := 999
// 			for k, tree := range areas[i][j].trees {
// 				if !tree.live {
// 					areas[i][j].nutrient += tree.age / 2
// 					if k < dieIndex {
// 						dieIndex = k
// 					}
// 				} else {
// 					areas[i][j].trees[k].live = false
// 				}
// 			}
// 			if dieIndex != 999 {
// 				areas[i][j].trees = areas[i][j].trees[:dieIndex]
// 			}
// 		}
// 	}
// 	fmt.Println("====여름 후 areas 확인=========")
// 	for j := 0; j < N; j++ {
// 		fmt.Println(areas[j])
// 	}
// 	fmt.Println("=============================")
// 	fmt.Println()
// 	return areas
// }

// func fall(areas [][]area) [][]area {
// 	for i := 0; i < N; i++ {
// 		for j := 0; j < N; j++ {
// 			for _, tree := range areas[i][j].trees {
// 				if tree.age%5 == 0 {
// 					for k := 0; k < 8; k++ {
// 						if i+moveX[k] >= 0 && i+moveX[k] < N && j+moveY[k] >= 0 && j+moveY[k] < N {
// 							areas[i+moveX[k]][j+moveY[k]].trees = append([]Tree{Tree{i + moveX[k], j + moveY[k], 1, false}}, areas[i+moveX[k]][j+moveY[k]].trees...)
// 						}
// 					}
// 				}
// 			}
// 		}
// 	}
// 	fmt.Println("====가을 후 areas 확인=========")
// 	for j := 0; j < N; j++ {
// 		fmt.Println(areas[j])
// 	}
// 	fmt.Println("=============================")
// 	fmt.Println()
// 	return areas
// }

// func winter(areas [][]area, nutrients [][]int) [][]area {
// 	for i := 0; i < N; i++ {
// 		for j := 0; j < N; j++ {
// 			areas[i][j].nutrient += nutrients[i][j]
// 		}
// 	}
// 	fmt.Println("====겨울 후 areas 확인=========")
// 	for j := 0; j < N; j++ {
// 		fmt.Println(areas[j])
// 	}
// 	fmt.Println("=============================")
// 	fmt.Println()
// 	return areas
// }

func springAndSummer(areas [][]area) [][]area {
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			for k, treeArray := range areas[i][j].trees { // k가 현재 treeArray에 속한 나무들의 나이
				if k != 0 && areas[i][j].nutrient >= k*len(treeArray) && len(treeArray) != 0 { // treeArray들이 모두 양분을 섭취할 만큼 양분 있음
					fmt.Println(i, j, "에 있는", k, "살 나무들 영양분 버억")
					areas[i][j].nutrient -= k * len(treeArray)
				} else {
					areas[i][j].nutrient += (k / 2) * len(treeArray)
					areas[i][j].trees[k] = treeSlice{}
				}
			}
			for k := len(areas[i][j].trees) - 2; k >= 0; k-- {
				if len(areas[i][j].trees[k]) != 0 {
					fmt.Println(i, j, "에 있는", k, "살 나무는 나이가 자랍니다")
					areas[i][j].trees[k+1] = append(areas[i][j].trees[k+1], areas[i][j].trees[k]...)
					areas[i][j].trees[k] = treeSlice{}
					// fmt.Println(areas)
				}
			}
		}
	}
	fmt.Println("====봄,여름 후 areas 확인=========")
	for j := 0; j < N; j++ {
		fmt.Println(areas[j])
	}
	fmt.Println("=============================")
	fmt.Println()
	return areas
}

func fallAndWinter(areas [][]area, nutrients [][]int) [][]area {
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			areas[i][j].nutrient += nutrients[i][j]
			for index, _ := range areas[i][j].trees { // index가 나이
				if index != 0 && index%5 == 0 && len(areas[i][j].trees) != 0 {
					for k := 0; k < 8; k++ {
						if i+moveX[k] >= 0 && i+moveX[k] < N && j+moveY[k] >= 0 && j+moveY[k] < N {
							for l := 0; l < len(areas[i][j].trees[index]); l++ {
								areas[i+moveX[k]][j+moveY[k]].trees[1] = append(areas[i+moveX[k]][j+moveY[k]].trees[1], Tree{i + moveX[k], j + moveY[k]})
							}
						}
					}
				}
			}
		}
	}
	fmt.Println("====가을, 겨울 후 areas 확인=========")
	for j := 0; j < N; j++ {
		fmt.Println(areas[j])
	}
	fmt.Println("=============================")
	fmt.Println()
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
			areas[i][j].trees = make([]treeSlice, 10)
		}
	}

	for i := 0; i < M; i++ {
		var x, y, age int
		fmt.Scan(&x, &y, &age)
		areas[x-1][y-1].trees[age] = append(areas[x-1][y-1].trees[age], Tree{x - 1, y - 1})
	}

	// fmt.Println("====입력 후 areas 확인=========")
	// for j := 0; j < N; j++ {
	// 	fmt.Println(areas[j])
	// }
	// fmt.Println("=============================")
	// fmt.Println()

	// for i := 0; i < N; i++ {
	// 	for j := 0; j < N; j++ {
	// 		if len(areas[i][j].trees) > 1 {
	// 			sort.Slice(areas[i][j].trees, func(n, m int) bool {
	// 				return areas[i][j].trees[n].age < areas[i][j].trees[m].age
	// 			})
	// 		}
	// 	}
	// }

	for i := 0; i < K; i++ {
		areas = fallAndWinter(springAndSummer(areas), nutrients)
		//areas = winter(fall(summer(spring(areas))), nutrients)
		fmt.Println("한해가 지났습니다.")
		fmt.Println()
	}

	var result int
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			for k := 1; k < 10; k++ {
				result += len(areas[i][j].trees[k])
			}
		}
	}

	fmt.Println(result)
}
