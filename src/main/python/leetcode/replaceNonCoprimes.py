class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        st = []
        for num in nums:
            while st and math.gcd(st[-1], num) > 1:
                prev = st.pop()
                num = math.lcm(prev, num)
            st.append(num)
        
        return st
