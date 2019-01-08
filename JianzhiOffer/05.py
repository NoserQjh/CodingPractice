# -*- coding:utf-8 -*-
'''
    入队存在一个栈里，取得时候两个栈来回倒，中间把栈2的栈顶弹出就行
'''


class Solution:
    def __init__(self):
        self.shed1 = []
        self.shed2 = []

    def push(self, node):
        # write code here
        self.shed1.append(node)

    def pop(self):
        # return xx
        while (len(self.shed1) > 0):
            self.shed2.append(self.shed1.pop())
        result = self.shed2.pop()
        while (len(self.shed2) > 0):
            self.shed1.append(self.shed2.pop())
        return result
