package main

import (
	"fmt"
	"strconv"
	"strings"
)

func sumValArray(valArray []int) int {
	total := 0

	for _, val := range valArray {
		total = total + val
	}

	return total
}

func convertValArrayToInt(valArray []string) []int {
	var intArray []int

	for _, val := range valArray {
		intVal, err := strconv.Atoi(val)
		check(err)
		intArray = append(intArray, intVal)
	}

	return intArray
}

func main() {
	input := readFile("day1.dat")

	//Replace Strings with numeric values
	input = strings.TrimSpace(strings.ReplaceAll(strings.ReplaceAll(input, "(", "1 "), ")", "-1 "))
	valArray := strings.Split(input, " ")

	total := sumValArray(convertValArrayToInt(valArray))

	fmt.Println(total)
}
