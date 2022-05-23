"""
File: boggle.py
Name: Andy Chi
----------------------------------------
TODO:When user's input a 4x4 letter panel, this program finds out
    all the anagrams that exists.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
# Global
FILE = 'dictionary.txt'
dic_lst = []
# Test: f y c l, i o m g, o r i l, h j h u


def main():
    """
    When user's input a 4x4 letter panel, this program finds out
    all the anagrams that exists.
    """
    start = time.time()
    ####################
    row_1 = (input('1 row of letters: ')).lower()
    if len(row_1.strip()) != 7:
        print('Illegal input')
        return False
    row_2 = (input('2 row of letters: ')).lower()
    if len(row_2.strip()) != 7:
        print('Illegal input')
        return False
    row_3 = (input('3 row of letters: ')).lower()
    if len(row_3.strip()) != 7:
        print('Illegal input')
        return False
    row_4 = (input('4 row of letters: ')).lower()
    if len(row_4.strip()) != 7:
        print('Illegal input')
        return False
    letter_lst = [row_1.split(), row_2.split(), row_3.split(), row_4.split()]
    read_dictionary()
    find_anagrams(letter_lst)
    count = find_anagrams(letter_lst)
    print('There are ' + str(len(count)) + ' words in total.')
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


# letter_lst = [['a', 'f', 't', 'r'], ['b', 'e', 'a', 's'], ['o', 'i', 'p', 'l'], ['w', 'v', 'n', 'm']]
#            = [(0, 0), (0, 1), (0, 2), (0, 3)]
#            = [(1, 0), (1, 1), (1, 2), (1, 3)]
#            = [(2, 0), (2, 1), (2, 2), (2, 3)]
#            = [(3, 0), (3, 1), (3, 2), (3, 3)]


def find_anagrams(s):
    """
    Finds all the adjacent words that exists in 4x4 board filled with letters
    :param s: lst, a nested lst input by users
    :return: lst
    """
    word_lst = []
    for x in range(4):
        for y in range(4):
            anagram_helper(s, x, y, word_lst, str(s[x][y]), [(x, y)])
    return word_lst


def anagram_helper(nest_lst, x, y, ans_lst, word, coordinate):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + i < 4:
                if 0 <= y + j < 4:
                    if (x + i, y + j) not in coordinate:
                        # Choose
                        ch = nest_lst[x + i][y + j]
                        location_tuple = (x + i, y + j)
                        coordinate.append(location_tuple)
                        word += ch
                        if len(word) >= 4 and word not in ans_lst and word in dic_lst:
                            ans_lst.append(word)
                            print('Found \"' + str(word) + '\"')
                        # Explore
                        if has_prefix(word):
                            anagram_helper(nest_lst, x + i, y + j, ans_lst, word, coordinate)
                        # Un-choose
                        word = word[:len(word) - 1]
                        coordinate.pop()


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    with open(FILE, 'r') as f:
        for line in f:
            if len(line.strip()) >= 4:
                dic_lst.append(line.strip())


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for word in dic_lst:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
