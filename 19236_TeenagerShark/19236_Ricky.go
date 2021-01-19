package main

import (
	"fmt"
)

type fish struct {
	x, y, fishNum, direction int
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
			fishes = nowElement.fishes
			area = nowElement.area
			eat = nowElement.eat
			sharkX = nowElement.sharkX
			sharkY = nowElement.sharkY
			sharkDirection = nowElement.sharkDirection

			if eat > bestEat {
				bestEat = eat
			}
			// 물고기 이동
			for i := 0; i < 16; i++ {
				var newX, newY, rotateCount int

				fmt.Println(fishes)
				fmt.Println(i+1, "번째 물고기 이동")
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
					if newX < 0 || newX > 16 || newY < 0 || newY > 16 { // 범위를 벗어나는 경우
						fishes[i].direction++
						rotateCount++
						if fishes[i].direction == 9 {
							fishes[i].direction = 1
						}
					} else if newX == sharkX && newY == sharkY { // 상어를 만나는 경우
						fishes[i].direction++
						rotateCount++
						if fishes[i].direction == 9 {
							fishes[i].direction = 1
						}
					} else { // 물고기 만나거나 빈칸
						fmt.Println(area[newX][newY].fishNum, "번째 물고기와 교체 ", fishes[i], fishes[area[newX][newY].fishNum-1])

						// tempX = fishes[area[newX][newY].fishNum-1].x
						// fishes[area[newX][newY].fishNum-1].x = fishes[i].x
						// fishes[i].x = tempX

						// tempY = fishes[area[newX][newY].fishNum-1].y
						// fishes[area[newX][newY].fishNum-1].y = fishes[i].y
						// fishes[i].y = tempY

						fishes[area[newX][newY].fishNum-1].x, fishes[i].x = fishes[i].x, fishes[area[newX][newY].fishNum-1].x
						fishes[area[newX][newY].fishNum-1].y, fishes[i].y = fishes[i].y, fishes[area[newX][newY].fishNum-1].y

						fmt.Println("교체 후 ", fishes[i], fishes[area[newX][newY].fishNum-1])

						area[newX][newY], area[fishes[i].x][fishes[i].y] = area[fishes[i].x][fishes[i].y], area[newX][newY]

						fmt.Println(area)
						fmt.Println("=========")

						break
					}
				}
			}

			// 상어 이동
			var newSharkX, newSharkY int
			for i := 1; i < 4; i++ { // i칸 이동하는 경우를 모두 구해야 함(최대 3칸)
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
				if newSharkX < 0 || newSharkX > 16 || newSharkY < 0 || newSharkY > 16 { // 범위를 벗어나는 경우
					break
				} else if area[newSharkX][newSharkY].fishNum == 0 { // 물고기가 없는 칸으로 갈 경우
					break
				} else { // 물고기 만나는 경우
					sharkX, sharkY = newSharkX, newSharkY
					sharkDirection = area[sharkX][sharkY].direction
					eat += area[sharkX][sharkY].fishNum
					area[sharkX][sharkY].fishNum = 0
					area[sharkX][sharkY].direction = 0
					newElement := Element{fishes, area, sharkX, sharkY, sharkDirection, eat}
					q.Push(newElement)
				}
			}
		}
	}
}
