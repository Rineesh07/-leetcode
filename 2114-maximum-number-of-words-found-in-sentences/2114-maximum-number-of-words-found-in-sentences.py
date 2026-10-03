class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_words = 0
        word_cnt = 0
        for sentence in sentences :
            word_cnt = 0
            for word in sentence.split(' '):
                word_cnt += 1
            max_words = max(max_words,word_cnt)
        return max_words
