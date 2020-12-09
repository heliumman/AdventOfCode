package main

import (
	"fmt"
	"strconv"
)

func followDirections(directions string) map[string]int {
	path := map[string]int{
		"0,0": 2,
	}

	pos := [2][2]int{{0, 0}, {0, 0}}

	for i, dir := range directions {
		if dir == '^' {
			pos[i%2][1]++
		} else if dir == 'v' {
			pos[i%2][1]--
		} else if dir == '<' {
			pos[i%2][0]--
		} else if dir == '>' {
			pos[i%2][0]++
		}
		charPos := strconv.Itoa(pos[i%2][0]) + "," + strconv.Itoa(pos[i%2][1])
		path[charPos]++
	}

	return path
}

func main() {
	input := readFile("day3.dat")

	fmt.Println(len(followDirections(input)))
}
