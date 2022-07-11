# Linked list stored value in different memory location but connected by links.
# linkedlist: [12]->[13]->[14]->[15]->End
# location  : 2400  1900  2698  1664
# linked list types -> doubly linked list, singly linked list, circular linked list

from itertools import count


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr + ' END')

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, datalist):
        self.head = None
        for data in datalist:
            self.insert_at_end(data)

    def len_of_list(self):
        count = 0
        itr = self.head
        llstr = ''
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index < 0 or index >= self.len_of_list():
            raise Exception('Invalid index')

        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.len_of_list():
            raise Exception('Invalid index')
        if index == 0:
            self.insert_at_begining(data)
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        if self.head is None:
            return
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
            itr = itr.next

    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.print()
    ll.remove_by_value("orange")  # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()

# ---- 2. Implement doubly linked list. The only difference with regular linked list is that double linked has prev node reference as well. That way you can iterate in forward and backward direction.

print()
print()
print('Doubly Linked list:')


class DNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Dub_LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = DNode(data, self.head, None)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = DNode(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = DNode(data, None, itr.next)

    def insert_values(self, datalist):
        self.head = None
        for data in datalist:
            self.insert_at_end(data)

    def len_of_list(self):
        count = 0
        itr = self.head
        llstr = ''
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index < 0 or index >= self.len_of_list():
            raise Exception('Invalid index')

        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.len_of_list():
            raise Exception('Invalid index')
        if index == 0:
            self.insert_at_begining(data)
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = DNode(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        if self.head is None:
            return
        if self.head.data == data_after:
            self.head.next = DNode(data_to_insert, self.head.next)
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = DNode(data_to_insert, itr.next)
                itr.next = node
            itr = itr.next

    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def print_forward(self):
        # This method prints list in forward direction. Use node.next
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr + ' END')

    def print_backward(self):
        # Print linked list in reverse direction. Use node.prev for this.
        pass
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr + ' END')


if __name__ == '__main__':
    dl = Dub_LinkedList()
    dl.insert_values(["banana", "mango", "grapes", "orange"])
    dl.print()
    # dl.print_forward()
    # print('backward List: ')
    # dl.print_backward()
    # dl.insert_after_value("mango", "apple")  # insert apple after mango
    # dl.print_forward()
    # dl.remove_by_value("orange")  # remove orange from linked list
    # dl.print_forward()
    # dl.remove_by_value("figs")
    # dl.print_forward()
    # dl.remove_by_value("banana")
    # dl.remove_by_value("mango")
    # dl.remove_by_value("apple")
    # dl.remove_by_value("grapes")
    # dl.print_forward()