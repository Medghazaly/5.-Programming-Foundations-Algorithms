# Linked list example


# the Node class
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


# the LinkedList class
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, val):
        item = self.head
        while (item != None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()
        return None

    def deleteAt(self, idx):
        if idx > self.count:
            return
        if self.head == None:
            return
        else:
            tempIdx = 0
            node = self.head
            while tempIdx < idx-1:
                node = node.get_next()
                tempIdx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()


# create a linked list and insert some items
itemlist = LinkedList()
itemlist.insert("Mohamed")
itemlist.insert("Ghazaly")
itemlist.insert("Mahmod")
itemlist.insert("Mazin")
itemlist.insert("Monir")

itemlist.dump_list()

# exercise the list
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find("Mazin"))
print("Finding item: ", itemlist.find("Chadi"))

# delete an item
itemlist.deleteAt(3)
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find("Mazin"))
itemlist.dump_list()

# try out the Python stack functions

# create a new empty stack
stack = []

# push items onto the stack
stack.append("one")
stack.append("two")
stack.append("three")
stack.append("four")

# print the stack contents
print(stack)

# pop an item off the stack
x = stack.pop()
print(x)
print(stack)

# try out the Python queue functions
from collections import deque

# create a new empty deque object that will function as a queue
queue = deque()

# add some items to the queue
queue.append("one")
queue.append("two")
queue.append("three")
queue.append("four")

# print the queue contents
print(queue)

# pop an item off the front of the queue
x = queue.popleft()
print(x)
print(queue)

# demonstrate hashtable usage


# create a hashtable all at once
items1 = dict({"Name": "Mohamed", "Age": 24, "Country": "Mauritania"})
print(items1)


# create a hashtable progressively
items2 = {}
items2["name"] = "Aziz"
items2["age"] = 18
items2["country"] = "Egypt"
print(items2)

# try to access a nonexistent key
# print(items1["key6"])

# replace an item
items2["age"] = 20
print(items2)

# iterate the keys and values in the dictionary
for key, value in items2.items():
    print("key: ", key, " value: ", value)
