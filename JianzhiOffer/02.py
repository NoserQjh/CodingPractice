# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        result = ''
        for char in s:
            if char == ' ':
                result += '%20'
            else:
                result += char
        return result


def main():
    solution = Solution()
    result = solution.replaceSpace('We Are Happy')
    print result


if __name__ == '__main__':
    main()