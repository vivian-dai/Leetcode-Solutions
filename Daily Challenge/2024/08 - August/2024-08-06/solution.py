class Solution:
    def minimumPushes(self, word: str) -> int:
        letter_counter = [0] * 26
        for c in word:
            letter_counter[ord(c) - ord('a')] += 1
        letter_counter.sort(reverse=True)
        singles = letter_counter[0] + letter_counter[1] + letter_counter[2] + letter_counter[3] + letter_counter[4] + letter_counter[5] + letter_counter[6] + letter_counter[7]
        doubles = letter_counter[8] + letter_counter[9] + letter_counter[10] + letter_counter[11] + letter_counter[12] + letter_counter[13] + letter_counter[14] + letter_counter[15]
        triples = letter_counter[16] + letter_counter[17] + letter_counter[18] + letter_counter[19] + letter_counter[20] + letter_counter[21] + letter_counter[22] + letter_counter[23]
        quadrouples = letter_counter[24] + letter_counter[25]
        return singles + (doubles * 2) + (triples * 3) + (quadrouples * 4)
