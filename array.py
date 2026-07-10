def find_median_two_pointer(nums1, nums2):
    m, n = len(nums1), len(nums2)
    total = m + n
    half = total // 2
    
    i = j = count = 0
    curr = prev = 0
    
    while count <= half:
        prev = curr
        if i < m and (j >= n or nums1[i] <= nums2[j]):
            curr = nums1[i]
            i += 1
        else:
            curr = nums2[j]
            j += 1
        count += 1
        
    if total % 2 != 0:
        return float(curr)
    return (prev + curr) / 2.0
