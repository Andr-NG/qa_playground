from collections import defaultdict


text = "veikxddtjgpixjrux srxiqrczp cxaldqsvsxpzn xrlxovsjy ervh cdtxwnahcvj, abc"
brokenLetters = "wqchprenozi"

lst = text.split(" ")
count = 0

words = text.split()
broken_set = set(brokenLetters)
count = 0

for word in words:
    if not (set(word) & broken_set):  # пересечение множеств пустое
        count += 1
print(count)

# Нужен порядок → list
# Нужны уникальные значения, операции пересечения и объединения, быстрый поиск → set
# Нужен ключ → значение → dict
# Нужен неизменяемый объект → tuple
# Нужна очередь/стек → deque
# Нужно подсчитать → Counter

# понимания задачи -> структура данных -> код