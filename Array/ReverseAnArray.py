#Using Recursion Method

def reverse(arr,s,e):
    if s>=e:
        return
    arr[s], arr[e] = arr[e], arr[s]
    reverse(arr,s+1,e-1)
    
arr = list(map(int, input().split("#")))
reverse(arr,0,len(arr)-1)
print(arr)





#Using Iterative Method

def reverse(arr):
    s = 0
    e = len(arr)-1
    while s<e:
        arr[s], arr[e] = arr[e], arr[s]
        s += 1 
        e -= 1 
    return arr
    
arr = list(map(int, input().split("#")))
reverse(arr)
print(arr)
