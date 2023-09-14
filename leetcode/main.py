from LinkedList import LinkedList


def main():
    # mergeTwoLists
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(2)
    ll1.append(4)

    ll2 = LinkedList()
    ll2.append(1)
    ll2.append(3)
    ll2.append(4)

    merged_head = ll1.mergeTwoLists(list1=ll1.head, list2=ll2.head)

    while merged_head is not None:
        print(merged_head.data)
        merged_head = merged_head.next


if __name__ == "__main__":
    main()
