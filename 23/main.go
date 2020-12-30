package main

import (
	"container/ring"
	"fmt"
)

func printRing(r *ring.Ring) {
	for j := 0; j < r.Len(); j++ {
		fmt.Print(r.Value)
		r = r.Next()
	}
	fmt.Println()
}

func modLikePython(d, m int) int {
	res := d % m
	if res <= 0 {
		return res + m
	}
	return res
}

func do(r *ring.Ring) *ring.Ring {
	var curr int = r.Value.(int)
	// fmt.Println(curr)
	// fmt.Println()

	// printRing(r)

	hand := r.Unlink(3)

	// printRing(hand)

	// finding the destination
dests:
	for dest := modLikePython(curr-1, 9); true; dest = modLikePython(dest-1, 9) {
		// fmt.Println("possible dest", dest)
		for j := 0; j < r.Len(); j++ {
			val := r.Value
			// fmt.Println(val, dest)
			if val.(int) == dest {
				// put the hand back in
				// fmt.Println("destination", r.Value)
				r.Link(hand)
				break dests
			}
			r = r.Next()
		}

	}

	// fmt.Println(r.Value)
	// fmt.Println()

	for j := 0; j < hand.Len(); j++ {
		val := r.Value
		if val.(int) == curr {
			break
		}
		r = r.Next()
	}

	r = r.Next()

	return r

}

func main() {
	numbers := []int{5, 9, 8, 1, 6, 2, 7, 3, 4}
	n := 9
	r := ring.New(n)

	// Load the numbers into the ring
	for _, number := range numbers {
		r.Value = number
		r = r.Next()
	}

	// for i := 10; i < 1000000; i++ {
	// 	r.Value = i
	// 	r = r.Next()
	// }

	for i := 0; i < 100; i++ {
		r = do(r)
	}

	for j := 0; j < r.Len(); j++ {
		val := r.Value
		if val.(int) == 1 {
			break
		}
		r = r.Next()
	}
	r = r.Prev()
	r.Unlink(1)
	r = r.Next()

	printRing(r)
}
