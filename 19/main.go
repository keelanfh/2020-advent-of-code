package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"reflect"
	"regexp"
	"strconv"
	"strings"
)

var rules map[int]string
var complete map[int]bool

func replaceRule(rule string) string {
	ruleInt, _ := strconv.Atoi(rule)

	if complete[ruleInt] {
		return "(" + rules[ruleInt] + ")"
	}
	return rule
}

func main() {
	// File opening
	file, err := os.Open("19/input.txt")
	if err != nil {
		log.Fatal(err)
	}

	rules = make(map[int]string)
	var texts []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.Split(scanner.Text(), ":")
		if len(line) == 2 {
			num, _ := strconv.Atoi(line[0])
			rules[num] = strings.ReplaceAll(line[1], "\"", "")
		} else if line[0] != "" {
			texts = append(texts, line[0])
		}
	}

	complete = make(map[int]bool)

	j := 0
	tot := 0
	for {
		newRules := make(map[int]string)
		for i, rule := range rules {
			// If there are no numbers in the string, it is complete
			re := regexp.MustCompile(`\d+`)
			if !re.MatchString(rule) {
				complete[i] = true
			}
			newRules[i] = re.ReplaceAllStringFunc(rule, replaceRule)
		}
		if reflect.DeepEqual(rules, newRules) {
			// Only stop iterating if rules=newRules twice
			// This stops us from running into issues where a rule hasn't been
			// marked as complete before it is referred to
			tot++
			rules = newRules
			if tot > 1 {
				break
			}
		}
		rules = newRules
		j++
	}

	newRules := make(map[int]string)
	for i, rule := range rules {
		newRules[i] = "^" + strings.ReplaceAll(rule, " ", "") + "$"
	}
	rules = newRules

	total := 0
	for _, text := range texts {
		matched, _ := regexp.MatchString(rules[0], text)
		if matched {
			total++
		}
	}

	fmt.Println(total)
}
