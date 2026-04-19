package main

import "testing"

func TestAdd(t *testing.T) {
	tests := []struct {
		a, b, want int
	}{
		{2, 3, 5},
		{0, 0, 0},
		{-1, 1, 0},
		{10, -5, 5},
	}
	for _, tc := range tests {
		got := Add(tc.a, tc.b)
		if got != tc.want {
			t.Errorf("Add(%d, %d) = %d, want %d", tc.a, tc.b, got, tc.want)
		}
	}
}

func TestMultiply(t *testing.T) {
	tests := []struct {
		a, b, want int
	}{
		{4, 5, 20},
		{0, 100, 0},
		{-3, 7, -21},
	}
	for _, tc := range tests {
		got := Multiply(tc.a, tc.b)
		if got != tc.want {
			t.Errorf("Multiply(%d, %d) = %d, want %d", tc.a, tc.b, got, tc.want)
		}
	}
}
