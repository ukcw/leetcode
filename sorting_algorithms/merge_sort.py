
def mergeSort(array):
    if len(array) > 1:
        mid = len(array)//2

        L = array[:mid]
        R = array[mid:]

        mergeSort(L)
        mergeSort(R)

        l = r = k = 0

        while l < len(L) and r < len(R):
            if L[l] <= R[r]:
                array[k] = L[l]
                l += 1
            else:
                array[k] = R[r]
                r += 1
            k += 1

        while l < len(L):
            array[k] = L[l]
            l += 1
            k += 1

        while r < len(R):
            array[k] = R[r]
            r += 1
            k += 1

if __name__ == "__main__":
    arr = [5,4,3,2,1]
    arr2 = [1]
    arr3 = [1,3,2]
    arr4 = [1,3,2,4]
    mergeSort(arr)
    mergeSort(arr2)
    mergeSort(arr3)
    mergeSort(arr4)
    print(arr)
    print(arr2)
    print(arr3)
    print(arr4)
