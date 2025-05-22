def summ_1d(arr):
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

def compare_arrays(arr1,arr2):
    res = []
    def arr1_compare(arr1,arr2):
        for i in range(len(arr1)):
            if arr1[i]>arr2[i]:
                res.append(True)
            else:
                res.append(False)
    def arr2_compare(arr1,arr2):
        for i in range(len(arr1)):
            if arr2[i]>arr1[i]:
                res.append(True)
            else:
                res.append(False)
    def equation_compare(arr1,arr2):
        for i in range(len(arr1)):
            if arr1[i]==arr2[i]:
                res.append(True)
            else:
                res.append(False)
    return arr1_compare(arr1, arr2), arr2_compare(arr1, arr2), equation_compare(arr1,arr2)