class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Helper function to find the k-th bit in S_n
        def find_kth(n, k):
            # Base case: If n = 1, S_1 is "0"
            if n == 1:
                return '0'
            
            # Length of the S_n string
            length = (1 << n) - 1  # 2^n - 1, length of S_n
            
            # Middle point of the string S_n
            mid = length // 2 + 1
            
            # If k is the middle bit, it is '1'
            if k == mid:
                return '1'
            
            # If k is in the first half, recurse on S_{n-1}
            if k < mid:
                return find_kth(n - 1, k)
            
            # If k is in the second half, recurse on S_{n-1}, reverse, and invert
            # The corresponding position in S_{n-1} is (length - k + 1)
            return '1' if find_kth(n - 1, length - k + 1) == '0' else '0'

        # Call the helper function for the given n and k
        return find_kth(n, k)
