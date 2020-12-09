package main

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/gonum/stat/combin"
)

func parseInputToDimensions(input []string) [][]int {
	var dimensionsArray [][]int

	for _, in := range input {
		var sizeArray []int
		for _, dim := range strings.Split(strings.TrimSpace(in), "x") {
			intDim, err := strconv.Atoi(dim)
			check(err)
			sizeArray = append(sizeArray, intDim)
		}

		dimensionsArray = append(dimensionsArray, sizeArray)
	}

	return dimensionsArray
}

func calculateTotalSize(dimensionsArray [][]int) int {
	total := 0
	combinations := combin.Combinations(3, 2)

	for _, dim := range dimensionsArray {
		var areas []int

		for _, combination := range combinations {
			areas = append(areas, dim[combination[0]]*dim[combination[1]])
		}

		minArea := calculateMinInt(areas)

		for _, area := range areas {
			total = total + (2 * area)
		}

		total = total + minArea
	}
	return total
}

func calculateMinInt(ints []int) int {
	min := ints[0]
	for _, i := range ints {
		if i < min {
			min = i
		}
	}

	return min
}

func main() {
	input := splitLines(readFile("day2.dat"))

	fmt.Println(calculateTotalSize(parseInputToDimensions(input)))
}
