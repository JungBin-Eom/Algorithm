package main

import "fmt"

type fish struct {
	x, y, fishNum, direction int
}

func main() {
	var fishNum, direction int
	var sharkX, sharkY, sharkDirection, eat int

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
			fishNum++
		}
	}

	// 상어 입장
	sharkDirection = area[0][0].direction
	sharkX, sharkY = 0, 0
	eat += area[0][0].fishNum
	area[0][0].fishNum = 0
	area[0][0].direction = 0

	// 물고기 이동
	for i := 0; i < 16; i++ {
		var newX, newY, rotateCount int
		for rotateCount != 8 {
			switch fishes[i].direction {
			case 1:
				newX, newY = fishes[i].x-1, fishes[i].y-1
			case 2:
				newX, newY = fishes[i].x-1, fishes[i].y
			case 3:
				newX, newY = fishes[i].x-1, fishes[i].y+1
			case 4:
				newX, newY = fishes[i].x, fishes[i].y-1
			case 5:
				newX, newY = fishes[i].x, fishes[i].y+1
			case 6:
				newX, newY = fishes[i].x+1, fishes[i].y-1
			case 7:
				newX, newY = fishes[i].x+1, fishes[i].y
			case 8:
				newX, newY = fishes[i].x+1, fishes[i].y+1
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
				area[newX][newY], area[fishes[i].x][fishes[i].y] = area[fishes[i].x][fishes[i].y], area[newX][newY]
				fishes[area[newX][newY].fishNum].x, fishes[i].x = fishes[i].x, fishes[area[newX][newY].fishNum].x
				fishes[area[newX][newY].fishNum].y, fishes[i].y = fishes[i].y, fishes[area[newX][newY].fishNum].y
				break
			}
		}
	}

	// 상어 이동
	var newSharkX, newSharkY int
	for i := 1; i < 4; i++ { // i칸 이동하는 경우를 모두 구해야 함(최대 3칸)
		switch sharkDirection {
		case 1:
			newSharkX, newSharkY = sharkX-i, sharkY-i
		case 2:
			newSharkX, newSharkY = sharkX-i, sharkY
		case 3:
			newSharkX, newSharkY = sharkX-i, sharkY+i
		case 4:
			newSharkX, newSharkY = sharkX, sharkY-i
		case 5:
			newSharkX, newSharkY = sharkX, sharkY+i
		case 6:
			newSharkX, newSharkY = sharkX+i, sharkY-i
		case 7:
			newSharkX, newSharkY = sharkX+i, sharkY
		case 8:
			newSharkX, newSharkY = sharkX+i, sharkY+i
		}
		if newSharkX < 0 || newSharkX > 16 || newSharkY < 0 || newSharkY > 16 { // 범위를 벗어나는 경우

		} else if area[newSharkX][newSharkY].fishNum == 0 { // 물고기가 없는 칸으로 갈 경우

		} else { // 물고기 만나는 경우
			sharkX, sharkY = newSharkX, newSharkY
			sharkDirection = area[sharkX][sharkY].direction
			area[sharkX][sharkY].fishNum = 0
			area[sharkX][sharkY].direction = 0
		}
	}
	fmt.Println(area)
}
