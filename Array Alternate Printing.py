# You are given an array arr[], 
# the task is to return a list 
# elements of arr in alternate 
# order (starting from index 0).

#User function Template for python3

def getAlternates( arr):
    
    # Code Here
    a=[]
    for i in range(0,len(arr),2):
        a.append(arr[i])
        
    return a

arr=[1,2,3,4,5,6,7]
print(getAlternates(arr))

