class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()  # Sort the array of people
        start, end = 0, len(people) - 1
        boats = 0

        while start <= end:
            if people[start] + people[end] <= limit:
                start += 1  # The lightest person is paired up
            end -= 1  # The heaviest person is always accounted for in this round
            boats += 1  # In each iteration, we use up one boat

        return boats


s = Solution()
print(s.numRescueBoats(people=[3, 5, 3, 4], limit=5))
