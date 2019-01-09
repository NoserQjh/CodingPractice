# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        n = number + 1
        fib = [0, 1]
        i = 2
        while (i <= n):
            fib.append(0)
            for j in range(i):
                fib[i] += fib[j]
            i += 1
        return fib[n]

    def jumpFloorII_eazy(self, number):
        return 2**(number - 1)


def main():
    solution = Solution()
    result = solution.jumpFloorII(4)
    print result


if __name__ == '__main__':
    main()
