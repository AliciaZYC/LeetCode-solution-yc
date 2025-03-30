class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        dq = deque([(beginWord, 0)])
        # 开始 BFS 遍历
        while dq:
            curr_word, steps = dq.popleft()
            if curr_word == endWord:
                return steps+1
            for i, ch in enumerate(curr_word):
                for new_ch in 'abcdefghijklmnopqrstuvwxyz':
                    if new_ch != ch:  # 跳过和原字符相同的变换
                        mutated = curr_word[:i] + new_ch + curr_word[i+1:]
                        if mutated in wordList:
                            wordList.remove(mutated)  # 标记访问过，避免重复走
                            dq.append((mutated, steps + 1))  # 入队，步数+1

        # 如果遍历完也没找到目标序列，返回 -1
        return 0
