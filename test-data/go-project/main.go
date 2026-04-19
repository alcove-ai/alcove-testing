package main

import "fmt"

// Add takes two integers a and b and returns their sum.
// This function performs basic integer addition and returns
// the result as an integer.
//
// Example:
//   result := Add(2, 3)  // result will be 5
func Add(a, b int) int {
	return a + b
}

// Multiply takes two integers a and b and returns their product.
// This function performs basic integer multiplication and returns
// the result as an integer.
//
// Example:
//   result := Multiply(4, 5)  // result will be 20
func Multiply(a, b int) int {
	return a * b
}

// main is the entry point of the program.
// It demonstrates the usage of Add and Multiply functions
// by printing their results to standard output.
func main() {
	fmt.Println("2 + 3 =", Add(2, 3))
	fmt.Println("4 * 5 =", Multiply(4, 5))
}
