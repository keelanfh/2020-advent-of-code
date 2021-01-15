package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

var l, m, n, p int

// Make a zeroed 3D grid of size m*n*p
func make3DGrid() [][][]bool {

	grid := make([][][]bool, m)

	for i := range grid {
		grid[i] = make([][]bool, n)
		for j := range grid[i] {
			grid[i][j] = make([]bool, p)
		}
	}

	return grid
}

// Making a zeroed 4D Grid of size l*m*n*p
func make4DGrid() [][][][]bool {

	grid := make([][][][]bool, l)

	for i := range grid {
		grid[i] = make3DGrid()
	}

	return grid
}

// Sum the 3D neighbours of a cube x,y,z in a grid
func sum3DNeighbours(grid [][][]bool, x, y, z int) int {
	total := 0

	for i := -1; i <= 1; i++ {
		for j := -1; j <= 1; j++ {
			for k := -1; k <= 1; k++ {
				// Set up indices for all the neighbours
				xo := x + i
				yo := y + j
				zo := z + k

				// Don't count the cube itself
				if !(i == 0 && j == 0 && k == 0) {
					// Bounds checking - the grid is big enough, so just disregard
					// Only add to total if the neighbour is active
					if xo >= 0 && yo >= 0 && zo >= 0 &&
						xo < m && yo < n && zo < p &&
						grid[xo][yo][zo] {
						total++
					}
				}
			}
		}
	}

	return total
}

// Compute the 4D neighbours of a hypercube w,x,y,z in a grid
func sum4DNeighbours(grid [][][][]bool, w, x, y, z int) int {
	total := 0

	for h := -1; h <= 1; h++ {
		for i := -1; i <= 1; i++ {
			for j := -1; j <= 1; j++ {
				for k := -1; k <= 1; k++ {
					// Set up indices for all the neighbours
					wo := w + h
					xo := x + i
					yo := y + j
					zo := z + k

					// Don't count the hypercube itself
					if !(h == 0 && i == 0 && j == 0 && k == 0) {
						// Bounds checking - the grid is big enough, so disregard
						// Only add to total if the neighbour is active
						if wo >= 0 && xo >= 0 && yo >= 0 && zo >= 0 &&
							wo < l && xo < m && yo < n && zo < p &&
							grid[wo][xo][yo][zo] {
							total++
						}
					}
				}
			}
		}
	}
	return total
}

// Compute the new state for a (hyper)cube - this logic is the same in 3D and 4D
func newState(active bool, total int) bool {

	if active {
		if total == 2 || total == 3 {
			return true
		}
		return false
	}

	if total == 3 {
		return true
	}

	return false
}

func iterate3DGrid(grid [][][]bool) [][][]bool {
	newGrid := make3DGrid()
	for i, flat := range grid {
		for j, row := range flat {
			for k := range row {
				newGrid[i][j][k] = newState(grid[i][j][k], sum3DNeighbours(grid, i, j, k))
			}
		}
	}

	return newGrid
}

func iterate4DGrid(grid [][][][]bool) [][][][]bool {
	newGrid := make4DGrid()
	for h, cube := range grid {
		for i, flat := range cube {
			for j, row := range flat {
				for k := range row {
					newGrid[h][i][j][k] = newState(grid[h][i][j][k], sum4DNeighbours(grid, h, i, j, k))
				}
			}
		}
	}

	return newGrid
}

func countCube(cube [][][]bool) int {
	actives := 0

	for _, flat := range cube {
		for _, row := range flat {
			for _, char := range row {
				if char {
					actives++
				}
			}
		}
	}

	return actives

}

func compute(iterations int, dimension int) int {

	// File opening
	file, err := os.Open("17/input.txt")
	if err != nil {
		log.Fatal(err)
	}

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	// Set up the right dimensions for the array
	l = iterations*2 + 1
	m = l
	n = iterations*2 + len(lines)
	p = iterations*2 + len(lines[0])

	if dimension == 3 {

		grid := make3DGrid()

		// Filling the grid with input data
		for i, row := range lines {
			for j, char := range row {
				grid[iterations][iterations+i][iterations+j] = (string(char) == "#")
			}
		}

		for i := 0; i < iterations; i++ {
			grid = iterate3DGrid(grid)
		}

		return countCube(grid)

	} else if dimension == 4 {
		grid := make4DGrid()

		// Filling the grid with the input data
		for i, row := range lines {
			for j, char := range row {
				grid[iterations][iterations][iterations+i][iterations+j] = (string(char) == "#")
			}
		}

		for i := 0; i < iterations; i++ {
			grid = iterate4DGrid(grid)
		}

		actives := 0
		for _, cube := range grid {
			actives += countCube(cube)
		}
		return actives
	}
	return 0
}

func main() {
	fmt.Println(compute(6, 3))
	fmt.Println(compute(6, 4))
}
