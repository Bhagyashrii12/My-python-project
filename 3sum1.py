def threeSumClosest(nums, target):
    nums.sort()
    # Initialize with the sum of the first three elements
    closest_sum = sum(nums[:3])
    
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            # If we find the exact target, return it
            if current_sum == target:
                return current_sum
            
            # Update closest_sum if the current_sum is nearer to target
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            
            # Move pointers based on comparison with target
            if current_sum < target:
                left += 1
            else:
                right -= 1
                
    return closest_sum
