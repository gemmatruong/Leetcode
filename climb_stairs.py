class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a = 1
        b = 2
        for _ in range(3, n+1):
            a, b = b, a + b
        return b

def main():
    sol = Solution()

    while True:
        try:
            number = int(input("Enter the number of stairs: "))
            if number < 0:
                print("Invalid input - Number cannot be negative!")
                continue
            ways = sol.climbStairs(number)
            print(f"To climb {number} stairs, we will have {ways} way(s)")

            cont = True
            while cont:
                choice = input("Continue (Y-yes/ N-no)? ").upper()
                if choice == "YES" or choice == "Y":
                    break
                elif choice == "NO" or choice == "N":
                    cont = False
                else:
                    print("Invalid input - Must be Y-Yes or N-No")
            if not cont:
                break
        except ValueError:
            print("Invalid input - must be a number")


if __name__ == "__main__":
    main()