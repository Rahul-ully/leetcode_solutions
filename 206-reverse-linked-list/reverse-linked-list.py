class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        current = head

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev