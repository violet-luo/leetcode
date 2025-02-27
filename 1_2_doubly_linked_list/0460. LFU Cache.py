class ListNode:
    def __init__(self, key=None, value=None, freq=1):
        self.key = key
        self.value = value
        self.freq = freq  # 访问频率，LFU 需要记录每个节点的访问次数
        self.prev = None
        self.next = None

class DoublyLinkedList: # 同146
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def insert_to_front(self, node: ListNode):
        node.next = self.head
        node.prev = None
        if self.head:
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = node
        self.length += 1
    
    def delete(self, node: ListNode):
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            if node == self.head:
                self.head = node.next
                self.head.prev = None
            elif node == self.tail:
                self.tail = node.prev
                self.tail.next = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
        self.length -= 1

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0  # 记录当前最小访问频率
        # key -> ListNode 映射
        # { A: (A, 1, freq=2), B: (B, 2, freq=1) }
        self.node_map = {}  
        # freq -> DoublyLinkedList 映射，每个访问频率对应一个双向链表
        # {1: [ (1, "A") <-> (2, "B") <-> (3, "C") ]}
        self.freq_map = defaultdict(DoublyLinkedList)  
    
    def _update_freq(self, node: ListNode): # 比146多了这个
        freq = node.freq
        self.freq_map[freq].delete(node)  # 将node从当前频率的链表中删除
        
        # 如果 min_freq 1的链表为空，更新 min_freq 到2
        if self.freq_map[freq].length == 0 and self.min_freq == freq:
            self.min_freq += 1 
        
        node.freq += 1  # 增加访问频率
        self.freq_map[node.freq].insert_to_front(node)  # 将node插入到新频率的链表中
    
    def get(self, key: int) -> int:
        """ 获取键对应的值，如果存在则更新频率 """
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        self._update_freq(node)  # 访问一次，增加频率
        return node.value
    
    def put(self, key: int, value: int) -> None:
        """ 插入或更新键值对 """ 
        if key in self.node_map: # 如果key存在
            node = self.node_map[key]
            node.value = value  # 更新值
            self._update_freq(node)  # 更新访问频率
        else: # 如果key不存在
            if len(self.node_map) == self.capacity: # 缓存已满，删除LFU节点
                removed_node = self.freq_map[self.min_freq].tail
                self.freq_map[self.min_freq].delete(removed_node) # 删除最久未使用的点
                del self.node_map[removed_node.key]
						
						# 加入新节点 
						# 不能放在else里，因为不管怎么样都要增加这个节点
            new_node = ListNode(key, value)
            self.node_map[key] = new_node  # 添加到字典
            self.freq_map[1].insert_to_front(new_node)  # 插入到访问频率为1的列表中
            self.min_freq = 1
