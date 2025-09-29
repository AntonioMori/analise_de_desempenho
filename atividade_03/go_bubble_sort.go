package main

import (
	"bufio"
	"fmt"
	"os"
	"runtime"
	"strconv"
	"strings"
	"time"
)

func bubbleSort(arr []int) []int {
	n := len(arr)
	for i := 0; i < n; i++ {
		for j := 0; j < n-i-1; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
			}
		}
	}
	return arr
}

func readNumbersFromFile(filename string) ([]int, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var numbers []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		if line != "" {
			num, err := strconv.Atoi(line)
			if err != nil {
				return nil, err
			}
			numbers = append(numbers, num)
		}
	}
	return numbers, scanner.Err()
}

func writeNumbersToFile(filename string, numbers []int) error {
	file, err := os.Create(filename)
	if err != nil {
		return err
	}
	defer file.Close()

	writer := bufio.NewWriter(file)
	for _, num := range numbers {
		fmt.Fprintf(writer, "%d\n", num)
	}
	return writer.Flush()
}

func getMemoryUsage() uint64 {
	var m runtime.MemStats
	runtime.ReadMemStats(&m)
	return m.Alloc
}

func main() {
	// System information
	fmt.Printf("Linguagem: Go %s\n", runtime.Version())
	fmt.Printf("Sistema: %s\n", runtime.GOOS)
	fmt.Printf("Arquitetura: %s\n", runtime.GOARCH)
	fmt.Printf("Algoritmo: Bubble Sort\n")
	fmt.Println(strings.Repeat("-", 50))

	// Create resultados folder if it doesn't exist
	resultadosFolder := "resultados"
	if _, err := os.Stat(resultadosFolder); os.IsNotExist(err) {
		os.Mkdir(resultadosFolder, 0755)
	}

	// Read input file
	inputFile := "input.txt"
	outputFile := "resultados/arq-saida-go-bubble.txt"

	numbers, err := readNumbersFromFile(inputFile)
	if err != nil {
		fmt.Printf("Erro ao ler arquivo: %v\n", err)
		return
	}

	// Force garbage collection before measurement
	runtime.GC()
	runtime.GC() // Call twice to ensure cleanup

	// Measure memory before sorting
	memoryBefore := getMemoryUsage()

	// Measure execution time
	startTime := time.Now()

	// Create a copy for sorting
	numbersCopy := make([]int, len(numbers))
	copy(numbersCopy, numbers)
	sortedNumbers := bubbleSort(numbersCopy)

	endTime := time.Now()

	// Measure memory after sorting
	memoryAfter := getMemoryUsage()
	memoryUsed := float64(memoryAfter-memoryBefore) / 1024 // Convert to KB

	// Write output file
	err = writeNumbersToFile(outputFile, sortedNumbers)
	if err != nil {
		fmt.Printf("Erro ao escrever arquivo: %v\n", err)
		return
	}

	// Print results
	executionTimeMs := float64(endTime.Sub(startTime).Nanoseconds()) / 1000000
	fmt.Printf("Tempo de execução: %.2f ms\n", executionTimeMs)
	fmt.Printf("Memoria utilizada: %.2f KB\n", memoryUsed)
	fmt.Printf("Arquivo de saída: %s\n", outputFile)
}