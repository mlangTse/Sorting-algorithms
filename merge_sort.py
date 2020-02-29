# runing time complexity is O(nlogn)
def merge(A, start, mid, end):
    # seqarate list A to two part
    left = A[start:mid+1]
    right = A[mid+1:end+1]

    i, j = 0, 0
    for k in range(start, end+1):
        if j == len(right) or (i < len(left) and left[i] <= right[j]):
            A = A[:k] + [left[i]] + A[k+1:]
            i += 1
        else:
            A = A[:k] + [right[j]] + A[k+1:]
            j += 1
    return A

def merge_sort(A, start, end):
    if start < end:
        mid = int((start + end) / 2)
        A = merge_sort(A, start, mid)
        A = merge_sort(A, mid + 1, end)
        A = merge(A, start, mid, end)
    return A

s = [1,5,6,1,2,3,43,2]
s = merge_sort(s, 0, len(s)-1)
