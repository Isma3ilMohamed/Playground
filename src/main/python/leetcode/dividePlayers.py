from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        total_skill_per_team = skill[0] + skill[-1]
        chemistry_sum = 0
        
        for i in range(n // 2):
            team_skill = skill[i] + skill[n - i - 1]
            if team_skill != total_skill_per_team:
                return -1
            chemistry = skill[i] * skill[n - i - 1]
            chemistry_sum += chemistry
        
        return chemistry_sum
