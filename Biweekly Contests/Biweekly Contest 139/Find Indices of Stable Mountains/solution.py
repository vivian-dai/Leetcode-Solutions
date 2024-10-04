class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        stable = []
        for i in range(len(height) - 1):
            if height[i] > threshold:
                stable.append(i + 1)
        return stable
