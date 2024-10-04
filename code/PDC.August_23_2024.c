#include <iostream>
#include <thread>
#include <vector>
#include <random>

void fillRowWithRandom(int* row, int cols) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dist(0, 99);

    for (int i = 0; i < cols; i++) {
        row[i] = dist(gen); // Genera un número aleatorio entre 0 y 99
    }
}

int main() {
    const int rows = 5;
    const int cols = 5;
    int matrix[rows][cols];
    std::vector<std::thread> threads;

    // Crear y lanzar los threads
    for (int i = 0; i < rows; i++) {
        threads.emplace_back(fillRowWithRandom, matrix[i], cols);
    }

    // Esperar a que todos los threads terminen
    for (auto& th : threads) {
        th.join();
    }

    // Imprimir la matriz
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}
