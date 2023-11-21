def pylons(k, arr):
    n = len(arr)
    i = 0
    count = 0
    while i < n:
        j = min(i + k - 1, n - 1)
        found_plant = False  # Flag to check if a suitable city is found within the coverage range
        while j >= max(0, i - k + 1):
            if arr[j] == 1:
                count += 1
                i = j + k
                found_plant = True
                break
            j -= 1
        # If no suitable city found within the coverage range, return -1
        if not found_plant:
            return -1

    return count
