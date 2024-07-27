class Solution:
    def maximum69Number(self, num: int) -> int:
        num = [int(i) for i in str(num)]

        for i in range(len(num)):
            if num[i] == 6:
                num[i] = 9
                break

        return int("".join([str(i) for i in num]))

    def maximum69Number_v2(self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximum69Number_v2(9669))
    print(sol.maximum69Number(9996))
    print(sol.maximum69Number(9999))
    print(sol.maximum69Number(6666))
    print(sol.maximum69Number(6669))
    print(sol.maximum69Number(6699))
    print(sol.maximum69Number(6999))
    print(sol.maximum69Number(9999))
    print(sol.maximum69Number(6666))
