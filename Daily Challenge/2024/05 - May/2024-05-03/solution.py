class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        v1_i = []
        v2_i = []
        for v in v1:
            v1_i.append(int(v))
        for v in v2:
            v2_i.append(int(v))
        for i in range(min(len(v2_i), len(v1_i))):
            if v1_i[i] > v2_i[i]:
                return 1
            elif v1_i[i] < v2_i[i]:
                return -1
        if len(v2_i) > len(v1_i):
            # make sure v2_i isn't just all 0
            for i in range(len(v1_i), len(v2_i)):
                if v2_i[i] != 0:
                    return -1
        elif len(v1_i) > len(v2_i):
            for i in range(len(v2_i), len(v1_i)):
                if v1_i[i] != 0:
                    return 1
        return 0
