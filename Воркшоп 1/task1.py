class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def search_common_part(headA, headB):
    if not headA or not headB:
        return None
    
    flagA, flagB = headA, headB

    while flagA != flagB:
        flagA = flagA.next if flagA else headB
        flagB = flagB.next if flagB else headA

    return flagA

# Пример
def create_Lists():
    common = ListNode(8)
    common.next = ListNode(4)
    common.next.next = ListNode(5)
    
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = common
    
    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = common
    
    return headA, headB

# Тест
headA, headB = create_Lists()
first_common = search_common_part(headA, headB)
if first_common:
    print(f"Узел пересечения со значением: {first_common.val}")
else:
    print("Пересечения нет")