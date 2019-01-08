# -*- coding:utf-8 -*-
'''
    这题有坑，输入可能直接是None
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode is not None:
            result = self.printListFromTailToHead(listNode.next)
            result.append(listNode.val)
            return result
        else:
            return []


def main():
    solution = Solution()
    a = ListNode(0)
    a.next = ListNode(1)
    a.next.next = ListNode(2)
    result = solution.printListFromTailToHead(a)
    print result


if __name__ == '__main__':
    main()
