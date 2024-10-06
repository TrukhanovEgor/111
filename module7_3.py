import os.path

class WordsFinder:

    def __init__(self, *files):
        self.file_names = []

        for item in files:
            if isinstance(item , str):
                self.file_names.append(item)

            if isinstance(item, dict):
                for key in item.keys():
                    self.file_names.append(key)
                    if os.path.isfile(key):
                        os.remove(key)

                    with open(key, "w", encoding='utf-8') as file:
                        for val in item.values():
                            for val_ in val:
                                file.write(f"{val_}\n")

    def get_all_words(self):
        dict_ = {}
        subst_list = [",", '.', '=', '!', '?', ';', ':', ' - ']

        for key in self.file_names:
            str_ = ""
            with open(key, 'r', encoding='utf-8') as file:
                for line in file:
                    line_ = line.rstrip()
                    for item_ in subst_list:
                        line_ = line_.replace(item_, " ")

                    str_ += " " + line_.lower()
                str_ = str_.replace(' ', "", 1)

                dict_[key] = str_.split()

        return dict_

    def find(self, word):
        dic_main = self.get_all_words()

        word = word.lower()
        for key, values in dic_main.items():
            i = 0
            for val in values:
                i += 1
                if val == word:
                    return {key: i}

            return None

    def count(self, word):
        dic_main = self.get_all_words()

        word = word.lower()
        for key, values in dic_main.items():
            i = 0
            for val in values:
                if val == word:
                    i += 1

            if i > 0: return {key: i}

        return None


def start():
    dic_1 = {"test_file.txt": ["It's a text for task Найти везде,",
                               "Используйте его для самопроверки.",
                               "Успехов в решении задачи!",
                               "text text text"]}

    finder1 = WordsFinder(dic_1)
    finder1.get_all_words()
    print(finder1.get_all_words())  # Все слова
    print(finder1.find('TEXT'))   # 3 слово по счёту
    print(finder1.count('teXT'))  # 4 слова teXT в тексте всего

    print()
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего


if __name__ == '__main__':
    start()