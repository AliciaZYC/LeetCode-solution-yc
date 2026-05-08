class WordDistance:

    def __init__(self, wordsDict: List[str]):
        # 初始化字典，用于存储每个单词出现的所有位置索引
        self.dic = {}
        # 记录单词数组的总长度，用于初始化最短距离的初始值
        self.l = len(wordsDict)
        # 遍历单词数组，记录每个单词出现的所有位置
        for index, word in enumerate(wordsDict):
            # 将当前索引添加到对应单词的索引列表中
            # self.dic.get(word, []) 如果单词不存在则返回空列表
            self.dic[word] = self.dic.get(word, []) + [index]  # 注意：这里应该是 index 而不是 i

    def shortest(self, word1: str, word2: str) -> int:
        # 获取两个单词的所有出现位置列表
        l1, l2 = self.dic[word1], self.dic[word2]  # 注意：这里应该是 self.dic 而不是 self.dict
        # 双指针初始化，分别指向两个列表的起始位置
        i = j = 0
        # 初始化结果为数组最大长度（最坏情况下的距离）
        res = self.l
        # 使用双指针遍历两个索引列表
        while i < len(l1) and j < len(l2):
            # 计算当前两个位置的距离，更新最小值
            res = min(res, abs(l1[i] - l2[j]))
            # 移动较小索引的指针，以寻找更小的距离
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)