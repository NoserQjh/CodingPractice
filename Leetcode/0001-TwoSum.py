'''
@Author: NoserQJH
@LastEditors: NoserQJH
@Date: 2019-01-24 16:22:57
@LastEditTime: 2019-01-24 17:30:18
@Description:
'''

# -*- coding:utf-8 -*-


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp_dict = {}
        for idx in range(len(nums)):
            if nums[idx] in temp_dict:
                # 这里不能用temp_dict.keys()，因为dict的读取方式是哈希的，而keys()返回一个list，时间复杂度提高
                return idx, temp_dict[nums[idx]]
            else:
                temp_dict[target - nums[idx]] = idx


def main():
    solution = Solution()
    result = solution.twoSum([2, 7, 11, 15], 9)
    print result


if __name__ == '__main__':
    main()
