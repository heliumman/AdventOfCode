package main

import (
	"io/ioutil"
	"log"
	"strings"
)

func check(e error) {
	if e != nil {
		log.Fatal(e)
	}
}

func readFile(file string) string {
	dat, err := ioutil.ReadFile(file)
	check(err)
	return strings.TrimSpace(string(dat))
}

func splitLines(input string) []string {
	return strings.Split(input, "\n")
}
