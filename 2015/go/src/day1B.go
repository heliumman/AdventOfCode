package main

import (
	"fmt"
	"strconv"
	"strings"
)

func findFloor(floor int, valArray []int) int {
	total := 0
	foundFloor := false
	i := 0

	for i < len(valArray) && !foundFloor {
		total = total + valArray[i]
		if total == -1 {
			foundFloor = true
		}
		i++
	}

	return i
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

	position := findFloor(-1, convertValArrayToInt(valArray))

	fmt.Println(position)
}
