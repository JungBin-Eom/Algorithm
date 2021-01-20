package main

import (
	"fmt"
)

type fish struct {
	x, y, fishNum, direction int
}

func (f fish) String() string {
	return fmt.Sprintf("(%d, %d) %d번(%d)", f.x, f.y, f.fishNum, f.direction)
}

type Element struct {
	fishes                              []fish
	area                                [][]fish
	sharkX, sharkY, sharkDirection, eat int
}

type Queue struct {
	element chan Element
	size    int
}

func (q *Queue) Push(e Element) {
	q.element <- e
	q.size++
}

func (q *Queue) Pop() (Element, bool) {
	if q.size == 0 {
		return Element{}, false
	} else {
		q.size--
		return <-q.element, true
	}
}

func main() {
	// fmt.Printf("\n\n\n\n\n\n\n")
	var fishNum, direction int
	var sharkX, sharkY, sharkDirection, eat, bestEat int

	fishes := make([]fish, 16)
	area := make([][]fish, 4)
	for i := 0; i < 4; i++ {
		area[i] = make([]fish, 4)
	}

	for i := 0; i < 4; i++ {
		for j := 0; j < 4; j++ {
			fmt.Scan(&fishNum, &direction)
			area[i][j] = fish{i, j, fishNum, direction}
			fishes[fishNum-1] = fish{i, j, fishNum, direction}
			// fmt.Println(fishes)
		}
	}

	// 상어 입장
	sharkDirection = area[0][0].direction
	sharkX, sharkY = 0, 0
	eat += area[0][0].fishNum
	fishes[area[0][0].fishNum-1] = fish{}
	area[0][0].fishNum = 0
	area[0][0].direction = 0

	// queue 생성
	q := Queue{element: make(chan Element, 1000)}
	newElement := Element{fishes, area, sharkX, sharkY, sharkDirection, eat}
	q.Push(newElement)

	for {
		nowElement, ok := q.Pop()
		if ok == false {
			break
		} else {
			copy(fishes, nowElement.fishes)
			copy(area, nowElement.area)
			eat = nowElement.eat
			sharkX = nowElement.sharkX
			sharkY = nowElement.sharkY
			sharkDirection = nowElement.sharkDirection
			if eat > bestEat {
				bestEat = eat
			}
			// fmt.Println("지금 상태의 상어는 ", eat, "만큼 먹었고 지금까지 최대값은 ", bestEat, "입니다.")

			// 물고기 이동
			for i := 0; i < 16; i++ {
				var newX, newY, rotateCount int

				// fmt.Println("물고기 목록: ", fishes)
				if fishes[i].direction == 0 {
					// fmt.Println(i+1, "번째 물고기는 이미 먹혔으므로 이동하지 않습니다.")
					// fmt.Println("========")
					rotateCount = 8
				} else {
					// fmt.Println(i+1, "번 물고기 이동")
				}
				for rotateCount != 8 {
					switch fishes[i].direction {
					case 1:
						newX, newY = fishes[i].x-1, fishes[i].y
					case 2:
						newX, newY = fishes[i].x-1, fishes[i].y-1
					case 3:
						newX, newY = fishes[i].x, fishes[i].y-1
					case 4:
						newX, newY = fishes[i].x+1, fishes[i].y-1
					case 5:
						newX, newY = fishes[i].x+1, fishes[i].y
					case 6:
						newX, newY = fishes[i].x+1, fishes[i].y+1
					case 7:
						newX, newY = fishes[i].x, fishes[i].y+1
					case 8:
						newX, newY = fishes[i].x-1, fishes[i].y+1
					}
					if newX < 0 || newX > 3 || newY < 0 || newY > 3 { // 범위를 벗어나는 경우
						fishes[i].direction++
						area[fishes[i].x][fishes[i].y].direction++
						rotateCount++
						if fishes[i].direction == 9 {
							fishes[i].direction = 1
							area[fishes[i].x][fishes[i].y].direction = 1
						}
					} else if newX == sharkX && newY == sharkY { // 상어를 만나는 경우
						fishes[i].direction++
						area[fishes[i].x][fishes[i].y].direction++
						rotateCount++
						if fishes[i].direction == 9 {
							fishes[i].direction = 1
							area[fishes[i].x][fishes[i].y].direction = 1
						}
					} else { // 물고기 만나거나 빈칸
						tempX := fishes[i].x
						tempY := fishes[i].y
						if area[newX][newY].fishNum == 0 {
							// fmt.Println("빈칸으로 이동")
							fishes[i].x, fishes[i].y = newX, newY
						} else {
							// fmt.Println(area[newX][newY].fishNum, "번 물고기와 교체 ")
							fishes[area[newX][newY].fishNum-1].x, fishes[i].x = fishes[i].x, newX
							fishes[area[newX][newY].fishNum-1].y, fishes[i].y = fishes[i].y, newY
						}

						// tempX = fishes[area[newX][newY].fishNum-1].x
						// fishes[area[newX][newY].fishNum-1].x = fishes[i].x
						// fishes[i].x = tempX

						// tempY = fishes[area[newX][newY].fishNum-1].y
						// fishes[area[newX][newY].fishNum-1].y = fishes[i].y
						// fishes[i].y = tempY

						// fmt.Println("이동 전 area")
						// for k := 0; k < 4; k++ {
						// 	fmt.Println(area[k])
						// }

						// fmt.Println(area[newX][newY], "<=>", area[tempX][tempY])

						area[newX][newY], area[tempX][tempY] = area[tempX][tempY], area[newX][newY]
						area[newX][newY].x, area[tempX][tempY].x = area[tempX][tempY].x, area[newX][newY].x
						area[newX][newY].y, area[tempX][tempY].y = area[tempX][tempY].y, area[newX][newY].y

						// fmt.Println("이동 후 area")
						// for k := 0; k < 4; k++ {
						// 	fmt.Println(area[k])
						// }

						// fmt.Println("=========")

						break
					}
				}
			}

			// 상어 이동
			var newSharkX, newSharkY int
			for i := 1; i < 4; i++ { // i칸 이동하는 경우를 모두 구해야 함(최대 3칸)
				// fmt.Printf("상어가 %d방향으로 %d칸 이동합니다.\n", sharkDirection, i)
				switch sharkDirection {
				case 1:
					newSharkX, newSharkY = sharkX-i, sharkY
				case 2:
					newSharkX, newSharkY = sharkX-i, sharkY-i
				case 3:
					newSharkX, newSharkY = sharkX, sharkY-i
				case 4:
					newSharkX, newSharkY = sharkX+i, sharkY-i
				case 5:
					newSharkX, newSharkY = sharkX+i, sharkY
				case 6:
					newSharkX, newSharkY = sharkX+i, sharkY+i
				case 7:
					newSharkX, newSharkY = sharkX, sharkY+i
				case 8:
					newSharkX, newSharkY = sharkX-i, sharkY+i
				}
				if newSharkX < 0 || newSharkX > 3 || newSharkY < 0 || newSharkY > 3 { // 범위를 벗어나는 경우
					// do nothing
					// 상어가 이동하지 않습니다.
					// fmt.Println("상어가 범위를 벗어났습니다.")
				} else if area[newSharkX][newSharkY].fishNum == 0 { // 물고기가 없는 칸으로 갈 경우
					// do nothing
					// 상어가 이동하지 않습니다.
					// fmt.Println("상어가 물고기를 찾지 못했습니다.")
				} else { // 물고기 만나는 경우
					newDirection := area[newSharkX][newSharkY].direction
					newFishes := make([]fish, 16)
					copy(newFishes, fishes)
					newFishes[area[newSharkX][newSharkY].fishNum-1] = fish{}
					newArea := make([][]fish, 4)
					for j := 0; j < 4; j++ {
						newArea[j] = make([]fish, 4)
					}
					for j := 0; j < 4; j++ {
						copy(newArea[j], area[j])
					}
					newEat := eat + newArea[newSharkX][newSharkY].fishNum
					newArea[newSharkX][newSharkY].fishNum = 0
					newArea[newSharkX][newSharkY].direction = 0
					newElement := Element{newFishes, newArea, newSharkX, newSharkY, newDirection, newEat}
					q.Push(newElement)
				}
			}
		}
	}
	fmt.Println(bestEat)
}
