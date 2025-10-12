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

func quickSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}

	pivot := arr[len(arr)/2]
	var left, middle, right []int

	for _, x := range arr {
		if x < pivot {
			left = append(left, x)
		} else if x == pivot {
			middle = append(middle, x)
		} else {
			right = append(right, x)
		}
	}

	result := make([]int, 0, len(arr))
	result = append(result, quickSort(left)...)
	result = append(result, middle...)
	result = append(result, quickSort(right)...)

	return result
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
	
	fmt.Printf("Linguagem: Go %s\n", runtime.Version())
	fmt.Printf("Sistema: %s\n", runtime.GOOS)
	fmt.Printf("Arquitetura: %s\n", runtime.GOARCH)
	fmt.Printf("Algoritmo: Quick Sort\n")
	fmt.Println(strings.Repeat("-", 50))

	
	resultadosFolder := "resultados"
	if _, err := os.Stat(resultadosFolder); os.IsNotExist(err) {
		os.Mkdir(resultadosFolder, 0755)
	}

	
	inputFile := "input.txt"
	outputFile := "resultados/arq-saida-go-quick.txt"

	numbers, err := readNumbersFromFile(inputFile)
	if err != nil {
		fmt.Printf("Erro ao ler arquivo: %v\n", err)
		return
	}

	
	runtime.GC()
	runtime.GC()
	
	memoryBefore := getMemoryUsage()

	
	startTime := time.Now()

	
	numbersCopy := make([]int, len(numbers))
	copy(numbersCopy, numbers)
	sortedNumbers := quickSort(numbersCopy)

	endTime := time.Now()

	
	memoryAfter := getMemoryUsage()
	memoryUsed := float64(memoryAfter-memoryBefore) / 1024 

	
	err = writeNumbersToFile(outputFile, sortedNumbers)
	if err != nil {
		fmt.Printf("Erro ao escrever arquivo: %v\n", err)
		return
	}

	
	executionTimeMs := float64(endTime.Sub(startTime).Nanoseconds()) / 1000000
	fmt.Printf("Tempo de execução: %.2f ms\n", executionTimeMs)
	fmt.Printf("Memoria utilizada: %.2f KB\n", memoryUsed)
	fmt.Printf("Arquivo de saída: %s\n", outputFile)
}