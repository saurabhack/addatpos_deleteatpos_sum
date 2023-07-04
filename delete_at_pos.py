class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None

    def push( self,data):
        New_node = node(data)
        if self.head == None:
            self.head = New_node
            return
        New_node.next = self.head
        self.head = New_node
        return self.head
    def delete_pos(self,n):
        if self.head==None:
            return None
        i=1
        current=self.head
        while(i<n):
            current=current.next
            i=i+1
        current.next=current.next.next
    def printList(self):
        current = self.head
        while (current != None):
            print(current.data, end="->")
            current = current.next
        print("null")
if __name__=="__main__":
    ll=linkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.printList()
    ll.addat(2,6)
    ll.printList()
    ll.delete_pos(4)
    ll.printList()
    ll.sum()
