def bubble_sort(arr):
    n = len(arr)
    # print(n)
    swapped = False

    for i in range(n):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break


arr = [10, 30, 5, 10, 40]
print('before sorted array: -', arr)
bubble_sort(arr)
print('after sorted array is: ', arr)
