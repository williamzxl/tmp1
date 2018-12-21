def sum(arr):
    if len(arr) == 1:
        print("Arr",arr)
        return arr[0]
    else:
        print(arr, arr[0])
        total = arr[0] + sum(arr[1:])
        print(total)
        return total

a = sum([1, 2, 3, 7, 10])
print(a)