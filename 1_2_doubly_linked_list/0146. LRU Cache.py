class ListNode:
    def __init__(self, key=None, value=None):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def delete(self, node: ListNode):
        if self.length == 1: # 链表中只有一个节点
            self.head = None
            self.tail = None
            self.length -=1
        else:
            if node == self.head:
                self.head = node.next
                node.next.prev = None
            elif node == self.tail:
                self.tail = node.prev
                node.prev.next = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            self.length -=1

    def insert_to_front(self, key, val):
        if self.length == 0: # 如果链表为空，插入的节点就是头节点
            new_node = ListNode(key, val)
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return new_node
        else: # 如果链表不为空，将新节点插入到链表头部
            new_node = ListNode(key, val)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
            return new_node
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.dll = DoublyLinkedList()
        
    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.dll.delete(node)
            inserted_node = self.dll.insert_to_front(key,node.value)
            self.dic[key] = inserted_node # 更新哈希表中的值
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic: # 如果键已存在，把节点移到头部
            self.dic[key].value = value # 更新该键的值

            node = self.dic[key] # 获取该键对应的节点
            self.dll.delete(node)
            inserted_node = self.dll.insert_to_front(key,node.value) # 将节点插入到头部
            self.dic[key] = inserted_node # 更新哈希表中的值
            
        else:
            if self.capacity > self.dll.length: # 链表未满
                inserted_node = self.dll.insert_to_front(key, value)
                self.dic[key] = inserted_node
            else: 
                remove_node = self.dll.tail # 链表已满，删除最久未使用的尾结点
                self.dll.delete(remove_node)
                del self.dic[remove_node.key]
                inserted_node = self.dll.insert_to_front(key, value)
                self.dic[key] = inserted_node
