class Solution:

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:  # noqa: F821

        slope = None

        if (coordinates[1][0] - coordinates[0][0]) != 0:

            slope = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0])

        for i in range(2, len(coordinates)):

            if (coordinates[i][0] - coordinates[i - 1][0]) == 0:

                if slope is not None:

                    return False

            elif (coordinates[i][1] - coordinates[i - 1][1])/(coordinates[i][0] - coordinates[i - 1][0]) != slope:

                return False

        return True
        