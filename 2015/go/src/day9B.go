package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"

	prmt "github.com/gitchander/permutation"
)

func stringInList(val string, list []string) bool {
	found := false

	for _, s := range list {
		if s == val {
			found = true
		}
	}

	return found
}

func parseInput(input []string) (map[string]int, []string) {
	edges := map[string]int{}
	vertecies := []string{}

	for _, in := range input {
		locations := strings.Split(strings.TrimSpace(strings.Split(in, "=")[0]), "to")
		tmpLocation := []string{}

		for _, l := range locations {
			tmpLocation = append(tmpLocation, strings.TrimSpace(l))

			if !stringInList(strings.TrimSpace(l), vertecies) {
				vertecies = append(vertecies, strings.TrimSpace(l))
			}
			sort.Strings(vertecies)

		}
		sort.Strings(tmpLocation)

		val := strings.TrimSpace(strings.Split(in, "=")[1])
		dis, _ := strconv.Atoi(val)

		edges[tmpLocation[0]+":"+tmpLocation[1]] = dis

	}

	return edges, vertecies
}

func findShortestPath(edges map[string]int, vertecies []string) int {
	val := 0
	p := prmt.New(prmt.StringSlice(vertecies))
	for p.Next() {
		i := 0
		pathLength := 0
		for i < len(vertecies)-1 {
			tmpLocations := []string{vertecies[i], vertecies[i+1]}
			sort.Strings(tmpLocations)

			pathLength = pathLength + edges[tmpLocations[0]+":"+tmpLocations[1]]

			i++
		}

		if val == 0 {
			val = pathLength
		} else if val < pathLength {
			val = pathLength
		}
	}

	return val
}

func main() {
	input := splitLines(readFile("day9.dat"))

	edges, vertecies := parseInput(input)
	fmt.Println(findShortestPath(edges, vertecies))

}
