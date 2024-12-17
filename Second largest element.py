# Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

# Note: The second largest element should not be equal to the largest element.



def getSecondLargest( arr):
    # Code Here
    largest=arr[0]
    for element in arr:
        if element>largest:
            largest=element
    second=-1
    for element in arr:
        if element<largest and element>second:
            second=element
    
    return second


arr= [12, 35, 1, 10, 34, 1]
print(getSecondLargest(arr))