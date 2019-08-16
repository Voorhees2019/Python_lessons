arr = [142, 34, 242, 23, 54, 2, 52, 23]

# ---------------buble_search alghoritm----------------
for i in range(len(arr)-1):
    for j in range(1, len(arr)):
        if arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]


print(arr)
