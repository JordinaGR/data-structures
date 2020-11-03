class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None

    def add_value_beggining(self, data):
        node = Node(data, self.head)
        self.head = node

    def add_value_final(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        i = self.head
        while i.next:
            i = i.next

        i.next = Node(data, None)

    def add_multiple_values_end(self, data):
        if self.head is None:
            self.head = Node(data[0], None)
            del data[0]

        i = self.head
        while i.next:
            i = i.next

        for j in range(len(data)):
            i.next = Node(data[j], None)
            i = i.next
        return

    def add_multiple_values_beggining_order(self, data):
        if self.head is None:
            ll.add_multiple_values_end(data)
            return

        i = len(data)-1

        while i >= 0:
            node = Node(data[i], self.head)
            self.head = node
            i -= 1

    def remove_at_inx(self, index):
        if index < 0 or index >= self.len_linked_list():
            print('index out of range')
            return
        
        if index == 0:
            self.head = self.head.next
            return
        
        k = 0
        i = self.head
        while i:
            if k == index-1:
                i.next = i.next.next
                break
            i = i.next
            k += 1
        
    def len_linked_list(self):
        lenth = 1

        i = self.head
        while i.next:
            lenth += 1
            i = i.next
        return lenth

    def display(self):
        if self.head is None:
            print('empty list')
            return
        
        i = self.head
        string = ' '
        while i:
            string += str(i.data) + ' --> '
            i = i.next

        print(string)


ll  = LinkedList()
ll.add_value_beggining(100)
ll.add_multiple_values_beggining_order([1,20,3])
ll.display()
