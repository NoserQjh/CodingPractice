# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        last = None
        while pHead is not None:
            nextNode = pHead.next
            pHead.next = last
            last = pHead
            pHead = nextNode
        return last


def main():
    solution = Solution()
    a = ListNode(0)
    a.next = ListNode(1)
    result = solution.ReverseList(a)
    print result


if __name__ == '__main__':
    main()
