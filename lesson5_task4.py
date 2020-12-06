from translate import Translator

translator = Translator(to_lang="russian")
word = open("test_3.txt", "r", encoding="utf=8").read()
new_list = []
new_list.append(translator.translate(word + "\n"))

word = open("test_3.txt", "w", encoding="utf=8")
word.writelines(new_list)
