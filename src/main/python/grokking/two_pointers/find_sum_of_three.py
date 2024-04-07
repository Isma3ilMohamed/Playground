def find_sum_of_three(nums: list[int], target: int) -> bool:
    nums.sort()

    for i in range(0, len(nums) - 2):
        low = i + 1
        high = len(nums) - 1
        while low < high:
            triplet = nums[low] + nums[i] + nums[high]
            if triplet == target:
                return True
            if triplet < target:
                low += 1
            else:
                high -= 1
    return False
