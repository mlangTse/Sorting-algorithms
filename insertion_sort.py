# time complxity O(n^2)
def insertion_sort(A):
    for i in range(len(A)):
        key = A[i]
        j = i - 1
        while j > 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A

if __name__ == "__main__":
    # try to change the array
    A = [1,5,6,1,2,3,43,2]
    A = insertion_sort(A)
    print(A)