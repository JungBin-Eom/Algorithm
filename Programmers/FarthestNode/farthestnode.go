package main

import (
	"fmt"
)

func solution(n int, edge [][]int) int {
	var result int
	graph := make([][]int, n+1)
	for _, v := range edge {
		graph[v[0]] = append(graph[v[0]], v[1])
		graph[v[1]] = append(graph[v[1]], v[0])
	}

	distance := make([]int, n+1)
	for i := 2; i < n+1; i++ {
		distance[i] = 20000
	}

	queue := make([][]int, 0)
	start := []int{1, 0}
	queue = append(queue, start)

	for len(queue) != 0 {
		now, dist := queue[0][0], queue[0][1]
		if len(queue) == 1 {
			queue = make([][]int, 0)
		} else {
			queue = queue[1:]
		}
		if distance[now] >= dist {
			for _, v := range graph[now] {
				cost := dist + 1
				if cost < distance[v] {
					distance[v] = cost
					new := []int{v, cost}
					queue = append(queue, new)
				}
			}
		}
	}
	max := 0

	for _, dist := range distance {
		if dist > max {
			result = 1
			max = dist
		} else if dist == max {
			result += 1
		}
	}
	return result
}

func main() {
	n := 6
	edge := [][]int{{3, 6}, {4, 3}, {3, 2}, {1, 3}, {1, 2}, {2, 4}, {5, 2}}
	fmt.Println(solution(n, edge))
}
