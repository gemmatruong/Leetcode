from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1,n+1):
            if (i % 3 == 0) and (i % 5 == 0):
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
    
def main():
    sol = Solution()

    test_cases = [
        1,    # ["1"]
        3,    # ["1","2","Fizz"]
        5,    # ["1","2","Fizz","4","Buzz"]
        6,    # ["1","2","Fizz","4","Buzz","Fizz"]
        10,   # ends with "Buzz"
        15,   # contains "FizzBuzz"
        20,   # checks longer sequence
        0,    # edge case: empty result
        2,    # short sequence no fizz/buzz
        30,   # large enough to include multiple FizzBuzz
    ]

    for i, n in enumerate(test_cases, 1):
        result = sol.fizzBuzz(n)
        print(f"Test Case {i}: fizzBuzz({n}) -> {result}")


if __name__ == "__main__":
    main()