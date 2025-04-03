class WordBreak2:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        length = len(s)
        output = []
        joiner = ' '
        cur_words = []
        word = ''
        for i in range(length):
            word += s[i]
            if word in wordDict:
              cur_words.append(word)
              remaining_word = ''
              j = i+1
              while(j < length):
                remaining_word += s[j]
                if remaining_word in wordDict:
                  cur_words.append(remaining_word)
                  remaining_word = ''
                j += 1

              if len(cur_words) > 0 and j == length:
                output.append(joiner.join(cur_words))
                cur_words.clear()
        return output


