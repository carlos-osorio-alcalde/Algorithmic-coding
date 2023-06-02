class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        seen_values = set()
        
        def recursion(head):
            if head is None:
                return None

            if head.val in seen_values:
                return recursion(head.next)
            else:
                seen_values.add(head.val)
                head.next = recursion(head.next)
            return head
        
        return recursion(head)
    
def convert_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    
    return result

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)
    head.next.next.next.next.next = ListNode(3)

    s = Solution()
    print(convert_to_list(head))
    print(convert_to_list(s.deleteDuplicates(head)))
