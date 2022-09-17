from ctypes import sizeof

def partition2(arr,l,h):
    pivot=arr[h]
    i=l-1
    for j in range(l,h):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return i+1              



def quick_sort(arr,i,j):
    if i<j:
        piv=partition2(arr,i,j)
        quick_sort(arr,i,piv-1)
        quick_sort(arr,piv+1,j)


arr=[1,2,5,0,15,7,35,20,-1]
n=len(arr)
quick_sort(arr,0,n-1)
print(arr)
