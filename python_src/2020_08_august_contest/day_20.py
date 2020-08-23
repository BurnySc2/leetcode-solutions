from typing import List


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next

    def __eq__(self, other: "ListNode") -> bool:
        if not isinstance(other, ListNode):
            return False

        if self.length(self) != self.length(other):
            return False

        first, second = self, other
        while first and second:
            if first.val != second.val:
                return False
            first, second = first.next, second.next
        return True

    def __repr__(self) -> str:
        seen = set()
        nodes = []
        current = self
        while 1:
            if id(current) in seen:
                return "REPEATED NODES " + " -> ".join(map(str, nodes))
            seen.add(id(current))
            nodes.append(current.val)
            if not current.next:
                return " -> ".join(map(str, nodes))
            current = current.next

    @classmethod
    def length(cls, node: "ListNode") -> int:
        l = 0
        start = node
        while start:
            start = start.next
            l += 1
        return l

    @classmethod
    def from_list(cls, my_list: List[int]) -> "ListNode":
        assert my_list
        start = cls(my_list[0])
        cur = start
        for i in my_list[1:]:
            cur.next = cls(i)
            cur = cur.next
        return start

    def to_list(self) -> List[int]:
        l = []
        cur = self
        while cur:
            l.append(cur.val)
            cur = cur.next
        return l


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next or not head.next.next:
            return

        # Find length
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        # Find middle listnode
        cur = head
        for i in range(length // 2):
            cur = cur.next
        prev, cur = cur, cur.next

        # Dettach to middle
        prev.next = None

        # Reverse second half
        while cur:
            cur.next, cur, prev = prev, cur.next, cur
        tail = prev

        # Mix lists
        next_head = head.next
        next_tail = tail.next

        # Cut off last link
        if length % 2 == 1:
            t = tail
        else:
            t = head
        for i in range(length // 2 - 1):
            t = t.next
        t.next = None

        # print(head)
        # print(tail)

        new_head = head
        while next_head and next_tail:
            new_head.next, tail.next = tail, new_head.next
            new_head, tail, next_head, next_tail = next_head, next_tail, next_head.next, next_tail.next
        # print(tail)
        if tail:
            new_head.next = tail
            tail.next = None
        # print(next_head)
        if next_head:
            tail.next = next_head
        # print(head)


# fmt: off
test_cases = [
    ListNode.from_list([1, 2, 3, 4]),
    ListNode.from_list([1, 2, 3, 4, 5]),
    ListNode.from_list([1]),
    # ListNode.from_list([]),
]
results = [
    [1, 4, 2, 3],
    [1, 5, 2, 4, 3],
    [1],
    # [],
]
# fmt: on

if __name__ == "__main__":
    app = Solution()
    for test_case, correct_result in zip(test_cases, results):
        test_case_copy = test_case.to_list()
        app.reorderList(test_case)
        my_result = test_case.to_list()
        assert (
            my_result == correct_result
        ), f"My result: {my_result}, correct result: {correct_result}\nTest Case: {test_case_copy}"
