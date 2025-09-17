from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1  # we want to add one
        i = len(digits) - 1
        
        while i >= 0 and carry:
            new_val = digits[i] + carry
            digits[i] = new_val % 10
            carry = new_val // 10
            i -= 1
        
        if carry:  # if we still have a carry left, insert at front
            digits.insert(0, carry)
        
        return digits

def main():
    solution = Solution()
    print(solution.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
    print(solution.plusOne([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
    print(solution.plusOne([9]))  # Output: [1, 0]
    print(solution.plusOne([9, 9, 9]))  # Output: [1, 0, 0, 0]

if __name__ == "__main__":
    main()