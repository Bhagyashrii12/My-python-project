def threeSum(nums):
    res = []
    nums.sort()  # Sort to handle duplicates and use two pointers

    for i, a in enumerate(nums):
        # Skip the same value as the previous element to avoid duplicate triplets
        if i > 0 and a == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            three_sum = a + nums[l] + nums[r]
            if three_sum > 0:
                r -= 1
            elif three_sum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                # Skip duplicate values for the second element
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
                    
    return res
