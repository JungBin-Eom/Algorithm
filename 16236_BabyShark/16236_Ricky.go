package main

import (
	"Algorithm/16236_BabyShark/queue"
	"fmt"
	"sort"
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
	var N, fish, sharkX, sharkY, startCount, totalCount, eattingCount, fishCount int
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

	fishCount--

	if startCount == 0 {
		fmt.Println(totalCount)
		return
	}

	visited[sharkX][sharkY] = 1
	mySea[sharkX][sharkY] = 0

	node := queue.Node{X: sharkX, Y: sharkY, Dist: 0}
	eat := []*queue.Node{}
	q.Enque(&node)
	for {
		eat = []*queue.Node{}
		for q.Size() != 0 { // BFS
			nowNode := q.Deque()
			if mySea[nowNode.X][nowNode.Y] != 0 && mySea[nowNode.X][nowNode.Y] < shark { // 먹을 수 있는 물고기 발견
				// fmt.Println("==============eat fish time=============")
				eat = append(eat, nowNode)
			}
			if nowNode.X-1 >= 0 && visited[nowNode.X-1][nowNode.Y] == 0 && mySea[nowNode.X-1][nowNode.Y] <= shark { // 위쪽
				q.Enque(&queue.Node{nowNode.X - 1, nowNode.Y, nowNode.Dist + 1})
				visited[nowNode.X-1][nowNode.Y] = 1
			}
			if nowNode.Y-1 >= 0 && visited[nowNode.X][nowNode.Y-1] == 0 && mySea[nowNode.X][nowNode.Y-1] <= shark { // 왼쪽
				q.Enque(&queue.Node{nowNode.X, nowNode.Y - 1, nowNode.Dist + 1})
				visited[nowNode.X][nowNode.Y-1] = 1
			}
			if nowNode.Y+1 < N && visited[nowNode.X][nowNode.Y+1] == 0 && mySea[nowNode.X][nowNode.Y+1] <= shark { // 오른쪽
				q.Enque(&queue.Node{nowNode.X, nowNode.Y + 1, nowNode.Dist + 1})
				visited[nowNode.X][nowNode.Y+1] = 1
			}
			if nowNode.X+1 < N && visited[nowNode.X+1][nowNode.Y] == 0 && mySea[nowNode.X+1][nowNode.Y] <= shark { // 아래쪽
				q.Enque(&queue.Node{nowNode.X + 1, nowNode.Y, nowNode.Dist + 1})
				visited[nowNode.X+1][nowNode.Y] = 1
			}
		}

		if len(eat) == 0 {
			break
		} else if len(eat) == 1 {
			mySea[eat[0].X][eat[0].Y] = 0
			sharkX = eat[0].X
			sharkY = eat[0].Y
			eattingCount++
			totalCount += eat[0].Dist
			if eattingCount == shark { // shark 크기만큼 물고기 먹으면 성장
				eattingCount = 0
				shark++
			}
			visited = make([][]int, N)
			for i := 0; i < N; i++ {
				visited[i] = make([]int, N)
			}
			q = queue.NewQueue()
			q.Enque(&queue.Node{sharkX, sharkY, 0})
		} else {
			// eat sort해야함
			sort.Slice(eat, func(i, j int) bool {
				if eat[i].Dist <= eat[j].Dist {
					if eat[i].Dist == eat[j].Dist {
						if eat[i].X <= eat[j].X {
							if eat[i].X == eat[j].X {
								if eat[i].Y < eat[j].Y {
									return true
								}
								return false
							}
							return true
						}
						return false
					}
					return true
				}
				return false
			})
			mySea[eat[0].X][eat[0].Y] = 0
			sharkX = eat[0].X
			sharkY = eat[0].Y
			eattingCount++
			totalCount += eat[0].Dist
			if eattingCount == shark { // shark 크기만큼 물고기 먹으면 성장
				eattingCount = 0
				shark++
			}
			visited = make([][]int, N)
			for i := 0; i < N; i++ {
				visited[i] = make([]int, N)
			}
			q = queue.NewQueue()
			q.Enque(&queue.Node{sharkX, sharkY, 0})
		}
		// fmt.Println(mySea)
		// fmt.Println("Shark is at X: ", nowNode.X, " Y: ", nowNode.Y)
		// fmt.Println("Total count: ", totalCount)
		// fmt.Println("Now distance: ", nowNode.Dist)
		// fmt.Println("Shark size: ", shark)
		// fmt.Println()
	}
	// fmt.Println(mySea)
	// fmt.Println("Shark is at X: ", sharkX, " Y: ", sharkY)
	// fmt.Println("Total count: ", totalCount)
	fmt.Println(totalCount)
}
