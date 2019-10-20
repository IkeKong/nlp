"""codes for word segmentation in Chinese"""


class Tokenizer:
    def __init__(self, word_dict):
        self.words = word_dict

    def left_max_cut(self, sentence, max_len=5):
        words_list = []
        while sentence != "":
            word = sentence[:max_len]
            while word != "":
                if len(word) == 1 or word in self.words:
                    words_list.append(word)
                    sentence = sentence[len(word):]
                    break
                else:
                    word = word[:-1]
        return words_list

    def right_max_cut(self, sentence, max_len=5):
        pass

if __name__ == "__main__":
    word_dict = set(["我", "北京大学", "北京大学生", "北京", "你好", "爱", "中国"])
    tokenizer = Tokenizer(word_dict)
    sentence = "我爱你北京大学生"

    word_list = tokenizer.left_max_cut(sentence)
    print(word_list)




