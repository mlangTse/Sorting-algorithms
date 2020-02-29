# time complexity O(n^2)
def selection_sort(A):
    for i in range(len(A)):
        # the smallest index in a not sorted part
        minIndex = i
        for j in range(i+1, len(A)):
            if A[j] < A[minIndex]:
                minIndex = j
        if minIndex != i:
            A[minIndex], A[i] = A[i], A[minIndex]
    return A

if __name__ == "__main__":
    # try to change the array
    A = [1,5,6,1,2,3,43,2]
    A = selection_sort(A)
    print(A)