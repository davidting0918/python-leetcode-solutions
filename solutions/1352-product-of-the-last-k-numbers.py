# https://leetcode.com/problems/product-of-the-last-k-numbers/description/?envType=daily-question&envId=2025-02-14

class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.last_zero_index = -1
        self.dp = [] 

    def add(self, num: int) -> None:
        self.nums.append(num)
        
        if num == 0:
            self.last_zero_index = len(self.nums) - 1
            self.dp = [0] * len(self.nums)
        
        else:
            self.dp.append(num)
            if num == 1:
                return
            for i in range(-2, (self.last_zero_index - len(self.nums)), -1):
                self.dp[i] = self.dp[i] * num
        
        return

    def getProduct(self, k: int) -> int:
        return self.dp[-k]


if __name__ == "__main__":
    s = ProductOfNumbers()

    actions = ["add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
    nuums = [[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

    for i in range(len(actions)):
        if actions[i] == "add":
            s.add(nuums[i][0])
        else:
            print(s.getProduct(nuums[i][0]))


