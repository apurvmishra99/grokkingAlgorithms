def binary_search(arr, key):
    low = 0             # initialising base values for low and high
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2 # "//" for integral division

        if key == arr[mid]:
            return mid
        elif key > arr[mid]:
            low = mid + 1
        elif key < arr[mid]:
            high = mid - 1
    return None # if the key is not found

if __name__ == "__main__":
    arr = sorted(list(input("Enter the sorted list: ").split(" ")))
    key = input("The key to find is: ")
    print(arr)
    if binary_search(arr, key) is not None:
        print(f"The key was found at the index: {binary_search(arr, key)}.")
    else:
        print(f"The key was not found")
    