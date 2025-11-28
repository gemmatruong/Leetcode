class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        ugly_numbers = [0]*n
        ugly_numbers[0] = 1
        p2, p3, p5 = 0, 0, 0

        for i in range(1, n):
            # Find the next ugly number and add it to the list
            next_p2 = ugly_numbers[p2]*2
            next_p3 = ugly_numbers[p3]*3
            next_p5 = ugly_numbers[p5]*5
            next_ugly = min(next_p2, next_p3, next_p5)
            ugly_numbers[i] = next_ugly

            # Update index of the pointer that's just been taken
            if next_ugly == next_p2:
                p2 += 1
            if next_ugly == next_p3:
                p3 += 1
            if next_ugly == next_p5:
                p5 += 1
        return ugly_numbers[n-1]

def main():
    sol = Solution()

    test_cases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 8),
        (10, 12),
        (15, 24),
        (20, 36),
    ]

    for i, (n, expected) in enumerate(test_cases, 1):
        result = sol.nthUglyNumber(n)
        print(f"Test {i}: nthUglyNumber({n}) = {result} | Expected = {expected} | "
              f"{'PASS' if result == expected else 'FAIL'}")

if __name__ == "__main__":
    main()
