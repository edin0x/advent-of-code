package main

import (
  "bufio"
  "fmt"
  "os"
  "strconv"
)

func main() {
  file, _ := os.Open("input")
  scanner := bufio.NewScanner(file)
  var numbers []int
  for scanner.Scan() {
      lineStr := scanner.Text()
      num, _ := strconv.Atoi(lineStr)
      numbers = append(numbers, num)
  }

  var l = len(numbers)
  var i, steps, move = 0, 0, 0

  for {
    steps += 1
    move = numbers[i]
    if (i + numbers[i] >= l) {
      break;
    }

    if (move >= 3) {
      numbers[i] -= 1
    } else {
      numbers[i] += 1
    }


    i += move
  }

  fmt.Println(steps)
}
