# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        odd_array = []
        even_array = []
        for x in array:
            if x % 2 == 1:
                odd_array.append(x)
            else:
                even_array.append(x)
        return odd_array + even_array


def main():
    solution = Solution()
    result = solution.reOrderArray([4, 1, 2])
    print result


if __name__ == '__main__':
    main()
