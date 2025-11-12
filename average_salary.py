from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)

        salary.remove(min_salary)
        salary.remove(max_salary)

        average = sum(salary) / len(salary)

        return average

def main():
    sol = Solution()
    
    test_cases = [
        [4000, 3000, 1000, 2000],           # Normal case
        [1000, 2000, 3000],                 # Small list
        [6000, 5000, 4000, 3000, 2000, 1000], # Larger list
        [8000, 9000, 2000, 3000, 1000],     # Extreme high/low salaries
        [5000, 5000, 4000, 3000, 2000],     # Duplicate mid-values
        [10000, 20000, 30000, 40000, 50000],# Increasing sequence
        [50000, 40000, 30000, 20000, 10000],# Decreasing sequence
        [2000, 2000, 2000, 1000, 3000],     # Many duplicates with extremes
        [2500, 2500, 2500, 2500, 2500],     # All equal (after removing min/max, same values left)
        [6000, 1000, 2000, 3000, 4000, 5000, 7000] # 7 elements, varied spread
    ]

    for i, salaries in enumerate(test_cases, 1):
        # Copy to avoid modifying original list
        result = sol.average(salaries.copy())
        print(f"Test {i}: Input = {salaries} → Average (excluding min/max) = {result:.2f}")


if __name__ == "__main__":
    main()