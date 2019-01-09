# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        fib = [0, 1]
        i = 2
        while (i <= n):
            fib.append(fib[i - 1] + fib[i - 2])
            i += 1
        return fib[n]


def main():
    solution = Solution()
    result = solution.Fibonacci(5)
    print result


if __name__ == '__main__':
    main()
