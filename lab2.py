def is_possible(positions, C, min_dist):
    count = 1
    last_position = positions[0]
    for i in range(1, len(positions)):
        if positions[i] - last_position >= min_dist:
            count += 1
            last_position = positions[i]
        if count == C:
            return True
    return False


def counting_sort(arr):
    if not arr:
        return arr
    
    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1
    
    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1
    
    sorted_arr = []
    for i, freq in enumerate(count):
        if freq > 0:
            sorted_arr.extend([i + min_val] * freq)
    
    return sorted_arr


def largest_min_distance(N, C, free_sections):
    sorted_sections = counting_sort(free_sections)
    
    left = 0
    right = sorted_sections[-1] - sorted_sections[0]
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        if is_possible(sorted_sections, C, mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result