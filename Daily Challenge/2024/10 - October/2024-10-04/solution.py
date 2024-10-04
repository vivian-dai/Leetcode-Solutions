class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chem = 0
        target = skill[0] + skill[-1]
        for i in range(len(skill)//2):
            if skill[i] + skill[len(skill) - i - 1] != target:
                return -1
            chem += skill[i] * skill[len(skill) - i -1]

        return chem
