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
		var perims []int

		for _, combination := range combinations {
			perims = append(perims, 2*(dim[combination[0]]+dim[combination[1]]))
		}

		minPerim := calculateMinInt(perims)

		volume := dim[0] * dim[1] * dim[2]

		total = total + minPerim + volume
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
