def find_peak(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left


arr = [1, 3, 7, 12, 9, 5, 2]

peak = find_peak(arr)

print("Peak index:", peak)
print("Peak value:", arr[peak])
