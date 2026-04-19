package main

import "fmt"

// Add returns the sum of two integers.
func Add(a, b int) int {
	return a + b
}

// Multiply returns the product of two integers.
func Multiply(a, b int) int {
	return a * b
}

func main() {
	fmt.Println("2 + 3 =", Add(2, 3))
	fmt.Println("4 * 5 =", Multiply(4, 5))
}
