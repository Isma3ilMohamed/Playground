def find_length(nums: list[int], k: int) -> int:
    left = curr = ans = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        ans = max(ans, (right - left) + 1)
    return ans


def find_length(s: str) -> str:
    left = curr = ans = 0
    for right in range(len(s)):
        if s[right] == "0":
            curr += 1
        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1
        ans = max(ans, (right - left) + 1)

    return ans


print(find_length(s="1101100111"))
