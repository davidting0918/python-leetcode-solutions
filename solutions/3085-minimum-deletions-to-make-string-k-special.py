# https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/description/?envType=daily-question&envId=2025-06-21

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        letters = set(word)
        letter_counts = {}
        for l in letters:
            count = word.count(l)
            letter_counts[count] = letter_counts.get(count, 0) + 1

        print(letter_counts)

        # let each freq be the standard
        answer = float('inf')
        for target in letter_counts:
            temp_answer = 0
            target_max = target + k
            for freq in letter_counts:
                if freq == target:
                    continue
                if freq > target_max:
                    temp_answer += (freq - target_max) * letter_counts[freq]
                elif freq < target:
                    temp_answer += freq * letter_counts[freq]
            print(f"target: {target}, temp_answer: {temp_answer}")
            answer = min(answer, temp_answer)
        return answer
    

if __name__ == "__main__":
    s = Solution()
    word = "aaabaaa"
    k = 2
    print(s.minimumDeletions(word, k))
