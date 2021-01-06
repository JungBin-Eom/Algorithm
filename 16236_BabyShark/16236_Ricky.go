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
	var N, fish, sharkX, sharkY, startCount, totalCount, eattingCount, fishCount, moveCount int
	shark := 2
	q := queue.NewQueue()
	fmt.Scanln(&N)

	mySea := make(sea, N)
	visited := make([][]int, N)

	for i := 0; i < N; i++ {
		mySea[i] = make([]int, N)
		visited[i] = make([]int, N)
	}

	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			fmt.Scan(&fish)
			if fish == 9 {
				sharkX = i
				sharkY = j
			} else if fish == 1 {
				startCount++
			}
			if fish != 0 {
				fishCount++
			}
			mySea[i][j] = fish
		}
	}

	if startCount == 0 {
		fmt.Println(totalCount)
		return
	}

	visited[sharkX][sharkY] = 1

	node := queue.Node{sharkX, sharkY, 0}
	q.Enque(&node)

	for q.Size() != 0 || fishCount == 0 {
		nowNode := q.Deque()
		if mySea[nowNode.X][nowNode.Y] != 0 || mySea[nowNode.X][nowNode.Y] < shark { // 먹을 수 있는 물고기 발견
			eattingCount++
			mySea[nowNode.X][nowNode.Y] = 0
			if eattingCount == shark { // shark 크기만큼 물고기 먹으면 성장
				eattingCount = 0
				shark++
			}
			fishCount--
		}

		if nowNode.X-1 >= 0 || visited[nowNode.X-1][nowNode.Y] == 0 || mySea[nowNode.X-1][nowNode.Y] <= shark { // 위쪽
			q.Enque(&queue.Node{nowNode.X - 1, nowNode.Y})
			visited[nowNode.X-1][nowNode.Y] = 1
		}
		if nowNode.Y-1 >= 0 || visited[nowNode.X][nowNode.Y-1] == 0 || mySea[nowNode.X][nowNode.Y-1] <= shark { // 왼쪽
			q.Enque(&queue.Node{nowNode.X, nowNode.Y - 1})
			visited[nowNode.X][nowNode.Y-1] = 1
		}
		if nowNode.X+1 < N || visited[nowNode.X+1][nowNode.Y] == 0 || mySea[nowNode.X+1][nowNode.Y] <= shark { // 오른쪽
			q.Enque(&queue.Node{nowNode.X + 1, nowNode.Y})
			visited[nowNode.X+1][nowNode.Y] = 1
		}
		if nowNode.Y+1 < N || visited[nowNode.X][nowNode.Y+1] == 0 || mySea[nowNode.X][nowNode.Y+1] <= shark { // 아래쪽
			q.Enque(&queue.Node{nowNode.X, nowNode.Y + 1})
			visited[nowNode.X][nowNode.Y+1] = 1
		}
	}

	fmt.Println(mySea)
	fmt.Println("Shark is at X: ", sharkX, " Y: ", sharkY)
}
