class Solution:
    def merge_intervals(self, intervals: list[list[int]]) -> list[list[int]]:
        output = []

        last_edited_position = 0
        output.append(intervals[last_edited_position])

        for i in range(1, len(intervals)):
            temp = intervals[i]
            # [1,9],[3,8]
            if output[last_edited_position][0] <= temp[0] <= output[last_edited_position][1]:
                result_x = min(temp[0], output[last_edited_position][0])
                result_y = max(temp[1], output[last_edited_position][1])
                output[last_edited_position] = [result_x, result_y]
            else:
                last_edited_position += 1
                output.append(temp)

        return output


solution = Solution()
print(solution.merge_intervals([[1, 5], [4, 6], [6, 8], [11, 15]]))
