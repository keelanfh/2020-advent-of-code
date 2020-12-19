package main

import "fmt"

var lastSpoken map[int]int
var beforeLastSpoken map[int]int

func compute(startingNumbers []int, maxTurn int) int {

	// Set up the two maps
	lastSpoken = make(map[int]int)
	beforeLastSpoken = make(map[int]int)

	var previous int
	var result int

	// Loop through the starting numbers
	for i, num := range startingNumbers {
		// lastSpoken becomes beforeLastSpoken
		// current turn becomes lastSpoken
		beforeLastSpoken[num], lastSpoken[num] = lastSpoken[num], i+1

		// Assign the current num to the `previous` variable so that it goes into the next step
		previous = num
	}

	// Now we're loooping through all the rest of the turns
	for turn := len(startingNumbers) + 1; turn <= maxTurn; turn++ {
		// Speak 0 if it's only been spoken once before
		if beforeLastSpoken[previous] == 0 {
			result = 0
			// Otherwise compute the difference between the previous two times
		} else {
			result = lastSpoken[previous] - beforeLastSpoken[previous]
		}

		// lastSpoken becomes beforeLastSpoken
		// current turn becomes lastSpoken
		// assign result to previous for next iteration
		beforeLastSpoken[result], lastSpoken[result] = lastSpoken[result], turn
		previous = result
	}

	return result
}

func main() {
	startingNumbers := []int{18, 8, 0, 5, 4, 1, 20}
	fmt.Println(compute(startingNumbers, 2020))
	fmt.Println(compute(startingNumbers, 30000000))
}
