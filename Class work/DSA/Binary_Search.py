# Binary Search Implementation
arr=[ 10, 20, 30, 40, 50 ]

target= int(input("Enter the target value to search: "))

def binary_search(arr,target):
    start=0
    end=len(arr)-1

    while start<=end:
        mid=(start+end)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return -1
binary_search(arr,target)
print("The index of the target value is: ",binary_search(arr,target))
