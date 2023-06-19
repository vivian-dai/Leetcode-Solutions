class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        bruh = 0
        while mainTank >= 5:
            mainTank -= 5
            bruh += 5
            if additionalTank > 0:
                mainTank += 1
                additionalTank -= 1
        bruh += mainTank
        return bruh*10
        