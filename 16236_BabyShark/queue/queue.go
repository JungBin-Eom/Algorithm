package queue

import "fmt"

type Node struct {
	X, Y int
}

func (n *Node) String() string {
	return fmt.Sprint(n.X, n.Y)
}

func NewQueue() *Queue {
	return &Queue{}
}

type Queue struct {
	nodes []*Node
	count int
}

func (s *Queue) Enque(n *Node) {
	s.nodes = append(s.nodes[:s.count], n)
	s.count++
}

func (s *Queue) Deque() *Node {
	if s.count == 0 {
		return nil
	}
	s.count--
	result := s.nodes[0]
	s.nodes = s.nodes[1:]
	return result
}
