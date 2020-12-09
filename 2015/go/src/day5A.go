package main

import (
	"fmt"
	"strings"
)

func testWord(word string) int {

	validWord := 0

	//vowel count
	vowels := "aeiou"
	vowelCount := 0

	for _, vowel := range vowels {
		vowelCount = vowelCount + strings.Count(word, string(vowel))
	}

	//double letter
	tempLetter := ""
	containsDoubleLetter := false
	for _, letter := range word {
		if tempLetter == string(letter) {
			containsDoubleLetter = true
		} else {
			tempLetter = string(letter)
		}
	}

	//bad combos
	badCombos := [4]string{"ab", "cd", "pq", "xy"}
	badCount := 0
	for _, combo := range badCombos {
		badCount = badCount + strings.Count(word, combo)
	}

	if vowelCount >= 3 && containsDoubleLetter && badCount == 0 {
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
