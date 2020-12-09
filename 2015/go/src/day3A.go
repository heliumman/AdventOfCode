package main

import (
	"fmt"
	"strconv"
)

func followDirections(directions string) map[string]int {
	path := map[string]int{
		"0,0": 1,
	}

	pos := [2]int{0, 0}

	for _, dir := range directions {
		if dir == '^' {
			pos[1]++
		} else if dir == 'v' {
			pos[1]--
		} else if dir == '<' {
			pos[0]--
		} else if dir == '>' {
			pos[0]++
		}
		charPos := strconv.Itoa(pos[0]) + "," + strconv.Itoa(pos[1])
		path[charPos]++
	}

	return path
}

func main() {
	input := readFile("day3.dat")

	fmt.Println(len(followDirections(input)))
}
