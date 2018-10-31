def quicksort(arr):
    if arr==[]:
        return []
    base=arr[0]
    lower=[]
    higher=[]
    t=[]
    t.append(base)

    for i in range(1,len(arr)):
        if arr[i]<=base:
            lower.append(arr[i])
        if arr[i]>base:
            higher.append(arr[i])
    return quicksort(lower)+t+quicksort(higher)