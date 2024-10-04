class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        uncoms = []
        s1 = s1.split(" ")
        s2 = s2.split(" ")

        all_words = s1 + s2 
        all_words.sort()
        last_word = all_words[0]
        for i in range(1, len(all_words) - 1):
            if all_words[i] != last_word:
                last_word = all_words[i]
                if all_words[i + 1] != last_word:
                    uncoms.append(last_word)
        if last_word != all_words[-1]:
            uncoms.append(all_words[-1])
        if all_words[0] != all_words[1]:
            uncoms.append(all_words[0])
        return uncoms
