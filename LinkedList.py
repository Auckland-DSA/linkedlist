"""
Node definition
"""
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, node = None):
        self.head = node
        self.length = 1 if node else 0
        self.tail = node

    def createNode(self, value):
        return Node(value)

    """
    Insert an element at the end of the list
    """
    def append(self, node):
        pass

    """
        Get the index of a node based on the value
    """
    def getPositionOfValue(self, value):
        pass

    """
        Get the value of a node based on an index
    """
    def getValueOfPosition(self, position):
        element = self.head
        tempPosition = 0
        while element:
            tempPosition += 1
            if tempPosition == position:
                return "The position " + str(position) + " has the value " + str(element.value) + " on the list"
            element = element.next
        return "The position doesn't exist in the list"



    def insert(self, value, position):
        node = self.createNode(value)
        if position > self.length + 1:
            print "The list is has a length of " + str(self.length) + ", so the element was not inserted"
            return
        elif position == 1:
            node.next = self.head
            self.head = node
            self.length += 1
            return
        else:
            element = self.head
            currentPosition = 0
            while element and currentPosition < self.length:
                currentPosition += 1
                if currentPosition + 1 == position:
                    tempNode = element.next
                    element.next = node
                    node.next = tempNode

                    self.length += 1

                    print "Node Inserted"
                    return

                element = element.next


    """
        Delete a node based on its value
    """
    def deleteValue(self, value):
        node = self.head
        if node:
            if node.value == value:
                self.head = node.next

                self.length -= 1

                del node
                return
            else:
                while node:
                    next = node.next
                    if next and next.value == value:
                        node.next = next.next

                        self.length -= 1

                        del next
                        return
                    else:
                        node = next

        print "Value doesnt exist in list"

    """
        Delete a node based on its index
    """
    def deleteNode(self, n):
        pass

    def printNodes(self):
        element = self.head
        print "==================================="
        print "Head: Value {0} Address of this element: {1}  Address of Next element: {2}".format(element.value, hex(id(element)), hex(id(element.next)) if element.next else '0x0')
        element = element.next
        while element:
            print "Node: Value {0} Address of this element: {1}  Address of Next element: {2}".format(element.value, hex(id(element)), hex(id(element.next)) if element.next else '0x0')
            element = element.next
        print "==================================="

a = -1

ll = LinkedList()

while a != 0:
    print "Linked List"
    print "1. Append (empty)"
    print "2. Get Position Of Value (empty)"
    print "3. Get Value Of Position"
    print "4. Insert"
    print "5. Delete (Value)"
    print "6. Delete (Node) (empty)"
    print "7. Print LinkedList"
    print "0. Exit"
    a = input("Choose an option: ")

    if a == 1:
        ll.append(input("Introduce value to append: "))
    elif a == 2:
        print ll.getPositionOfValue(input("Introduce value to search it's position: "))
    elif a == 3:
        print ll.getValueOfPosition(input("Introduce position to search it's value: "))
    elif a == 4:
        ll.insert(input("Introduce value to insert: "), input("Introduce which position you want to insert the node: "))
    elif a == 5:
        ll.deleteValue(input("Introduce value of the node to be deleted: "))
    elif a == 6:
        ll.deleteNode(input("Introduce node to delete: "))
    elif a == 7:
        pass



    ll.printNodes()
    print "{0} nodes in total".format(ll.length)

