package main

import "fmt"


func is_prime(int a) bool {
	/* Проверяет, является ли число простым. */
	if (a < 2) return false;

	for (int i = 2; i <= (int)sqrt(a); i++) {
		if (a % i == 0) return false;
	}

	return true;
}


func calculateNthNum(int a) int {
	/*  */
}


func main() {

}