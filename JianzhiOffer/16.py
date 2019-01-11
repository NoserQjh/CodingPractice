# -*- coding:utf-8 -*-
'''
    有坑，输入可能为None
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):

        if (pHead1 is None) and (pHead2 is None):
            return None
        elif pHead1 is None:
            pHead = pHead2
            pHead2 = pHead2.next
        elif pHead2 is None:
            pHead = pHead1
            pHead1 = pHead1.next
        else:
            if pHead1.val < pHead2.val:
                pHead = pHead1
                pHead1 = pHead1.next
            else:
                pHead = pHead2
                pHead2 = pHead2.next

        last = pHead
        while (pHead1 is not None) or (pHead2 is not None):
            if pHead1 is None:
                last.next = pHead2
                pHead2 = pHead2.next
                last = last.next
            elif pHead2 is None:
                last.next = pHead1
                pHead1 = pHead1.next
                last = last.next
            else:
                if pHead1.val < pHead2.val:
                    last.next = pHead1
                    pHead1 = pHead1.next
                    last = last.next
                else:
                    last.next = pHead2
                    pHead2 = pHead2.next
                    last = last.next
        return pHead


def main():
    solution = Solution()
    a = ListNode(0)
    a.next = ListNode(2)
    b = ListNode(1)
    b.next = ListNode(3)
    result = solution.Merge(a, None)
    print result


if __name__ == '__main__':
    main()
