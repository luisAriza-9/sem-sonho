function diagonalDifference(arr) {
    let primaryDiagonal = 0, secondaryDiagonal = 0;
    for(let i = 0; i < arr.length; i++) {
        primaryDiagonal += arr[i][i];
        secondaryDiagonal += arr[i][arr.length - i - 1];
    }
    return Math.abs(primaryDiagonal - secondaryDiagonal);
}

// Ejemplo de uso:
const matrix = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
];

console.log(diagonalDifference(matrix)); // Salida: 15


