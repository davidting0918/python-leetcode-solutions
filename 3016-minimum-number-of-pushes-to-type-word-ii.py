# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/description/
class Solution:
    def minimumPushes(self, word: str) -> int:
        word_set = set(word)
        word_map = {}

        for i in word_set:
            word_map[i] = word.count(i)

        push = 1
        left = 8
        result = 0
        for _, count in sorted(word_map.items(), key=lambda x: x[1], reverse=True):
            result += count * push
            left -= 1

            if left == 0:
                push += 1
                left = 8
        return result
    


if __name__ == "__main__":
    s = Solution()

    word = "aabbccddeeffgghhiiiiii"
    print(s.minimumPushes(word))