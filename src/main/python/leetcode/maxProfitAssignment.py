class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))  # Combine and sort jobs by difficulty
        worker.sort()  # Sort workers by their abilities
        
        max_profit = 0
        total_profit = 0
        job_index = 0
        
        for ability in worker:
            # Move the job_index pointer to the most profitable job that the current worker can perform
            while job_index < len(jobs) and jobs[job_index][0] <= ability:
                max_profit = max(max_profit, jobs[job_index][1])
                job_index += 1
            # Add the max_profit for the current worker to the total_profit
            total_profit += max_profit
        
        return total_profit
