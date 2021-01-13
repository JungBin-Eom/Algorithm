package main

import "fmt"

type consult struct {
	time, price int
}

func main() {
	var N, time, price int
	fmt.Scanln(&N)

	schedules := make([]consult, 0)
	profit := make([]int, N+1)

	for i := 0; i < N; i++ {
		fmt.Scanln(&time, &price)
		schedule := consult{time, price}
		schedules = append(schedules, schedule)
	}

	for i := N - 1; i >= 0; i-- {
		// fmt.Println("i : ", i)
		if i+schedules[i].time > N {
			profit[i] = profit[i+1]
		} else if schedules[i].price+profit[i+schedules[i].time] > profit[i+1] {
			profit[i] = schedules[i].price + profit[i+schedules[i].time]
			// fmt.Printf("%d째날 이득 계산\n", i+1)
			// fmt.Println("이날 상담 시작하는 경우", schedules[i].price+profit[i+schedules[i].time])
			// fmt.Println("이 전에 상담을 계속 하는 경우", profit[i+1])
		} else {
			profit[i] = profit[i+1]
			// fmt.Printf("%d째날 이득 계산\n", i+1)
			// fmt.Println("이날 상담 시작하는 경우", schedules[i].price+profit[i+schedules[i].time])
			// fmt.Println("이 전에 상담을 계속 하는 경우", profit[i+1])
		}
	}
	// fmt.Println(profit)
	fmt.Println(profit[0])
}
