class Solution:
    def isUgly(self, n: int) -> bool:
        # WAY 1: Slow and unnecessary checking
    #     if n <= 0:
    #         return False

    #     if n in [1,2,3,5]:
    #         return True

    #     end = int(n//) + 1
    #     for i in range(2, end):
    #         if (n % i == 0) and (i not in [2,3,5]) and self.isPrime(i):
    #             return False

    #     if self.isPrime(n):
    #         return False

    #     return True
    
    # def isPrime(self, n: int) -> bool:
    #     if n <= 1:
    #         return False
    #     if n <= 3:
    #         return True
    #     if n % 2 == 0:
    #         return False

    #     # Check odd divisors up to sqrt(n)
    #     end = int(n**0.5)+1
    #     for i in range(3,end):
    #         if n % i == 0:
    #             return False
    #     return True

        # WAY 2: Efficient. Just remove all allowed factors (2,3,5) from the number.
        # If the remained number is 1, it is an ugly number
        if n <= 0:
            return False
        if n == 1:
            return True

        for i in (2,3,5):
            while n % i == 0:
                n //= i
        return n == 1

def main():
    sol = Solution()

    test_cases = [
        (1, True),
        (2, True),
        (3, True),
        (5, True),
        (6, True),
        (8, True),
        (14, False),
        (25, True),
        (30, True),
        (121, False),
    ]

    for i, (n, expected) in enumerate(test_cases, 1):
        result = sol.isUgly(n)
        print(f"Test {i}: isUgly({n}) = {result} | Expected = {expected} | "
              f"{'PASS' if result == expected else 'FAIL'}")

if __name__ == "__main__":
    main()
