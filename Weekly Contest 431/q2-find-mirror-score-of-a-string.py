# https://leetcode.com/contest/weekly-contest-431/problems/find-mirror-score-of-a-string/description/
class Solution:
    def calculateScore(self, s: str) -> int:
        # use heap to solve this question
        n = len(s)
        score = 0

        hash_table = {}
        for i in range(n):
            reverse_l = self.get_reverse_letter(s[i])
            if reverse_l not in hash_table:
                hash_table[s[i]] = hash_table.get(s[i], []) + [i]
                continue
            if not hash_table[reverse_l]:
                hash_table[s[i]] = hash_table.get(s[i], []) + [i]
                continue
            score += (i - hash_table[reverse_l].pop())
        return score

    def is_reverse(self, l1: str, l2: str):
        return ord(l1) + ord(l2) == 219

    def get_reverse_letter(self, l: str):
        return chr(219 - ord(l))

if __name__ == "__main__":
    s = Solution()
    string = "zadavyayobbgqsexaabk"
    print(''.join([s.get_reverse_letter(l) for l in string]))
    print(s.calculateScore(string)) # 14