# Return a dict with the letter as key and the number of letters in the string as value

import re


def char_count(string: str):
    temp = {}
    for char in string:
        temp[char] = list(string).count(char)
    print(temp)


# Check anagram
def is_anagram(string: str, string2: str):
    # set(string) == set(string2)
    if not set(string) - set(string2):
        print("yes")
    else:
        print("no")


# Return a list of unique elements without using set
def unique_list(lst: list):
    temp = {el: "" for el in lst}
    print(list(temp.keys()))


# Return a reversed list
def reverse_words(string: str):
    print(string.split(" ")[::-1])


# Return the 3 most used words in a string
def top_words(string: str):
    lst = string.split(" ")
    temp = {el: lst.count(el) for el in lst}
    sorted_lst = sorted(temp.items(), key=lambda d: d[1], reverse=True)
    end_lst = [el[0] for el in sorted_lst]
    print(end_lst)


# Check balance of parenthesis
def is_valid(string: str):

    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for el in string:
        if el in mapping.values():
            stack.append(el)
        elif el in mapping:
            if not stack or stack.pop() != mapping[el]:
                return False

    return not stack
    # return True if stack else False / but stack should be empty if a string is valid, so
    # it is not False => True


a = ["flower", "flow", "flight"]


# Return the longest prefix
def longest_prefix(lst: list):
    if len(lst) == 0:
        print("")

    base = lst[0]
    for ind, val in enumerate(base):
        for word in lst[1:]:
            if word[ind] != val:
                return base[0:ind]
    return base


# Given a list of users, return a list of user names who are 18 or older.
def filter_adults(users: list[dict]) -> list[str]:
    # lst = list(filter(lambda d: d.get("age") >= 18, users))
    # result_lst = [el.get("name") for el in lst]
    # return result_lst
    return [user.get("name") for user in users if user.get("age", 0) >= 18]


class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, item: str, price: float):
        self.items[item] = price

    def remove_item(self, item: str):
        self.items.pop(item, None)

    def total(self):
        return sum(self.items.values())


def count_unique_words(text: str):
    lst = re.findall(r"\w+", text.lower())
    return len(set(lst))


def count_unique_letters(text: list, letter: str):
    temp = ""
    for el in text:
        if isinstance(el, str):
            temp += el
    print(temp.count(letter))


count_unique_letters(["python", "y", "yes"], "y")