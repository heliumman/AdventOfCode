package main

import (
	"fmt"
	"strconv"
	"strings"
)

var off = -1
var on = 1
var toggle = 0

func processInstructions(instructions []string) map[string]int {
	path := map[string]int{}

	for _, instruction := range instructions {
		lights, op := parseInstruction(instruction)

		i := lights[0][0]
		for i <= lights[0][1] {
			j := lights[1][0]
			for j <= lights[1][1] {

				pos := strconv.Itoa(i) + "," + strconv.Itoa(j)
				status := path[pos]

				if status == 0 {
					status = -1
				}

				if op != toggle {
					status = op
				} else {
					status = -1 * status
				}

				path[pos] = status

				j++
			}

			i++
		}
	}

	return path

}

func parseInstruction(instruction string) ([2][2]int, int) {
	lights := [2][2]int{}
	op := 0

	prefix := ""
	if strings.HasPrefix(instruction, "turn off") {
		prefix = "turn off"
		op = off
	} else if strings.HasPrefix(instruction, "turn on") {
		prefix = "turn on"
		op = on
	} else {
		prefix = "toggle"
		op = toggle
	}

	tempInstruction := strings.TrimSpace(strings.Split(instruction, prefix)[1])

	lowerbound := strings.TrimSpace(strings.Split(tempInstruction, "through")[0])
	upperbound := strings.TrimSpace(strings.Split(tempInstruction, "through")[1])

	lights[0][0], _ = strconv.Atoi(strings.Split(lowerbound, ",")[0])
	lights[0][1], _ = strconv.Atoi(strings.Split(upperbound, ",")[0])
	lights[1][0], _ = strconv.Atoi(strings.Split(lowerbound, ",")[1])
	lights[1][1], _ = strconv.Atoi(strings.Split(upperbound, ",")[1])

	return lights, op

}

func countLights(path map[string]int) int {
	total := 0

	for _, i := range path {
		if i == on {
			total++
		}
	}

	return total
}

func main() {
	input := splitLines(readFile("day6.dat"))

	path := processInstructions(input)
	fmt.Println(countLights(path))
}
