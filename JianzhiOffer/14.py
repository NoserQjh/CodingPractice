# -*- coding:utf-8 -*-
'''
    有坑，测试会有非法输入
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        shed = []
        while head is not None:
            shed.append(head)
            head = head.next
        if k > len(shed):
            return None
        if k == 0:
            return None
        while k - 1 > 0:
            shed.pop()
            k -= 1
        return shed.pop()


def main():
    solution = Solution()
    a = ListNode(0)
    a.next = ListNode(1)
    result = solution.FindKthToTail(a, 2)
    print result


if __name__ == '__main__':
    main()
