def minmax(arr,a,b):
    for i in range(1,len(arr)):
        if arr[i]>a:
            a = arr[i]
        if arr[i]<b:
            b = arr[i]
    return a,b
      
    
arr = list(map(int,input().split(",")))
print(minmax(arr,arr[0],arr[0]))
