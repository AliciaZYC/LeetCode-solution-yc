class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        current_words = []
        current_length = 0  # sum of the lengths of words (no spaces)
        for w in words:
            # If adding this word plus (at least one space per gap) exceeds maxWidth
            if current_words and current_length + len(w) + len(current_words) > maxWidth:
                # Justify the current line
                total_spaces = maxWidth - current_length
                gaps = len(current_words) - 1
                if gaps == 0:
                    # Only one word in this line
                    res.append(current_words[0] + ' ' * (maxWidth - len(current_words[0])))
                else:
                    # Distribute spaces as evenly as possible
                    space_per_gap, extra = divmod(total_spaces, gaps)
                    line = ""
                    for i in range(gaps):
                        line += current_words[i]
                        # add the base number of spaces
                        line += ' ' * space_per_gap
                        # add one more space to the first 'extra' gaps
                        if i < extra:
                            line += ' '
                    # Add the last word
                    line += current_words[-1]
                    res.append(line)
                # Reset for the next line
                current_words = []
                current_length = 0
            # Add the current word to the line
            current_words.append(w)
            current_length += len(w)
        # Handle the last line (left-justified)
        if current_words:
            line = ' '.join(current_words)
            # pad the end with spaces
            line += ' ' * (maxWidth - len(line))
            res.append(line)
        return res