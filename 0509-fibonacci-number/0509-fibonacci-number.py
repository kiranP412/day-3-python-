class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)

# Call the function
param_1 = 4
ret = Solution().fib(param_1)
print(ret)  # Output: 3


