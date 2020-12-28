package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

// Execute a sum with operator and arguments
func executeSum(op string, a int, b int) int {
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

// Execute the leftmost sum in an expression
// Supply operators as []string e.g. []string{`*`, `+`}
// If nothing matches, will return expr
func executeLeftmostSum(expr string, op []string) string {
	opregex := strings.Join(op, `|\`)
	regex := `^(.*?)(\d+)\s(\` + opregex + `)\s(\d+)(.*)$`

	re := regexp.MustCompile(regex)
	matches := re.FindStringSubmatch(expr)

	if matches != nil {
		// matches:
		// [1]: string before sum
		// [2]: first operand
		// [3]: operator
		// [4]: second operand
		// [5]: string after sum

		a, _ := strconv.Atoi(matches[2])
		op := matches[3]
		b, _ := strconv.Atoi(matches[4])

		result := fmt.Sprintf(`${1}%d${5}`, executeSum(op, a, b))

		return re.ReplaceAllString(expr, result)
	}

	return expr
}

// Process an expression line with a given mode
func executeLine(expr string, mode int) string {
	// Very simple behaviour in the first mode.
	// This evaluates the leftmost sum that it can, matching * and +.
	if mode == 1 {
		expr = executeLeftmostSum(expr, []string{`*`, `+`})
	} else if mode == 2 {
		// Look for brackets first
		re := regexp.MustCompile(`^(.*)\((.*?)\)(.*)$`)
		matches := re.FindStringSubmatch(expr)

		// If you find a match, apply executeLine recursively inside the brackets
		if matches != nil {
			expr = re.ReplaceAllString(expr, "${1}"+executeLine(matches[2], 2)+"${3}")
			// Otherwise, use the rules of precedence for operators
			// Apply the addition one first as many times as you can
			// Then the same for the multiplication one
			// We can guarantee that there are no brackets in this section.
		} else {

			for _, op := range [][]string{{`+`}, {`*`}} {
				for {
					newExpr := executeLeftmostSum(expr, op)
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
			// Keep running executeLine until you get to a number
			result, err := strconv.Atoi(expr)
			for err != nil {
				expr = executeLine(expr, mode)
				result, err = strconv.Atoi(expr)
			}
			total += result
		}
		fmt.Println(total)
	}
}
