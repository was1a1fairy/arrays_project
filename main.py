from arrays_lib import *
from logger import *

def user_input():

    while True:
        elem = input('inpt elem: ')

        if elem[0] == '-':
            elem = elem[1::]
            if elem.isdigit():
                elem = -int(elem)
                break
            else:
                print('net ^_^')
                break

        else:
            if elem.isdigit():
                elem = int(elem)
                break
            else:
                print('net ^_^')
                continue
    
    return elem

def input_count_1d():
    while True:
        count_1 = input('input count for arr: ')

        if count_1.isdigit():
            count_1 = int(count_1)

            if count_1 == 0:
                print('количество не может быть нулевым')
                continue
            else:
                break

        else:
            print('net ^_^')
            continue
    
    return count_1

def input_arr(count_1):
    import random
    n = count_1

    arr = [random.randint(-9, 9) for i in range(n)]

    return arr

def input_count_matrix():
    while True:
        line = input('input count for matrix line: ')

        if line.isdigit():
            line = int(line)

            if line == 0:
                print('количество не может быть нулевым')
                continue
            else:
                break

        else:
            print('net ^_^')
            continue
    
    while True:
        col = input('input count for matrix col: ')

        if col.isdigit():
            col = int(col)

            if col == 0:
                print('количество не может быть нулевым')
                continue
            else:
                break

        else:
            print('net ^_^')
            continue
    
    return line, col

def input_matrix(line, col):
    from random import randint

    matrix = [[randint(-9, 9) for i in range(line)] for j in range(col)]

    return matrix

def input_value():
    value = input('input value: ')
    if value.isdigit():
        value = int(value)
    else:
        value = 'value incorrect'
    return value


def main():
    count_1 = input_count_1d()
    arr = input_arr(count_1)
    log_action('array:')
    log_action(str(arr))

    line, col = input_count_matrix()
    matrix = input_matrix(line, col)
    log_action('matrix:')
    log_action(str(matrix))

    value = input_value()

    sum = summ_1d(arr)
    log_action('(:function call sum')
    log_action(str(sum))

    prod_1 = prod_1d(arr)
    log_action('(:function call prod_1')
    log_action(str(prod_1))

    mean_1 = mean_1d(arr)
    log_action('(:function call mean_1')
    log_action(str(mean_1))

    max_1 = max(arr)
    log_action('(:function call max')
    log_action(str(max_1))

    min_1 = min_elem(arr)
    log_action('(:function call min')
    log_action(str(min_1))

    sum_2 = sum_2d(matrix)
    log_action('(:function call sum_2')
    log_action(str(sum_2))

    prod_2 = prod_2d(matrix)
    log_action('(:function call prod_2')
    log_action(str(prod_2))

    mean_2 = mean_2d(matrix)
    log_action('(:function call mean_2')
    log_action(str(mean_2))

    max_2 = max_2d(matrix)
    log_action('(:function call max_2')
    log_action(str(max_2))

    min_2 = min_2d(matrix)
    log_action('(:function call min_2')
    log_action(str(min_2))

    arr1, arr2 = [1, 2, 3], [4, 5, 6]
    sum_array = sum_arrays(arr1, arr2)
    log_action('(:function call sum arrays')
    log_action(str(sum_array))

    diff_array = diff_arrays(arr1, arr2)
    log_action('(:function call diff arrays')
    log_action(str(diff_array))

    prod_array = prod_arrays(arr1, arr2)
    log_action('(:function call prod arrays')
    log_action(str(prod_array))

    lower = lower_triangle(matrix)
    log_action('(:function call lower matrix')
    log_action(str(lower))

    upper = upper_triangle(matrix)
    log_action('(:function call upper matrix')
    log_action(str(upper))

    left = left_triangle(matrix)
    log_action('(:function call left matrix')
    log_action(str(left))

    right = right_triangle(matrix)
    log_action('(:function call right matrix')
    log_action(str(right))

    less = filter_less(arr, value)
    log_action('(:function call filter_less')
    log_action(str(less))

    greater = filter_greater(arr, value)
    log_action('(:function call filter_greater')
    log_action(str(greater))

    equal = filter_equal(arr, value)
    log_action('(:function call filter_equal')
    log_action(str(equal))

    not_equal = filter_not_equal(arr, value)
    log_action('(:function call filter_not_equal')
    log_action(str(not_equal))

main()