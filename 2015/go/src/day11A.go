package main

import (
	"fmt"
	"strings"
)

func findPassword(pw string) string {
	newPw := pw
	validPw := false

	for !validPw {
		newPw = incrimentLetter(newPw)
		validPw = validPassword(newPw)
	}

	return newPw
}

func incrimentLetter(pw string) string {
	resets := []int{}
	increment := len(pw) - 1

	i := len(pw) - 1

	for i >= 0 && increment > -1 {
		if pw[i] == 'z' {
			resets = append(resets, i)
			increment--
		} else {
			increment = -1
			pw = pw[:i] + string(pw[i]+1) + pw[i+1:]
		}
		i--
	}

	for _, j := range resets {
		pw = pw[:j] + "a" + pw[j+1:]
	}

	return pw
}

func validPassword(pw string) bool {
	return !containsIOL(pw) && containsRun(pw) && contains2Doubles(pw)
}

func containsIOL(pw string) bool {
	return strings.Contains(pw, "i") || strings.Contains(pw, "o") || strings.Contains(pw, "l")
}

func containsRun(pw string) bool {
	valid := false
	i := 0

	for i < len(pw)-2 && !valid {
		valid = pw[i]+1 == pw[i+1] && pw[i]+2 == pw[i+2]
		i++
	}

	return valid
}

func contains2Doubles(pw string) bool {
	valid := false
	tmp := ""
	counter := 0
	i := 0

	for i < len(pw) {
		if string(pw[i]) == tmp {
			counter++
			tmp = ""
		} else {
			tmp = string(pw[i])
		}
		i++
	}

	valid = counter >= 2

	return valid
}

func main() {
	input := readFile("day11.dat")

	fmt.Println(findPassword(input))
}
