'''
@Author: NoserQJH
@LastEditors: NoserQJH
@Date: 2019-01-25 17:47:30
@LastEditTime: 2019-01-25 18:33:48
@Description:
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers1(self, l1, l2):
        def list2num(l):
            num = 0
            rate = 1
            while (l is not None):
                num += l.val * rate
                rate = rate * 10
                l = l.next
            return num

        def num2list(num):
            root = ListNode(num % 10)
            num = (num - num % 10) / 10
            last = root
            while num != 0:
                last.next = ListNode(num % 10)
                num = (num - num % 10) / 10
                last = last.next
            return root

        return num2list(list2num(l1) + list2num(l2))

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = l1.val if l1 else 0
        num2 = l2.val if l2 else 0
        num = num1 + num2
        remain = num / 10
        # 这里不要用int(math.floor()),python的int直接忽略小数
        num = num % 10
        root = ListNode(num)
        last = root
        l1 = l1.next
        l2 = l2.next
        while (l1 is not None) or (l2 is not None):
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            num = num1 + num2 + remain
            remain = num / 10
            num = num % 10
            last.next = ListNode(num)
            last = last.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if remain == 1:
            last.next = ListNode(1)
        return root

    def addTwoNumbers_eazy(self, l1, l2):
        # 看到别人的写法，复杂度一样，但代码用递归写简洁好多
        def toint(node):
            return node.val + 10 * toint(node.next) if node else 0

        def tolist(n):
            node = ListNode(n % 10)
            if n > 9:
                node.next = tolist(n / 10)
            return node

        return tolist(toint(l1) + toint(l2))


def main():
    solution = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(8)
    l2 = ListNode(5)
    result = solution.addTwoNumbers(l1, l2)
    print result


if __name__ == '__main__':
    main()
