package main

import (
	"fmt"
	"strconv"
)

func parseNumber(num string) string {
	val := ""

	tmp := ""
	counter := 0

	for _, n := range num {
		if tmp != string(n) {

			if counter > 0 {
				val = val + strconv.Itoa(counter) + tmp
			}

			counter = 1
			tmp = string(n)
		} else {
			counter = counter + 1
		}
	}

	if counter > 0 {
		val = val + strconv.Itoa(counter) + tmp
	}

	return val
}

func main() {
	input := readFile("day10.dat")

	fmt.Println(input)

	counter := 1
	num := input

	for counter <= 50 {
		num = parseNumber(num)

		counter++
	}

	fmt.Println(len(num))
}
