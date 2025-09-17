class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 0:
            return -1

        elif x == 0 or x == 1:
            return x        
        
        else:
            # Using the Newton-Raphson method to approximate the square root
            guess = x/2

            SD = 0.000000000000001
            
            while True:
                new_guess = (guess + x/guess) /2
                if abs(new_guess - guess) < SD:
                    return int(new_guess)
                guess = new_guess

            # low = 1
            # high = x//2

            # while low <= high:
            #     mid = (low + high) // 2
            #     check = mid*mid
                
            #     if check == x:
            #         return mid
            #     elif check < x:
            #         low = mid + 1
            #     else:
            #         high = mid - 1
            # return high


def main():
    sol = Solution()
    print(sol.mySqrt(4))  # Output: 2
    print(sol.mySqrt(8))  # Output: 2
    print(sol.mySqrt(0))  # Output: 0
    print(sol.mySqrt(1))  # Output: 1
    print(sol.mySqrt(16)) # Output: 4
    print(sol.mySqrt(25)) # Output: 5
    print(sol.mySqrt(26)) # Output: 5
    print(sol.mySqrt(2147395599)) # Output: 46339

if __name__ == "__main__":
    main()