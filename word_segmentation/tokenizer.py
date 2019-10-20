"""codes for word segmentation in Chinese"""


class Tokenizer:
    def __init__(self, word_dict):
        self.words = word_dict

    def __left_max_cut(self, sentence, max_len=5):
        word_list = []
        while sentence != "":
            word = sentence[:max_len]
            while word != "":
                if len(word) == 1 or word in self.words:
                    word_list.append(word)
                    sentence = sentence[len(word):]
                    break
                else:
                    word = word[:-1]
        return word_list

    def __right_max_cut(self, sentence, max_len=5):
        word_list = []
        while sentence:
            word = sentence[-max_len:]
            while word:
                if len(word) == 1 or word in self.words:
                    word_list.append(word)
                    sentence = sentence[:-len(word)]
                    break
                else:
                    word = word[-len(word)+1:]

        word_list.reverse()
        return word_list

    def __bi_cut(self, sentence, max_len=5):
        left_word = self.__left_max_cut(sentence, max_len)
        right_word = self.__right_max_cut(sentence, max_len)
        n_left = len(left_word)
        n_right = len(right_word)

        if n_left < n_right:
            return left_word
        if n_left > n_right:
            return right_word

        if left_word == right_word:
            return left_word

        left_count = sum([1 for word in left_word if len(word) == 1])
        right_count = sum([1 for word in right_word if len(word) == 1])

        if left_count < right_count:
            return left_word
        return right_word

    def cut(self, sentence, max_len=5, method="left"):
        if method == "left":
            ret = " ".join(self.__left_max_cut(sentence, max_len))
            return ret
        if method == "right":
            ret = " ".join(self.__right_max_cut(sentence, max_len))
            return ret
        else:
            assert(method == "bi")
            ret = " ".join(self.__bi_cut(sentence, max_len))
            return ret


if __name__ == "__main__":
    word_dict = set(["我", "北京大学", "北京", "你好", "爱", "中国", "大学生", "大学"])
    tokenizer = Tokenizer(word_dict)
    sentence = "我爱你北京大学生"

    word_list = tokenizer.cut(sentence, method="left")
    word_list2 = tokenizer.cut(sentence, method="right")
    word_list3 = tokenizer.cut(sentence, method="bi")
    print(sentence)
    print(word_list)
    print(word_list2)
    print(word_list3)



