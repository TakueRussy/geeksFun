# Given an array arr. Your task is to find the minimum and maximum elements in the array.

# Note: Return an array that contains two elements the first one will be a minimum element and the second will be a maximum of an array.


def get_min_max(arr):
    smallest,largest=arr[0],arr[0]
    for element in arr:
        if element < smallest:
            smallest=element
        elif element>largest:
            largest= element
            
    return [smallest,largest]

arr = [3, 2, 1, 56, 10000, 167]
print(get_min_max(arr))
