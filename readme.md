# arrays_lib
<<<<<<< HEAD
1. функция для поиска суммы элементов одномерного массива **sum_1d(arr: list) -> int or float**
- input data: list: [1, 2, 3]
- output data: int: 6

2. функция для поиска произведения элементов массива **prod_1d(arr:list) -> int or float**
- input data: list: [2, 2, 3]
- output data: int: 12

3. функция для поиска среднего арифметического элементов одномерного массива **mean_1d(arr:list) -> int or float**
- input data: list: [2, 2, 3]
- output data: int: 2.33

4. функция для поиска максимального элемента одномерного массива **max(arr:list) -> int or float**
- input data: list: [2, 2, 3]
- output data: int: 3

5. функция для поиска минимального элемента одномерного массива **min_1d(arr:list) -> int or float**
- input data: list: [1, 2, 3]
- output data: int: 1

### матрицы

6. функция для поиска суммы элементов двумерного массива **sum_2d(matrix: list[list]) -> int or float**
- input data: list: [[1, 2, 3],[4, 5, 6]]
- output data: int: 21

7. функция для поиска произведения элементов двумерного массива **prod_2d(matrix: list[list]) -> int or float**
- input data: list: [[1, 2, 3],[4, 5, 6]]
- output data: int: 720

8. функция для поиска среднего арифметического элементов двумерного массива **mean_2d(matrix: list[list]) -> int or float**
- input data: list: [[1, 2, 3],[4, 5, 6]]
- output data: int: 3.5

9. функция для поиска максимального элемента двумерного массива **max_2d(matrix: list[list]) -> int or float**
- input data: list: [[1, 2, 3],[4, 5, 6]]
- output data: int: 6

10. функция для поиска минимального элемента двумерного массива **min_2d(matrix: list[list]) -> int or float**
- input data: list: [[1, 2, 3],[4, 5, 6]]
- output data: int: 1

### работа с двумя массивами

11. сумма для поэлементного сложения массивов **sum_arrays(arr1: list, arr2: list) -> list**
- input data: arr1: [1, 2, 3]; arr2: [4, 5, 6]
- output data: int: [5, 7, 9]

12. сумма для поэлементного умножения массивов **prod_arrays(arr1: list, arr2: list) -> list**
- input data: arr1: [1, 2, 3]; arr2: [4, 5, 6]
- output data: int: [4, 10, 18]

13. функция для поэлементного сравнения массивов **compare_arrays(arr1: list, arr2: list) -> list**
- input data: arr1: [1, 20, 6]; arr2: [4, 5, 6]
- output data: int: [<, >, =]

### обходы треугольников

14. функция для обхода нижнего треугольника матрицы  **lower_triangle(matrix: list[list]) -> int or float**
- input data: list: [[1, 2],[4, 5]]
- output data: int: [[1, 0], [4, 5]]

15. функция для обхода верхнего треугольника матрицы  **upper_triangle(matrix: list[list]) -> int or float**
- input data: list: [[1, 2],[4, 5]]
- output data: int: [[1, 2], [0, 5]]

16. функция для обхода левого треугольника матрицы  **left_triangle(matrix: list[list]) -> int or float**
- input data: list: [[1, 2],[4, 5]]
- output data: int: [[1, 0], [4, 0]]

17. функция для обхода правого треугольника матрицы  **right_triangle(matrix: list[list]) -> int or float**

- input data: list: [[1, 2],[4, 5]]
- output data: int: [[0, 2], [0, 5]]

18. функция для нахождения элементов, больших заданного значения **filter_greater(arr: list, value: int) -> list**
- input data: list: [1, 2, 3, 4], int: 2
- output data: list: [3, 4]

19. функция для нахождения элементов, меньших заданного значения **filter_less(arr: list, value: int) -> list**
- input data: list: [1, 2, 3, 4], int: 3
- output data: list: [1, 2]

20. функция для нахождения элементов, равных заданному значению **filter_equal(arr: list, value: list) -> list**
- input data: list: [1, 2, 3, 4], int: 3
- output data: list[3]

- input data: list: [1, 2, 2, 3], int: 2
- output data: list[2, 2]

21. функция для нахождения элементов, равных заданному значению **filter_not_equal(arr: list, value: int) -> list**
- input data: list: [1, 2, 3, 4], int: 3
- output data: list: [1, 2, 4]