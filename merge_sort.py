# runing time complexity is O(nlogn)
def merge(A, start, mid, end):
    left = A[start:mid]
    right = A[mid+1:]
    print(left,'and', right)


def merge_sort(A, start, end):
    if start < end:
        mid = int((start + end) / 2)
        merge_sort(A, start, mid)
        merge_sort(A, mid + 1, end)
        merge(A, start, mid, end)

s = [1,3,5,2,1]
merge_sort(s, 0, len(s))
print(s)