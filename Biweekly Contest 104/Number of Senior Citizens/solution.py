class Solution:
    def countSeniors(self, details: List[str]) -> int:  # noqa: F821
        counter = 0
        for passenger in details:
            if(int(passenger[11:13]) > 60):
                counter += 1
        return counter