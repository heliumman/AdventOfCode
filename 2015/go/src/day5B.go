package main

import (
	"fmt"
	"strings"
)

func testWord(word string) int {

	validWord := 0

	rule1 := false

	i := 0
	for i < len(word)-1 {
		tempLetters := word[i : i+2]
		if strings.Contains(word[i+2:], tempLetters) {
			rule1 = true
		}
		i++
	}

	rule2 := false

	i = 0
	for i < len(word)-2 {
		if word[i] == word[i+2] {
			rule2 = true
		}
		i++
	}

	if rule1 && rule2 {
		validWord = 1
	}

	return validWord
}

func checkWords(words []string) int {
	count := 0

	for _, word := range words {
		count = count + testWord(word)
	}

	return count
}

func main() {
	input := splitLines(readFile("day5.dat"))

	fmt.Println(checkWords(input))
}
