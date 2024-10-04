import java.util.Random;

class FillMatrixTask implements Runnable {
    private int[][] matrix;
    private int row;

    public FillMatrixTask(int[][] matrix, int row) {
        this.matrix = matrix;
        this.row = row;
    }

    @Override
    public void run() {
        Random random = new Random();
        for (int i = 0; i < matrix[row].length; i++) {
            matrix[row][i] = random.nextInt(100); // Genera un número aleatorio entre 0 y 99
        }
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        int rows = 5;
        int cols = 5;
        int[][] matrix = new int[rows][cols];
        Thread[] threads = new Thread[rows];

        // Crear y lanzar los threads
        for (int i = 0; i < rows; i++) {
            threads[i] = new Thread(new FillMatrixTask(matrix, i));
            threads[i].start();
        }

        // Esperar a que todos los threads terminen
        for (int i = 0; i < rows; i++) {
            threads[i].join();
        }

        // Imprimir la matriz
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }
}
