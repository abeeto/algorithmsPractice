class node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

head = None
tail = None
size = 1

def enqueue(n):
    global tail,head, size
    if(head == None):
        head = node(n, None)
        tail = head
    else:
        tail.next = node(n, None)
        tail = tail.next
        if(head.next == None):
            head.next(tail)
    size += 1
    return "Added" + str(n)

def dequeue():
    global head, size
    if(head != None):
        toReturn = head.value
        head = head.next
        size -= 1
        return "removed " + str(toReturn)
    return "nothing to remove"
def front():
    global head
    if(head != None):
        toReturn = head.value
        return "next in queue: "+ str(toReturn)
    return "Nothing in front"

def getSize():
    return size

def isEmpty():
    global head
    if (head == None):
        return "Empty"
    return False

