def summ_1d(arr -> list) -> int:
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