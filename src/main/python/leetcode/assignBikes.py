from scipy.optimize import linear_sum_assignment

class Solution:
    def assignBikes(self, workers: list[list[int]], bikes: list[list[int]]) -> int:
        n, m = len(workers), len(bikes)

        cost_matrix = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                cost_matrix[i][j] = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])

        row_ind, col_ind = linear_sum_assignment(cost_matrix)

        min_cost = sum(cost_matrix[i][j] for i, j in zip(row_ind, col_ind))

        return min_cost
