package main

import (
	"fmt"
	"strconv"
	"strings"
)

var left = -1
var right = 1

var andGate = 0
var orGate = 1

var wires map[string]WireWrapper

type WireWrapper struct {
	wire  Wire
	value int
}

type Wire interface {
	Name() string
	Value(wires map[string]WireWrapper) int
	Sources() []string
}

type StaticWire struct {
	name  string
	value int
}

func (sw StaticWire) Name() string {
	return sw.name
}

func (sw StaticWire) Value(wires map[string]WireWrapper) int {
	return sw.value
}

func (sw StaticWire) Sources() []string {
	return []string{}
}

type ShiftWire struct {
	name   string
	dir    int
	value  int
	source string
}

func (sw ShiftWire) Name() string {
	return sw.name
}

func (sw ShiftWire) Value(wires map[string]WireWrapper) int {
	val := -1

	if wires[sw.source].value != -1 {
		val = bitShift(wires[sw.source].value, sw.value, sw.dir)
	}
	return val
}

func (sw ShiftWire) Sources() []string {
	return []string{sw.source}
}

func bitShift(source int, val int, dir int) int {
	i := int64(-1)

	counter := 0
	zeros := ""
	for counter < val {
		zeros = zeros + "0"
		counter++
	}

	b := fmt.Sprintf("%016b", source)
	tmp := ""

	if dir == left {
		tmp = (b + zeros)[val : val+16]
	} else if dir == right {
		tmp = (zeros + b)[0:16]
	}

	i, _ = strconv.ParseInt(tmp, 2, 32)

	return int(i)
}

type PassthroughWire struct {
	name   string
	source string
}

func (pw PassthroughWire) Name() string {
	return pw.name
}

func (pw PassthroughWire) Value(wires map[string]WireWrapper) int {
	return wires[pw.source].value
}

func (pw PassthroughWire) Sources() []string {
	return []string{pw.source}
}

type GateWire struct {
	name    string
	sources []string
	gate    int
}

func (gw GateWire) Name() string {
	return gw.name
}

func (gw GateWire) Value(wires map[string]WireWrapper) int {
	val := -1

	if wires[gw.sources[0]].value != -1 && wires[gw.sources[1]].value != -1 {
		val = binGate([]int{wires[gw.sources[0]].value, wires[gw.sources[1]].value}, gw.gate)
	}
	return val
}

func (gw GateWire) Sources() []string {
	return gw.sources
}

func binGate(sources []int, gate int) int {
	b := []string{fmt.Sprintf("%016b", sources[0]), fmt.Sprintf("%016b", sources[1])}

	val := ""

	counter := 0
	for counter < len(b[0]) {
		if gate == andGate {
			if b[0][counter] == '1' && b[1][counter] == '1' {
				val = val + "1"
			} else {
				val = val + "0"
			}
		} else if gate == orGate {
			if b[0][counter] == '1' || b[1][counter] == '1' {
				val = val + "1"
			} else {
				val = val + "0"
			}
		}

		counter++
	}

	i, _ := strconv.ParseInt(val, 2, 32)

	return int(i)
}

type NotWire struct {
	name   string
	source string
}

func (nw NotWire) Name() string {
	return nw.name
}

func (nw NotWire) Value(wires map[string]WireWrapper) int {
	val := -1

	if wires[nw.source].value != -1 {
		val = notGate(wires[nw.source].value)
	}
	return val
}

func (nw NotWire) Sources() []string {
	return []string{nw.source}
}

func notGate(source int) int {
	b := fmt.Sprintf("%016b", source)
	val := ""

	for _, c := range b {
		if c == '0' {
			val = val + "1"
		} else {
			val = val + "0"
		}
	}

	i, _ := strconv.ParseInt(val, 2, 32)
	return int(i)
}

func parseLine(line string) []Wire {
	name := strings.TrimSpace(strings.Split(line, "->")[1])
	logic := strings.TrimSpace(strings.Split(line, "->")[0])

	ws := []Wire{}

	switch len(strings.Split(logic, " ")) {
	case 3:
		if strings.Split(logic, " ")[1] == "AND" {
			s1 := strings.Split(logic, " ")[0]
			s2 := strings.Split(logic, " ")[2]

			i1, e1 := strconv.Atoi(s1)
			i2, e2 := strconv.Atoi(s2)

			if e1 == nil && e2 == nil {
				tmp1 := name + strconv.Itoa(i1)
				ws = append(ws, &StaticWire{tmp1, i1})
				tmp2 := name + strconv.Itoa(i2)
				ws = append(ws, &StaticWire{tmp2, i2})
				ws = append(ws, &GateWire{name, []string{tmp1, tmp2}, andGate})
			} else if e1 == nil && e2 != nil {
				tmp := name + strconv.Itoa(i1)
				ws = append(ws, &StaticWire{tmp, i1})
				ws = append(ws, &GateWire{name, []string{tmp, s2}, andGate})
			} else if e1 != nil && e2 == nil {
				tmp := name + strconv.Itoa(i2)
				ws = append(ws, &StaticWire{tmp, i2})
				ws = append(ws, &GateWire{name, []string{s1, tmp}, andGate})
			} else {
				ws = append(ws, &GateWire{name, []string{s1, s2}, andGate})
			}

		} else if strings.Split(logic, " ")[1] == "OR" {
			s1 := strings.Split(logic, " ")[0]
			s2 := strings.Split(logic, " ")[2]

			i1, e1 := strconv.Atoi(s1)
			i2, e2 := strconv.Atoi(s2)

			if e1 == nil && e2 == nil {
				tmp1 := name + strconv.Itoa(i1)
				ws = append(ws, &StaticWire{tmp1, i1})
				tmp2 := name + strconv.Itoa(i2)
				ws = append(ws, &StaticWire{tmp2, i2})
				ws = append(ws, &GateWire{name, []string{tmp1, tmp2}, orGate})
			} else if e1 == nil && e2 != nil {
				tmp := name + strconv.Itoa(i1)
				ws = append(ws, &StaticWire{tmp, i1})
				ws = append(ws, &GateWire{name, []string{tmp, s2}, orGate})
			} else if e1 != nil && e2 == nil {
				tmp := name + strconv.Itoa(i2)
				ws = append(ws, &StaticWire{tmp, i2})
				ws = append(ws, &GateWire{name, []string{s1, tmp}, orGate})
			} else {
				ws = append(ws, &GateWire{name, []string{s1, s2}, orGate})
			}

		} else if strings.Split(logic, " ")[1] == "LSHIFT" {
			val, _ := strconv.Atoi(strings.TrimSpace(strings.Split(logic, " ")[2]))
			ws = append(ws, &ShiftWire{name, left, val, strings.Split(logic, " ")[0]})
		} else if strings.Split(logic, " ")[1] == "RSHIFT" {
			val, _ := strconv.Atoi(strings.TrimSpace(strings.Split(logic, " ")[2]))
			ws = append(ws, &ShiftWire{name, right, val, strings.Split(logic, " ")[0]})
		}
	case 2:
		ws = append(ws, &NotWire{name, strings.TrimSpace(strings.Split(logic, " ")[1])})
	case 1:
		val, e := strconv.Atoi(strings.TrimSpace(logic))
		if e == nil {
			ws = append(ws, &StaticWire{name, val})
		} else {
			ws = append(ws, &PassthroughWire{name, strings.TrimSpace(logic)})
		}
	}

	return ws
}

func parseInput(input []string) map[string]WireWrapper {
	wiresMap := map[string]WireWrapper{}

	for _, i := range input {
		ws := parseLine(i)
		for _, w := range ws {
			wiresMap[w.Name()] = WireWrapper{w, -1}
		}
	}

	return wiresMap
}

func processWires() map[string]WireWrapper {
	tempWires := map[string]WireWrapper{}

	for k, v := range wires {
		tempWires[k] = v
	}

	for len(tempWires) > 0 {
		for _, w := range tempWires {
			val := w.wire.Value(wires)
			if val != -1 {
				wires[w.wire.Name()] = WireWrapper{w.wire, val}
				delete(tempWires, w.wire.Name())
			}
		}
	}

	return wires
}

func processWires2(wireName string) int {
	fmt.Println(wireName)
	for _, w := range wires[wireName].wire.Sources() {
		if wires[w].value == -1 {
			val := processWires2(w)
			if val == 0 {
				fmt.Println(wires[w].wire)
			}
			wires[w] = WireWrapper{wires[w].wire, val}
		}
	}
	return wires[wireName].wire.Value(wires)
}

func main() {
	input := splitLines(readFile("day7.dat"))

	wires = parseInput(input)

	//fmt.Println(wiresMap)
	//fmt.Println(processWires(wiresMap))

	processedWires := processWires()

	for k, v := range processedWires {
		fmt.Println(k + ": " + strconv.Itoa(v.value))
	}

	fmt.Println(processedWires["a"].value)

	//fmt.Println(notGate(0))

	//fmt.Println(processWires2("a"))
}
