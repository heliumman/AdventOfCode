package main

import (
	"fmt"
	"strconv"
)

func parseString(in string) string {
	s, _ := strconv.Unquote(in)
	return s
}

func parseInput(input []string) int {
	total := 0
	for _, i := range input {
		parsed := parseString(i)
		total = total + len(i) - len(parsed)
	}

	return total
}

func main() {
	input := splitLines(readFile("day8.dat"))

	//fmt.Println(input)
	fmt.Println(parseInput(input))
}
