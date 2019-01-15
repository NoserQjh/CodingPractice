# -*- coding:utf-8 -*-
'''
    这题不错，有点意思
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_son(self, pRoot1, pRoot2):
        if pRoot2 is None:
            return True
        if pRoot1 is None:
            return False
        if pRoot1.val == pRoot2.val:
            return (self.is_son(pRoot1.left, pRoot2.left)) and (self.is_son(
                pRoot1.right, pRoot2.right))
        else:
            return False

    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot2 == None:
            return False
        if pRoot1 == None:
            return False
        else:
            if pRoot1.val == pRoot2.val:
                if self.is_son(pRoot1, pRoot2):
                    return True
            return (self.HasSubtree(pRoot1.left, pRoot2)
                    or self.HasSubtree(pRoot1.right, pRoot2))


def main():
    a = TreeNode(0)
    a.left = TreeNode(1)
    a.right = TreeNode(2)
    b = TreeNode(0)
    solution = Solution()
    result = solution.HasSubtree(a, b)
    print result


if __name__ == '__main__':
    main()
