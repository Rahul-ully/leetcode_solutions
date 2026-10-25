
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        x = ListNode(0)
        x.next = head
        prev = x

        while prev.next and prev.next.next:
            slow = prev.next
            fast = slow.next

            slow.next = fast.next
            fast.next = slow
            prev.next = fast

            prev = slow

        return x.next
