from collections import Counter
from typing import List

class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        # 步骤1: 统计所有单词中每个字符的总出现次数
        char_counter = Counter(char for word in words for char in word)
        
        # 步骤2: 计算全局可用的"字符对"总数（每2个相同字符组成1对，用于回文对称部分）
        total_pairs = sum(count // 2 for count in char_counter.values())
        
        # 步骤3: 将单词按长度升序排序（贪心策略：优先构造短单词，最大化回文串数量）
        sorted_lengths = sorted(len(word) for word in words)
        
        valid_count = 0  # 记录能成功构造成回文串的单词数量
        
        # 步骤4: 遍历每个单词所需字符对
        for length in sorted_lengths:
            # 每个单词构建回文串需消耗 length//2 个字符对（中间单字符无需配对）
            needed_pairs = length // 2
            total_pairs -= needed_pairs
            
            # 若剩余字符对仍非负，说明当前单词可成功构造
            if total_pairs >= 0:
                valid_count += 1
            else:
                # 一旦资源不足，后续更长单词必然无法构造（因已升序排序）
                break
        
        return valid_count