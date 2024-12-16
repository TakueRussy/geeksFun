# Given an array arr, complete the following three functions:
# searchEle: This function searches for an element x in the array arr. It should return a boolean value - true if the element is found, and false otherwise.
# insertEle: This function inserts an element y at index yi in the array. true will be printed if the insertion is done correctly, and false otherwise.
# deleteEle: This function deletes the first occurrence of an element z in the array. true will be printed if the deletion is done correctly, and false otherwise.

#  Note: 0-based indexing is followed.


    
def searchEle(arr, x):
    
    # Code here
    
    for i in range(len(arr)):
        if x==arr[i]:
            return True
    return False
    

# insert element if you have inserted properly 1 will be printed else 0
def insertEle(arr, y, yi):
    # Code here
    if len(arr)==yi:
        arr.append(y)
        print(arr)
        return True
    elif len(arr)>yi:
        first= arr[:yi]
        last=arr[yi:]
        arr[yi]=[y]
        final= first + arr[yi] +last
        print(final)
        return True
    else:
        return False
    
        

# delete element if you have deleted properly 1 will be printed else 0
def deleteEle(arr, z):
    # Code here
    if (z in arr):
        pos=arr.index(z)
        if pos==0:
            if len(arr)>1:
                print(arr[1:])
            else:
                print([])
        else:
            first=arr[:pos]
            if (len(arr)>pos+1):
                last=arr[pos+1:]
            else:
                last=[]
            ans=first +last
            print(ans)
            return True
            
    else:
        return False
                
arr=[1,2,3,4,5,6]      
        