# time complexity O(n^2)
def bubble_sort(A):
    for i in range(len(A)):
        for j in range(i, len(A)):
            if A[j] <= A[i]:
                A[i], A[j] = A[j], A[i]
    return A

if __name__ == "__main__":
    # try to change the array
    A = [1,3,2,4,1,5,3,2]
    A = bubble_sort(A)
    print(A)