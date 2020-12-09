package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"io"
	"strconv"
)

func checkHash(key string) bool {
	h := md5.New()
	io.WriteString(h, key)
	hexStr := hex.EncodeToString(h.Sum(nil))
	fmt.Println(hexStr)

	return hexStr[0:5] == "00000"
}

func incrimentKey(key string) int {
	i := 1

	saltedKey := key + strconv.Itoa(i)

	for !checkHash(saltedKey) {
		i++
		saltedKey = key + strconv.Itoa(i)
	}

	return i
}

func main() {
	input := readFile("day4.dat")

	fmt.Println(incrimentKey(input))
}
