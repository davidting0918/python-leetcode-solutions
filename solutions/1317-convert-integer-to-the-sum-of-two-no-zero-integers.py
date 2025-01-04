class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        a = 0
        while "0" in f"{n - a}{a}":
            a += 1
        return [a, n - a]

    def getNoZeroIntegers_v2(self, n: int) -> list[int]:
        a, b, step = 0, 0, 1

        while n > 0:

            left = n % 10
            n //= 10
            print(f"Left: {left}, n: {n}")

            special_cases = [0, 1]

            if left in special_cases and n > 0:
                n -= 1
                a += (left + 1) * step
                b += (9) * step
            else:
                a += (left - 1) * step
                b += (1) * step

            print(f"a: {a}, b: {b}, n: {n}, step: {step}")
            step *= 10

        return [a, b]


if __name__ == "__main__":
    sol = Solution()
    num = 19
    print(sol.getNoZeroIntegers_v2(num))