
def Search(arr, target):
    i=0
    while i < len(arr):
        if arr[i] == target:
            return i
        i += 1
    return -1

arr = ["Anshul", "Aman", "HArshit", "Harsh", "Ankit", "Anshika", "Anjali"]
target = input("Enter the name to search: ")
result = Search(arr, target)
print("Element found at index:", result)