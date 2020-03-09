"""
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""


def count_th(word):
    count = 0
    index = word.find("th")

    if index >= 0:
        count += 1

        word = word[index + len("th") :]
        count += count_th(word)

    return count
