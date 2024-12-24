# Solution class with twoSum method
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# Create an instance of the Solution class
solution = Solution()

# Test cases
test_cases = [
    {"nums": [2, 7, 11, 15], "target": 9, "expected": [0, 1]},
    {"nums": [3, 2, 4], "target": 6, "expected": [1, 2]},
    {"nums": [3, 3], "target": 6, "expected": [0, 1]},
    {"nums": [1, 5, 7, 2], "target": 10, "expected": [2, 3]},
]

# Run the test cases
for i, test in enumerate(test_cases):
    nums = test["nums"]
    target = test["target"]
    expected = test["expected"]
    
    result = solution.twoSum(nums, target)
    print(f"Test Case {i + 1}: {'Passed' if result == expected else 'Failed'}")
    print(f"  Input: nums={nums}, target={target}")
    print(f"  Expected: {expected}, Got: {result}\n")
