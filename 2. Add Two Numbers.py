class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        resultHead = ListNode(0)
        resultPrev = resultHead
        addOne = 0
        while l1 or l2 or addOne:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            sum = l1Val + l2Val + addOne
            if sum >= 10:
                sum -= 10
                addOne = 1
            else:
                addOne = 0

            resultThis = ListNode(sum)
            resultPrev.next = resultThis
            resultPrev = resultPrev.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return resultHead.next
