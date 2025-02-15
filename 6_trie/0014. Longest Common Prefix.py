class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        trie = Trie()
        for word in strs:
            trie.insert(word)

        node = trie.root
        prefix = ""
				
				# len(node.children) == 1 说明当前节点只有一个子节点，即当前路径是唯一的，没有分叉
				# not node.is_word 说明当前节点 不是某个单词的结束节点
				# 如果 node.is_word == True，意味着已经完整地插入了某个单词，不能继续扩展前缀。
        while node and len(node.children) == 1 and not node.is_word:
		        # node.children 是一个 字典 {char: TrieNode}
		        # iter(node.children) 生成一个迭代器，next() 取出唯一的键（即当前路径上的字符）。
            char = next(iter(node.children))
            prefix += char
            node = node.children[char]

        return prefix
