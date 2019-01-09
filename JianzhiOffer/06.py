# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        last = rotateArray[0]
        for x in rotateArray:
            if x < last:
                return x
            else:
                last = x
        return 0


def main():
    solution = Solution()
    result = solution.minNumberInRotateArray([3, 4, 5, 1, 2])
    print result


if __name__ == '__main__':
    main()
