# -*- coding:utf-8 -*-


class Solution:
    # array 二维列表
    def Find(self, target, array):
        x = len(array) - 1
        y = 0
        ylim = len(array[0])
        while ((y < ylim) & (x >= 0)):
            if array[x][y] == target:
                return True
            elif array[x][y] < target:
                y += 1
            else:
                x -= 1
        return False


def main():
    solution = Solution()
    result = solution.Find(1, [[1, 2, 3], [4, 5, 6]])
    print result


if __name__ == '__main__':
    main()