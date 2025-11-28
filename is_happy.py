class Solution:
    def isHappy(self, n: int) -> bool:
        # WAY 1: convert num to str and convert back to integer to get individual digit
        # seen = set()
        # while n != 1 and (n not in seen):
        #     seen.add(n)
        #     n = sum(int(digit)**2 for digit in str(n))
        # return n == 1

        # WAY 2: manipulate the number directly, no conversion
        seen = set()

        while n not in seen:
            seen.add(n)
            current_sum = 0
            while n > 0:
                digit = n%10
                current_sum += digit**2
                n = n//10
            n = current_sum

        if current_sum == 1:
            return True
        return False
    
def main():
    sol = Solution()
    
    test_cases = [
        (1, True),
        (2, False),
        (7, True),
        (19, True),
        (20, False),
        (100, True),
        (1111111, True),
        (222, False),
        (13, True),
        (9999, False),
    ]

    for i, (n, expected) in enumerate(test_cases, 1):
        result = sol.isHappy(n)
        print(f"Test {i}: isHappy({n}) = {result} | Expected = {expected} | {'PASS' if result == expected else 'FAIL'}")

if __name__ == "__main__":
    main()