# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # hash_set = set()
        # prev, curr = None, head
        
        # iterate over the nodes and check whether the last node is pointing null or any previous node
        # while curr:
        #     if curr in hash_set:
        #         return True
        #     else:
        #         hash_set.add(curr)
        #         curr = curr.next
        # return False


        ## keep two pointer one is fast and one is slow, if the cycle is present then definitely the fast pointer will get flag that and if not fast pointer will reach to end faster and return false
        slow, fast = head, head

        while fast and fast.next:
            slow= slow.next
            fast = fast.next.next

            if slow ==fast:
                return True
        return False
        