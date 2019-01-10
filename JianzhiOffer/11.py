# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n < 0:
            n = 2**32 + n
        n = abs(n)
        one_num = 0
        all_num = 0
        while (n > 0):
            if n % 2 == 1:
                one_num += 1
                n -= 1
            all_num += 1
            n /= 2
        return one_num


def main():
    solution = Solution()
    result = solution.NumberOf1(-1)
    print result


if __name__ == '__main__':
    main()
