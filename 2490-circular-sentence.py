# https://leetcode.com/problems/circular-sentence/description/?envType=daily-question&envId=2024-11-02
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        string_list = sentence.split(' ')

        for i in range(len(string_list)):
            prev = string_list[i - 1]
            current = string_list[i]
            if prev[-1] != current[0]:
                return False
        return True
