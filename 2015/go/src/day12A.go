package main

import (
	"encoding/json"
	"fmt"
)

func sumNumbers(i interface{}) int {
	total := 0

	f, ok := i.(float64)
	if ok {
		total = int(f)
	}

	s, ok := i.([]interface{})
	if ok {
		for _, i_ := range s {
			total = total + sumNumbers(i_)
		}
	}

	m, ok := i.(map[string]interface{})
	if ok {
		for _, i_ := range m {
			total = total + sumNumbers(i_)
		}
	}

	return total
}

func main() {
	input := readFile("day12.dat")

	var i interface{}
	json.Unmarshal([]byte(input), &i)

	fmt.Println(sumNumbers(i))
}
