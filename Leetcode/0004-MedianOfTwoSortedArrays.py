'''
@Author: NoserQJH
@LastEditors: NoserQJH
@Date: 2019-01-26 18:18:50
@LastEditTime: 2019-03-04 21:46:24
@Description:Runtime: 52 ms, faster than 99.36% of Python online submissions for Median of Two Sorted Arrays.
Memory Usage: 10.9 MB, less than 30.29% of Python online submissions for Median of Two Sorted Arrays.
'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = 0
        num = (len(nums1) + len(nums2)) / 2
        if len(nums1) < len(nums2):
            temp = nums2
            nums2 = nums1
            nums1 = temp
        if len(nums2) == 0:
            if (len(nums1) + len(nums2)) % 2 == 1:
                return nums1[num]
            else:
                return (nums1[num - 1] + nums1[num]) / 2.0
        if len(nums1) == 1:
            return (nums1[0] + nums2[0]) / 2.0
        if nums1[num - 1] <= nums2[0]:
            if (len(nums1) + len(nums2)) % 2 == 1:
                return min(nums1[num], nums2[0])
            else:
                if len(nums1) == len(nums2):
                    return (nums1[num - 1] + nums2[0]) / 2.0
                else:
                    return (nums1[num - 1] + min(nums1[num], nums2[0])) / 2.0
        if nums1[0] >= nums2[-1]:
            if (len(nums1) + len(nums2)) % 2 == 1:
                return nums1[num - len(nums2)]
            else:
                if len(nums1) == len(nums2):
                    return (nums1[0] + nums2[-1]) / 2.0
                else:
                    return (nums1[num - len(nums2)] +
                            nums1[num - len(nums2) - 1]) / 2.0
        nums2.append(max(nums1[-1],nums2[-1])+10)

        left = 0
        right = len(nums1)
        while (True):
            n = num - m - 2
            if n >= len(nums2) - 1:
                left = m
                m = (m + right) / 2
                continue
            if n < 0:
                right = m
                m = (m + left) / 2
                continue
            if (nums1[m] <= nums2[n + 1]) & (nums2[n] <= nums1[m + 1]):
                break
            elif nums1[m] > nums2[n + 1]:
                right = m
                m = (m + left) / 2
            else:
                left = m
                m = (m + right) / 2
        resultlist = [nums1[m], nums1[m + 1], nums2[n], nums2[n + 1]]
        resultlist.sort()
        if (len(nums1) + len(nums2)) % 2 == 0:
            return resultlist[2]
        else:
            return (resultlist[1] + resultlist[2]) / 2.0


def main():
    nums1 = []
    nums2 = [1]
    solution = Solution()
    result = solution.findMedianSortedArrays(nums1, nums2)
    print result


if __name__ == '__main__':
    main()
