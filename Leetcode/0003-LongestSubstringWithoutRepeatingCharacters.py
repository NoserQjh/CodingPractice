'''
@Author: NoserQJH
@LastEditors: NoserQJH
@Date: 2019-01-25 18:35:11
@LastEditTime: 2019-01-26 18:18:31
@Description:Runtime: 88 ms, faster than 37.81% of Python online submissions
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        max_len = 0
        now_dict = {}
        for idx in range(len(s)):
            if now_dict.get(s[idx], -1) >= start:
                start = now_dict[s[idx]] + 1
            now_dict[s[idx]] = idx
            if idx - start + 1 > max_len:
                max_len = idx - start + 1
        return max_len


def main():
    solution = Solution()
    result = solution.lengthOfLongestSubstring("abcabcbb")
    print result


if __name__ == '__main__':
    main()
