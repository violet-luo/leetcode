class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def get_root(self):
        return self.root
    
    # 插入单词
    def insert(self, word):
        # 指针 node 从根节点开始
        node = self.root
        # 遍历 word 中的字符
        for i in range(len(word)):
            if word[i] not in node.children:
                # 儿子节点中不存在该字符，需要新建一个儿子节点
                node.children[word[i]] = TrieNode()
            # 指针移动至对应字符的儿子节点
            node = node.children[word[i]]
        # 插入的是单词，更新两个存放单词的变量
        node.is_word = True
        node.word = word
        
    # 判断单词 word 是不是在字典树中
    def search(self, word):
        # 指针 node 从根节点开始
        node = self.root
        # 遍历 word 中的字符
        for i in range(len(word)):
            if word[i] not in node.children:
                # 儿子节点中不存在该字符
                # 说明字典树中不存在该单词
                return False
            # 指针移动至对应字符的儿子节点
            node = node.children[word[i]]
        # 循环结束后，只能说明 word 是一个前缀
        # 所以通过 is_word 变量判断 word 是不是一个单词
        return node.is_word
    
    # 判断前缀 prefix 是不是在字典树中
    def startsWith(self, prefix):
        # 指针 node 从根节点开始
        node = self.root
        # 遍历 prefix 中的字符
        for i in range(len(prefix)):
            if prefix[i] not in node.children:
                # 儿子节点中不存在该字符
                # 说明字典树中不存在该前缀
                return False
            # 指针移动至对应字符的儿子节点
            node = node.children[prefix[i]]
        # 循环结束后，证明前缀一定在字典树中
        return True
