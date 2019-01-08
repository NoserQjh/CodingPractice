# -*- coding:utf-8 -*-
'''
    基础题，直接递归暴力解就可以了
    但浪费了好长时间想o(N)的解法，最后发现好像没有？
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def addSon(self, fatherNode, sonNode, forward):
        if forward == 'left':
            fatherNode.left = sonNode
        else:
            fatherNode.right = sonNode

    def reConstructBinaryTree(self, pre, tin):
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        for x in range(len(tin)):
            if tin[x] == pre[0]:
                break
        if x == len(tin) - 1:
            root.left = self.reConstructBinaryTree(pre[1:], tin[0:-1])
        elif x == 0:
            root.right = self.reConstructBinaryTree(pre[1:], tin[1:])
        else:
            root.left = self.reConstructBinaryTree(pre[1:x + 1], tin[0:x])
            root.right = self.reConstructBinaryTree(pre[x + 1:], tin[x + 1:])
        return root


def main():
    solution = Solution()
    result = solution.reConstructBinaryTree([1, 2, 3, 4, 5, 6, 7],
                                            [3, 2, 4, 1, 6, 5, 7])
    print result


if __name__ == '__main__':
    main()
