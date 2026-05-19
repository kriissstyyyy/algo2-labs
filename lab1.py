def bubble_sort_descending(array):
    temp = array.copy()
    length = len(temp)
    for i in range(length):
        for j in range(length - i - 1):
            if temp[j] < temp[j + 1]:
                temp[j], temp[j + 1] = temp[j + 1], temp[j]
    return temp

def find_kth_largest(array, k):
    if k < 1 or k > len(array):
        raise ValueError(f"k must be between 1 to {len(array)}")

    sorted_array = bubble_sort_descending(array)
    kth_value = sorted_array[k - 1]
    position = array.index(kth_value)

    return kth_value, position
