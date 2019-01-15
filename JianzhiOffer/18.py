# -*- coding:utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root is None:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root


def main():
    a = TreeNode(0)
    a.left = TreeNode(1)
    a.right = TreeNode(2)
    solution = Solution()
    result = solution.Mirror(a)
    print result


if __name__ == '__main__':
    main()
