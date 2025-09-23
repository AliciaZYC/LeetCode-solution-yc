class TrieNode:
    def __init__(self):
        self.children = {}     # 子节点：字符 -> TrieNode
        self.is_end = False    # 是否为某个单词的结尾

class Trie:
    def __init__(self):
        self.root = TrieNode()  # 根节点为空节点

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            # 如果当前字符不存在于子节点中，则创建
            if char not in node.children:
                node.children[char] = TrieNode()
            # 移动到下一个节点
            node = node.children[char]
        node.is_end = True  # 最后一个节点标记为单词结尾

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    def _find_node(self, s: str) -> TrieNode:
        node = self.root
        for char in s:
            if char not in node.children:
                return None
            node = node.children[char]
        return node



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)