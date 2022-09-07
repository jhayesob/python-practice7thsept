from functools import cmp_to_key


def solution(s):
    # return word with greatest number of repeated chars
    # print(f'{s}')
    words = []
    word_start = 0

    for i in range(len(s)):
        # print(f'iteration {i}; char = "{s[i]}"')
        if s[i] == ' ':
            words.append(s[word_start:i])
            word_start = i + 1
            if word_start != 0:
                pass
                # print(f'word_start now = {word_start}')
        if i == len(s) - 1:
            words.append(s[word_start:])

    # add words to dictionary as keys
    # dictionary values need to be map to represent chars and their num repeats
    print(words)
    words.sort(key=cmp_to_key(cmp), reverse=True)
    print(words)


def cmp(str_a, str_b):
    # return word with great number of repeating chars
    str_a_dict = {}
    str_b_dict = {}
    for c in str_a:
        if c not in str_a_dict.keys():
            str_a_dict[c] = 1
        else:
            str_a_dict[c] += 1
    for c in str_b:
        if c not in str_b_dict.keys():
            str_b_dict[c] = 1
        else:
            str_b_dict[c] += 1

    a_totals = 0
    b_totals = 0
    for i in str_a_dict.values():
        if i > 1:
            a_totals += i
    for i in str_b_dict.values():
        if i > 1:
            b_totals += i

    if a_totals > b_totals:
        return 1
    elif a_totals < b_totals:
        return -1
    else:
        return 0

    # add all to int array, add up elements above 1? return greatest array


if __name__ == '__main__':
    solution('word woord woorrd')
