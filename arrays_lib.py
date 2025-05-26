def summ_1d(arr: list) -> int:
    summ=0
    for i in range(len(arr)):
        summ+=arr[i]
    return summ

def mean_1d(arr):
    return summ_1d(arr)/len(arr)

def min_elem(arr):
    min=arr[0]
    for i in range(len(arr)):
        if arr[i]<min:
            min=arr[i]
    return min

def max_elem(arr):
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

def prod_1d(arr):
    prod=1
    for i in range(len(arr)):
        prod*=arr[i]
    return prod

def sum_2d(matrix):
    summ=0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            summ+=matrix[i][j]
    return summ

def prod_2d(matrix):
    prod=1
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            prod*=matrix[i][j]
    return prod

def mean_2d(matrix):
    return mean_2d(matrix)/len(matrix)

def max_2d(matrix):
    max=matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if max<matrix[i][j]:
                max=matrix[i][j]
    return max

def min_2d(matrix):
    min = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if min>matrix[i][j]:
                min=matrix[i][j]
    return min

def sum_arrays(arr1, arr2):
    if len(arr1) == len(arr2):
        sum_elem_arrs = []

        for i in range(len(arr2)):
            sum_elems = arr1[i] +arr2[i]
            sum_elem_arrs.append(sum_elems)
            
    return sum_elem_arrs

def diff_arrays(arr1, arr2):
    if len(arr1) == len(arr2):
        diff_elem_arrs = []

        for i in range(len(arr2)):
            diff_elems = arr1[i] - arr2[i]
            diff_elem_arrs.append(diff_elems)

    return diff_elem_arrs

def prod_arrays(arr1, arr2):
    if len(arr1) == len(arr2):
        prod_elem_arrs = []

        for i in range(len(arr2)):
            prod_elems = arr1[i] * arr2[i]
            prod_elem_arrs.append(prod_elems)

    else:
        print('длина должна быть одинаковая, проверка не пройдена(((((((((')


    return prod_elem_arrs

def compare_arrays(arr1, arr2):
    if len(arr1) == len(arr2):
        compare_elem_arrs = []

        for i in range(len(arr2)):

            if arr1[i] > arr2[i]:
                compare_elem_arrs.append('>')
            elif arr1[i] < arr2[i]:
                compare_elem_arrs.append('<')
            else:
                compare_elem_arrs.append('=')

        else:
            print('длина должна быть одинаковая, проверка не пройдена(((((((((')

    return compare_elem_arrs

def lower_triangle(matrix):
    new = []

    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):

            if j <= i:
                row.append(matrix[i][j])
            else:
                row.append(0)
                
        new.append(row)

    return new

def upper_triangle(matrix):
    new = []

    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):

            if j >= i:
                row.append(matrix[i][j])
            else:
                row.append(0)
                
        new.append(row)

    return new

def left_triangle(matrix):
    new = []

    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):

            if j < (len(matrix[i]) + 1) // 2:
                row.append(matrix[i][j])
            else:
                row.append(0)
                
        new.append(row)

    return new

def right_triangle(matrix):
    new = []

    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):

            if j > (len(matrix[i])) // 2:
                row.append(matrix[i][j])
            else:
                row.append(0)
                
        new.append(row)

    return new

def filter_less(arr: list, value):
    min_value = []

    for i in range(len(arr)):

        if arr[i] < value:
            min_value.append(arr[i])

    return min_value

def filter_not_equal(arr: list, value):
    not_equal_value = []

    for i in range(len(arr)):

        if arr[i] == value:
            not_equal_value.append(arr[i])

    return not_equal_value