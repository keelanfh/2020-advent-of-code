package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
)

// Execute a sum with operator and arguments
func execute(op string, a int, b int) int {
	if op == "*" {
		return a * b
	} else if op == "+" {
		return a + b
	}
	return 0
}

// Remove brackets from an expression that has brackets just around digits
func removeBrackets(expr string) string {
	re := regexp.MustCompile(`\((\d+)\)`)
	return re.ReplaceAllString(expr, `$1`)
}

// Use a supplied regex to match a particular sum in the expr
// Evaluate that sum and then return the expr with that sum evaluated
// The regex should follow something like
// (_)(arg1)(op)(arg2)
func doRegex(expr string, regex string) string {
	re := regexp.MustCompile(regex)
	matches := re.FindStringSubmatch(expr)

	if matches != nil {

		a, _ := strconv.Atoi(matches[2])
		op := matches[3]
		b, _ := strconv.Atoi(matches[4])

		result := `${1}`
		result += strconv.Itoa(execute(op, a, b))
		result += `$5`

		return re.ReplaceAllString(expr, result)
	}

	return expr
}

// Process an expression line with a given mode
func processLine(expr string, mode int) string {
	// Very simple behaviour in the first mode.
	// This evaluates the leftmost sum that it can.
	if mode == 1 {
		expr = doRegex(expr, `^(.*?)(\d+)\s(\*|\+)\s(\d+)(.*)$`)
	} else if mode == 2 {
		// Look for brackets first
		re := regexp.MustCompile(`^(.*)\((.*?)\)(.*)$`)
		matches := re.FindStringSubmatch(expr)

		// If you find a match, apply processLine recursively inside the brackets
		if len(matches) == 4 {
			expr = re.ReplaceAllString(expr, "${1}"+processLine(matches[2], 2)+"${3}")
			// Otherwise, use the rules of precedence for operators
			// Apply the addition one first as many times as you can
			// Then the same for the multiplication one
			// We can guarantee that there are no brackets in this section.
		} else {
			regexes := []string{`^(.*?)(\d+)\s(\+)\s(\d+)(.*)$`,
				`^(.*?)(\d+)\s(\*)\s(\d+)(.*)$`}

			for _, regex := range regexes {
				for {
					newExpr := doRegex(expr, regex)
					if newExpr == expr {
						expr = newExpr
						break
					}
					expr = newExpr
				}
			}
		}
	}
	// Remove brackets which only surround one number
	return removeBrackets(expr)
}

func main() {

	// File opening
	file, err := os.Open("18/input.txt")
	if err != nil {
		log.Fatal(err)
	}

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	// Run for each mode in turn
	for mode := 1; mode <= 2; mode++ {
		total := 0

		for _, expr := range lines {
			// Keep running processLine until you get to a number
			result, err := strconv.Atoi(expr)
			for err != nil {
				newExpr := processLine(expr, mode)
				if newExpr == expr {
					break
				}
				expr = newExpr
				result, err = strconv.Atoi(expr)
			}
			total += result
		}
		fmt.Println(total)
	}
}
