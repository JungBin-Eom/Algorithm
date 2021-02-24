package main

import "fmt"

var N, min int
var S [][]int

func dfs(team []int, index int) {
	for i := index + 1; i < N; i++ {
		startTeam := append(team, i)
		if len(startTeam) == N/2 {
			// 팀 능력치 계산
			linkTeam := make([]int, 0)
			for j := 0; j < N; j++ {
				var in bool
				for _, member := range startTeam {
					if member == j {
						in = true
						break
					}
				}
				if !in {
					linkTeam = append(linkTeam, j)
				}
			}
			// fmt.Println(startTeam)
			// fmt.Println(linkTeam)
			var startStat, linkStat int
			for j := 0; j < N/2; j++ {
				for k := 0; k < N/2; k++ {
					if j != k {
						startStat += S[startTeam[j]][startTeam[k]]
						linkStat += S[linkTeam[j]][linkTeam[k]]
					}
				}
			}
			// fmt.Println("startStat is ", startStat)
			// fmt.Println("linkStat is ", linkStat)

			if startStat >= linkStat {
				if min > startStat-linkStat {
					min = startStat - linkStat
				}
			} else {
				if min > linkStat-startStat {
					min = linkStat - startStat
				}
			}
			// fmt.Println("min is ", min)
			startTeam = startTeam[:len(startTeam)-1]
		} else {
			dfs(startTeam, i)
			startTeam = startTeam[:len(startTeam)-1]
		}
	}
}

func main() {
	// input
	fmt.Scanln(&N)
	S = make([][]int, N)
	for i := 0; i < N; i++ {
		S[i] = make([]int, N)
		for j := 0; j < N; j++ {
			fmt.Scan(&S[i][j])
		}
	}
	min = 99999

	start := make([]int, 0)

	for i := 0; i < N/2+1; i++ {
		start = append(start, i)
		dfs(start, i)
		start = start[:len(start)-1]
	}

	fmt.Println(min)
}
