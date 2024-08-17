def bubble_sort(arr: list) -> list:
    n = len(arr)
    for x in range(n):
        swapped = False
        for y in range(n-x-1):
            if arr[y] > arr[y + 1]:
                arr[y], arr[y + 1] = arr[y + 1], arr[y]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    l = [6, 8, 3, 2, 9, 5]
    m = [9,3,4,5]
    sorted_l = bubble_sort(m)
    print(sorted_l)
